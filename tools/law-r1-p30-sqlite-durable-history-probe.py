#!/usr/bin/env python3
"""P30 Phase II-F source-pinned SQLite durable-history candidate probe.
The sqlite3 executable must be built from the separately frozen SQLite revision.
Each SQL call runs in a new process; each arm is a new disk-backed database.
"""
import argparse
import hashlib
import json
import os
import pathlib
import subprocess
import tempfile

SOURCE = "f3d536d37825302e31ed0eddd811c689f38f85a3"
PAIRS = ((True, False), (True, True), (False, False), (False, True))
ROUNDS = 3

def sql(executable, db, statement):
    command = [str(executable), "-json", str(db), statement]
    proc = subprocess.run(command, capture_output=True, text=True, check=False, timeout=30)
    if proc.returncode:
        raise RuntimeError(f"SQLite process failed (rc={proc.returncode}) on {statement!r}: {proc.stderr}")
    data = proc.stdout.strip()
    try:
        return json.loads(data) if data else []
    except json.JSONDecodeError as err:
        raise RuntimeError(f"Non-JSON SQLite CLI result for {statement!r}: {data[:200]!r}") from err

def snapshot(cli, db, auto):
    schema = sql(cli, db, "SELECT type,name,tbl_name,sql FROM sqlite_schema ORDER BY type,name;")
    visible = sql(cli, db, "SELECT id,note FROM events ORDER BY id;")
    count = sql(cli, db, "SELECT count(*) AS n FROM events;")
    journal = sql(cli, db, "PRAGMA journal_mode;")
    foreign_keys = sql(cli, db, "PRAGMA foreign_keys;")
    read_uncommitted = sql(cli, db, "PRAGMA read_uncommitted;")
    hidden = sql(cli, db, "SELECT name,seq FROM sqlite_sequence WHERE name='events';") if auto else None
    current = {
        "Q": 1,
        "R": "exact-source-sqlite3-file-cli",
        "G": {
            "autoincrement": auto,
            "schema": schema,
            "visible_rows": visible,
            "row_count": count,
            "journal_mode": journal,
            "foreign_keys": foreign_keys,
            "read_uncommitted": read_uncommitted,
            "intervention_sql": "INSERT INTO events(note) VALUES ('probe') RETURNING id;"
        },
        "O_now": visible
    }
    return current, hidden

def arm(cli, workspace, round_id, auto, history):
    label = ("AUTO" if auto else "ROWID") + ("_HISTORY" if history else "_FRESH")
    db = workspace / f"r{round_id}_{label}.db"
    table = "events(id INTEGER PRIMARY KEY" + (" AUTOINCREMENT" if auto else "") + ", note TEXT NOT NULL)"
    init = sql(cli, db, f"CREATE TABLE {table};")
    if history:
        sql(cli, db, "BEGIN; INSERT INTO events(note) VALUES ('history'); DELETE FROM events; COMMIT;")
    before, hidden = snapshot(cli, db, auto)
    # A separate SQLite process applies the identical prospective action, after all observations.
    future_rows = sql(cli, db, "INSERT INTO events(note) VALUES ('probe') RETURNING id;")
    result = {
        "round": round_id,
        "arm": label,
        "autoincrement": auto,
        "history": history,
        "before": before,
        "H_sequence": hidden,
        "future": future_rows,
        "reopened_process_per_operation": True
    }
    return result

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sqlite-bin", required=True)
    args = ap.parse_args()
    cli = pathlib.Path(args.sqlite_bin).resolve()
    if not cli.is_file():
        raise RuntimeError(f"Missing exact-source sqlite3 executable: {cli}")
    version = sql(cli, ":memory:", "SELECT sqlite_version() AS version;")
    if version != [{"version": "3.46.1"}]:
        raise RuntimeError(f"Unsupported SQLite version: {version}")
    with tempfile.TemporaryDirectory(prefix="p30_sqlite_durable_") as root:
        workspace = pathlib.Path(root)
        rows = [arm(cli, workspace, i, auto, history)
                for i in range(ROUNDS) for auto, history in PAIRS]
    out = {
        "stage": "G8 LAW-R1-P30",
        "candidate": "SQLite durable history predictive collision",
        "expected_sqlite_source_commit": SOURCE,
        "observed_sqlite_version": version[0]["version"],
        "rounds": ROUNDS,
        "arm_order": ["AUTO_FRESH","AUTO_HISTORY","ROWID_FRESH","ROWID_HISTORY"],
        "rows": rows,
        "source_binary_path": str(cli),
        "source_binary_sha256": hashlib.sha256(cli.read_bytes()).hexdigest(),
        "evidence_note": "Each SQL statement is a new sqlite3 process against a file database. Current view is captured before future INSERT."
    }
    print(json.dumps(out, sort_keys=True, separators=(",",":")))

if __name__ == "__main__":
    main()
