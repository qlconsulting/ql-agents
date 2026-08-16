"""
Integration test for the resumable agent sessions endpoints.

Runs the FastAPI app via uvicorn in a background thread and talks to it with
stdlib urllib (avoids the starlette TestClient/httpx2 version mismatch in this
environment).

Flow exercised:
  1. health
  2. create a session
  3. append conversation messages (user + assistant)
  4. persist agent run state (mid-step)
  5. NEW endpoint: GET /api/sessions/{id} -> fetch history + run state intact
  6. history alias endpoint
  7. list sessions
  8. missing session returns 404
"""
import json
import threading
import time
import urllib.request
import urllib.error
import uvicorn
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))

import main

import socket


def free_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


HOST, PORT = "127.0.0.1", free_port()
BASE = f"http://{HOST}:{PORT}"


def http(method, path, body=None):
    req = urllib.request.Request(BASE + path, method=method)
    req.add_header("Content-Type", "application/json")
    data = json.dumps(body).encode() if body is not None else None
    try:
        with urllib.request.urlopen(req, data=data) as resp:
            return resp.status, json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        return e.code, None


def start_server():
    main.init_db()
    config = uvicorn.Config(main.app, host=HOST, port=PORT, log_level="error")
    server = uvicorn.Server(config)
    thread = threading.Thread(target=server.run, daemon=True)
    thread.start()
    for _ in range(100):
        try:
            urllib.request.urlopen(BASE + "/health", timeout=1)
            return
        except Exception:
            time.sleep(0.1)
    raise RuntimeError("server did not start")


start_server()
print("== 1. Health ==")
print(http("GET", "/health"))

print("\n== 2. Create session ==")
code, r = http("POST", "/api/sessions", {"agent_name": "market_analyzer",
                                         "metadata": {"company": "Acme"}})
assert code == 200, (code, r)
sid = r["session"]["id"]
print("session id:", sid)
assert r["messages"] == []
assert r["run_state"]["position"] == 0

print("\n== 3. Append conversation messages ==")
http("POST", f"/api/sessions/{sid}/messages",
     {"role": "user", "content": "Analyze the competitive landscape for Acme."})
http("POST", f"/api/sessions/{sid}/messages",
     {"role": "assistant", "content": "Scanning market; 3 competitors found."})
http("POST", f"/api/sessions/{sid}/messages",
     {"role": "user", "content": "Drill into competitor #2 pricing."})

print("\n== 4. Persist mid-step run state ==")
code, r = http("POST", f"/api/sessions/{sid}/state",
               {"position": 7, "step_id": "gather_pricing",
                "variables": {"competitor": "RivalCorp", "price_range": "$99-$199"}})
assert code == 200, (code, r)

print("\n== 5. NEW ENDPOINT: fetch resume payload ==")
code, payload = http("GET", f"/api/sessions/{sid}")
assert code == 200, (code, payload)
print("messages recovered:", len(payload["messages"]))
for m in payload["messages"]:
    print("   -", m["role"], ":", m["content"][:45] + "...")
assert len(payload["messages"]) == 3
assert payload["messages"][0]["role"] == "user"
print("run_state recovered:", payload["run_state"])
assert payload["run_state"]["position"] == 7
assert payload["run_state"]["step_id"] == "gather_pricing"
assert payload["run_state"]["variables"]["competitor"] == "RivalCorp"

print("\n== 6. History alias endpoint ==")
code, r = http("GET", f"/api/sessions/{sid}/history")
assert code == 200
print("history alias ok, messages:", len(r["messages"]))

print("\n== 7. List sessions ==")
code, r = http("GET", "/api/sessions")
assert code == 200
print("sessions:", r["sessions"])

print("\n== 8. Missing session returns 404 ==")
code, _ = http("GET", "/api/sessions/does-not-exist")
assert code == 404, code
print("404 ok")

print("\nALL TESTS PASSED - resumable agent sessions work end to end.")