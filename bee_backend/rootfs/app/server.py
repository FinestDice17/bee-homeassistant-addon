from __future__ import annotations

import json
import os
import subprocess
from typing import Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Bee Backend", version="0.1.0")

BEE_BINARY = os.getenv("BEE_BINARY_PATH", "/usr/local/bin/bee")


class TodoCreateRequest(BaseModel):
    text: str
    alarm_at: str | None = None


def run_bee_command(args: list[str]) -> Any:
    cmd = [BEE_BINARY, *args]
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=False,
            timeout=60,
        )
    except FileNotFoundError as err:
        raise HTTPException(status_code=500, detail=f"Bee binary not found: {BEE_BINARY}") from err
    except subprocess.TimeoutExpired as err:
        raise HTTPException(status_code=504, detail="Bee command timed out") from err

    if result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip() or "Unknown Bee CLI error"
        raise HTTPException(status_code=500, detail=detail)

    stdout = result.stdout.strip()
    if not stdout:
        return {"ok": True}

    try:
        return json.loads(stdout)
    except json.JSONDecodeError:
        return {"raw": stdout}


@app.get("/health")
def health() -> dict[str, Any]:
    return {"ok": True, "service": "bee_backend", "bee_binary": BEE_BINARY}


@app.get("/status")
def status() -> Any:
    return run_bee_command(["status", "--json"])


@app.get("/me")
def me() -> Any:
    return run_bee_command(["me", "--json"])


@app.get("/today")
def today() -> Any:
    return run_bee_command(["today", "--json"])


@app.get("/now")
def now() -> Any:
    return run_bee_command(["now", "--json"])


@app.get("/facts")
def facts(limit: int = 25) -> Any:
    return run_bee_command(["facts", "list", "--limit", str(limit), "--json"])


@app.get("/todos")
def todos(limit: int = 25) -> Any:
    return run_bee_command(["todos", "list", "--limit", str(limit), "--json"])


@app.post("/todos")
def create_todo(payload: TodoCreateRequest) -> Any:
    args = ["todos", "create", "--text", payload.text]
    if payload.alarm_at:
        args.extend(["--alarm-at", payload.alarm_at])
    args.append("--json")
    return run_bee_command(args)
