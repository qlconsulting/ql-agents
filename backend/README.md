# QL Agents — Agent Server: Resumable Sessions API

New capability for this repo: the agent server now persists conversation
histories and agent run state in a SQLite database so an in-progress agent run
can be resumed after a disconnect or an app reload.

## New endpoint (the task)

```
GET /api/sessions/{session_id}
```
Returns the full **conversation history** plus the **agent run state** for a
session. A client that holds an existing `session_id` can call this to
reconstruct and continue the run where it left off. Returns `404` if the
session does not exist.

Response shape:
```json
{
  "session": { "id": "...", "agent_name": "...", "status": "active",
               "metadata_json": "{...}", "created_at": "...", "updated_at": "..." },
  "messages": [ { "role": "user|assistant", "content": "...", "created_at": "..." } ],
  "run_state": { "position": 7, "step_id": "gather_pricing",
                 "variables": { "...": "..." }, "updated_at": "..." }
}
```

## Supporting endpoints

| Method | Path | Purpose |
|--------|------|---------|
| `POST` | `/api/sessions` | Create a new agent session |
| `GET`  | `/api/sessions` | List sessions (optionally `?agent_name=<name>`) |
| `GET`  | `/api/sessions/{id}/history` | Alias of the resume payload |
| `POST` | `/api/sessions/{id}/messages` | Append a user/assistant message |
| `POST` | `/api/sessions/{id}/state` | Persist run state (position, step, variables) |
| `GET`  | `/api/sessions/{id}` | **Fetch history + run state (resume)** |
| `GET`  | `/health` | Liveness probe |

## Storage

SQLite database at `backend/agent_sessions.db` with three tables:
`session`, `message`, `run_state`. The schema is created automatically on
startup.

## Run & test

```bash
python backend/main.py            # serves on http://0.0.0.0:8000 (FastAPI/uvicorn)
python backend/test_sessions.py   # end-to-end test of the resume flow
```

Files changed in this task:
- `backend/main.py` — agent server with the new resume endpoint + persistence.
- `backend/test_sessions.py` — integration test (all checks pass).