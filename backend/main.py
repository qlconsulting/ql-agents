"""
QL Agents - Agent Server
========================
A FastAPI backend that persists conversation histories and agent run state in a
SQLite database so that agent sessions can be RESUMED after a disconnect or an
app reload.

Primary new endpoint (this task):
    GET /api/sessions/{session_id}
        Returns the full conversation history and the agent run state for a
        given session, allowing a client to reconstruct and continue an agent
        run where it left off.

Supporting endpoints:
    POST /api/sessions                        Create a new agent session
    GET  /api/sessions                        List all sessions (summary)
    POST /api/sessions/{session_id}/messages  Append a user/assistant message
    POST /api/sessions/{session_id}/state     Persist agent run state
    GET  /api/sessions/{session_id}/history   Alias for the full resume payload

Data model
----------
session(id TEXT PK, agent_name TEXT, status TEXT, metadata_json TEXT,
        created_at TEXT, updated_at TEXT)
message(id INTEGER PK AUTOINC, session_id TEXT, role TEXT, content TEXT,
        created_at TEXT)
run_state(session_id PK, position INTEGER, step_id TEXT, variables_json TEXT,
          updated_at TEXT)
"""

import json
import sqlite3
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# --------------------------------------------------------------------------- #
# Database setup
# --------------------------------------------------------------------------- #

DB_PATH = Path(__file__).resolve().parent / "agent_sessions.db"


def utc_now() -> str:
    """ISO-8601 timestamp in UTC (used for every persisted row)."""
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _connect() -> sqlite3.Connection:
    """Open a connection with row access by column name enabled."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db() -> None:
    """Create all tables on startup (idempotent)."""
    with _connect() as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS session (
                id            TEXT PRIMARY KEY,
                agent_name    TEXT NOT NULL,
                status        TEXT NOT NULL DEFAULT 'active',
                metadata_json TEXT NOT NULL DEFAULT '{}',
                created_at    TEXT NOT NULL,
                updated_at    TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS message (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                role       TEXT NOT NULL,
                content    TEXT NOT NULL,
                created_at TEXT NOT NULL,
                FOREIGN KEY (session_id) REFERENCES session(id)
            );

            CREATE TABLE IF NOT EXISTS run_state (
                session_id     TEXT PRIMARY KEY,
                position       INTEGER NOT NULL DEFAULT 0,
                step_id        TEXT,
                variables_json TEXT NOT NULL DEFAULT '{}',
                updated_at     TEXT NOT NULL,
                FOREIGN KEY (session_id) REFERENCES session(id)
            );

            CREATE INDEX IF NOT EXISTS idx_message_session
                ON message (session_id, id);
            """
        )


# --------------------------------------------------------------------------- #
# Pydantic request/response models
# --------------------------------------------------------------------------- #

class SessionCreate(BaseModel):
    agent_name: str
    metadata: Optional[Dict[str, Any]] = None


class MessageIn(BaseModel):
    role: str
    content: str


class StateIn(BaseModel):
    position: int = 0
    step_id: Optional[str] = None
    variables: Optional[Dict[str, Any]] = None


# --------------------------------------------------------------------------- #
# App + CORS
# --------------------------------------------------------------------------- #

app = FastAPI(title="QL Agents - Agent Server", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def _startup() -> None:
    init_db()


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #

def _get_session_or_404(conn: sqlite3.Connection, session_id: str) -> sqlite3.Row:
    row = conn.execute(
        "SELECT * FROM session WHERE id = ?", (session_id,)
    ).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Session %s not found" % session_id)
    return row


def _build_resume_payload(conn: sqlite3.Connection, session_id: str) -> Dict[str, Any]:
    """Assemble the full resumable payload for one session."""
    sess = _get_session_or_404(conn, session_id)

    messages = conn.execute(
        "SELECT role, content, created_at FROM message "
        "WHERE session_id = ? ORDER BY id",
        (session_id,),
    ).fetchall()

    state = conn.execute(
        "SELECT position, step_id, variables_json, updated_at "
        "FROM run_state WHERE session_id = ?",
        (session_id,),
    ).fetchone()

    return {
        "session": dict(sess),
        "messages": [dict(m) for m in messages],
        "run_state": _coerce_state(state),
    }


def _coerce_state(state: Optional[sqlite3.Row]) -> Dict[str, Any]:
    if state is None:
        return {"position": 0, "step_id": None, "variables": {}, "updated_at": None}
    out = dict(state)
    try:
        out["variables"] = json.loads(out.get("variables_json") or "{}")
    except (TypeError, ValueError):
        out["variables"] = {}
    out.pop("variables_json", None)
    return out


# --------------------------------------------------------------------------- #
# New endpoint (task): fetch conversation history + run state for resuming
# --------------------------------------------------------------------------- #

@app.get("/api/sessions/{session_id}")
def get_session(session_id: str) -> Dict[str, Any]:
    """
    Fetch the full conversation history and agent run state for a session.

    This is the backbone of resumable agent sessions. A client that loses its
    connection can call this endpoint with the session id it already holds and
    reconstruct the entire in-progress run:
      - `messages`  -> prior turns so the LLM context can be replayed
      - `run_state` -> where the agent stopped (step, variables, position)

    Returns 404 if the session does not exist.
    """
    with _connect() as conn:
        return _build_resume_payload(conn, session_id)


@app.get("/api/sessions/{session_id}/history")
def get_session_history(session_id: str) -> Dict[str, Any]:
    """Alias for /api/sessions/{session_id} - clearer naming for resume flows."""
    return get_session(session_id)


# --------------------------------------------------------------------------- #
# Supporting endpoints
# --------------------------------------------------------------------------- #

@app.post("/api/sessions")
def create_session(payload: SessionCreate) -> Dict[str, Any]:
    """Create a new agent session and return its id + empty resume payload."""
    session_id = uuid.uuid4().hex
    now = utc_now()
    meta = json.dumps(payload.metadata or {})
    with _connect() as conn:
        conn.execute(
            "INSERT INTO session (id, agent_name, status, metadata_json, "
            "created_at, updated_at) VALUES (?, ?, 'active', ?, ?, ?)",
            (session_id, payload.agent_name, meta, now, now),
        )
        conn.execute(
            "INSERT INTO run_state (session_id, position, step_id, "
            "variables_json, updated_at) VALUES (?, 0, NULL, '{}', ?)",
            (session_id, now),
        )
        conn.commit()
    with _connect() as conn:
        return _build_resume_payload(conn, session_id)


@app.get("/api/sessions")
def list_sessions(agent_name: Optional[str] = None) -> Dict[str, Any]:
    """List all sessions (optionally filtered by agent) as lightweight summaries."""
    with _connect() as conn:
        q = ("SELECT s.*, "
             "(SELECT COUNT(*) FROM message m WHERE m.session_id = s.id) AS message_count "
             "FROM session s")
        params: tuple = ()
        if agent_name:
            q += " WHERE s.agent_name = ?"
            params = (agent_name,)
        q += " ORDER BY s.updated_at DESC"
        rows = conn.execute(q, params).fetchall()
        return {"sessions": [dict(r) for r in rows]}


@app.post("/api/sessions/{session_id}/messages")
def add_message(session_id: str, payload: MessageIn) -> Dict[str, Any]:
    """Append a message to a session's conversation history."""
    now = utc_now()
    with _connect() as conn:
        _get_session_or_404(conn, session_id)
        conn.execute(
            "INSERT INTO message (session_id, role, content, created_at) "
            "VALUES (?, ?, ?, ?)",
            (session_id, payload.role, payload.content, now),
        )
        conn.execute(
            "UPDATE session SET updated_at = ? WHERE id = ?", (now, session_id)
        )
        conn.commit()
        return _build_resume_payload(conn, session_id)


@app.post("/api/sessions/{session_id}/state")
def save_state(session_id: str, payload: StateIn) -> Dict[str, Any]:
    """Persist the agent run state so a session can be resumed mid-step."""
    now = utc_now()
    variables = json.dumps(payload.variables or {})
    with _connect() as conn:
        _get_session_or_404(conn, session_id)
        conn.execute(
            "INSERT INTO run_state (session_id, position, step_id, "
            "variables_json, updated_at) VALUES (?, ?, ?, ?, ?) "
            "ON CONFLICT(session_id) DO UPDATE SET position=excluded.position, "
            "step_id=excluded.step_id, variables_json=excluded.variables_json, "
            "updated_at=excluded.updated_at",
            (session_id, payload.position, payload.step_id, variables, now),
        )
        conn.execute(
            "UPDATE session SET updated_at = ? WHERE id = ?", (now, session_id)
        )
        conn.commit()
        return _build_resume_payload(conn, session_id)


# --------------------------------------------------------------------------- #
# Health + demo runner
# --------------------------------------------------------------------------- #

@app.get("/health")
def health() -> Dict[str, str]:
    return {"status": "ok", "service": "ql-agents-agent-server"}


if __name__ == "__main__":
    import uvicorn

    init_db()
    uvicorn.run(app, host="0.0.0.0", port=8000)