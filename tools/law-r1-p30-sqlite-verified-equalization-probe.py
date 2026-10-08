#!/usr/bin/env python3
"""Phase II-H prospective SQLite state intervention with verified delivery.
Do not reuse the failed Phase II-G INSERT OR REPLACE manipulation.
"""
import argparse
import hashlib
import json
import pathlib
import subprocess
import tempfile

SQLITE_COMMIT="f3d536d37825302e31ed0eddd811c689f38f85a3"
FOSSIL_ID="c9c2ab54ba1f5f46360f1b4f35d849cd3f080e6fc2b6c60e91b16c63f69a1e33"
FUTURE_SQL="INSERT INTO events(note) VALUES ('probe') RETURNING id;"

def query(exe, db, statement):
    child=subprocess.run([str(exe),"-json",str(db),statement],
                         capture_output=True,text=True,check=False,timeout=30)
    if child.returncode:
        raise RuntimeError(f"sqlite3 command failed: rc={child.returncode}, SQL={statement!r}, stderr={child.stderr}")
    raw=child.stdout.strip()
    return json.loads(raw) if raw else []

def current(exe,db):
    return {
        "schema":query(exe,db,"SELECT type,name,tbl_name,sql FROM sqlite_schema ORDER BY type,name;"),
        "visible":query(exe,db,"SELECT id,note FROM events ORDER BY id;"),
        "count":query(exe,db,"SELECT count(*) AS n FROM events;"),
        "journal_mode":query(exe,db,"PRAGMA journal_mode;"),
        "foreign_keys":query(exe,db,"PRAGMA foreign_keys;"),
        "read_uncommitted":query(exe,db,"PRAGMA read_uncommitted;")
    }

def seq(exe,db):
    return query(exe,db,"SELECT name,seq FROM sqlite_sequence WHERE name='events' ORDER BY rowid;")

def measure(exe,root,iteration,history,target):
    arm=f"ROUND_{iteration}_HISTORY_{int(history)}_TARGET_{target}"
    db=root/(arm+".db")
    query(exe,db,"CREATE TABLE events(id INTEGER PRIMARY KEY AUTOINCREMENT, note TEXT NOT NULL);")
    if history:
        query(exe,db,"BEGIN; INSERT INTO events(note) VALUES ('history'); DELETE FROM events; COMMIT;")
    before=current(exe,db)
    h_before=seq(exe,db)
    if len(h_before)==0:
        treatment=f"INSERT INTO sqlite_sequence(name,seq) VALUES('events',{target});"
        branch="INSERT_IF_MISSING"
    elif len(h_before)==1:
        treatment=f"UPDATE sqlite_sequence SET seq={target} WHERE name='events';"
        branch="UPDATE_IF_EXISTS"
    else:
        raise RuntimeError(f"Ambiguous duplicate sequence rows before treatment in {arm}: {h_before}")
    query(exe,db,treatment)
    h_after=seq(exe,db)
    after=current(exe,db)
    fidelity=(h_after==[{"name":"events","seq":target}] and before==after)
    # Non-delivery must be rejected before collecting outcome Y.
    if not fidelity:
        raise RuntimeError(f"Intervention delivery failed in {arm}: before={h_before}; after={h_after}; visible_equal={before==after}")
    future=query(exe,db,FUTURE_SQL)
    return {
        "round":iteration,
        "history":history,
        "target_seq":target,
        "arm":arm,
        "before":before,
        "H_before":h_before,
        "treatment_branch":branch,
        "treatment_sql":treatment,
        "H_after":h_after,
        "after":after,
        "fidelity_verified_before_future":True,
        "future":future,
        "fresh_cli_process_per_sql_operation":True
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sqlite-bin",required=True)
    args=ap.parse_args()
    exe=pathlib.Path(args.sqlite_bin).resolve()
    if not exe.is_file():
        raise RuntimeError(f"SQLite CLI missing: {exe}")
    version=query(exe,":memory:","SELECT sqlite_version() AS version;")
    if version!=[{"version":"3.46.1"}]:
        raise RuntimeError(f"SQLite exact version mismatch: {version}")
    with tempfile.TemporaryDirectory(prefix="p30_sqlite_IIH_") as base:
        root=pathlib.Path(base)
        rows=[measure(exe,root,i,history,target)
              for i in range(3) for target in (0,7) for history in (False,True)]
    out={
        "stage":"G8 LAW-R1-P30",
        "candidate":"SQLite verified sequence equalization",
        "source_commit_expected":SQLITE_COMMIT,
        "fossil_uuid_expected":FOSSIL_ID,
        "version":version[0]["version"],
        "rounds":3,"target_values":[0,7],
        "arm_order":["ROUND_{r}_HISTORY_0_TARGET_{t}","ROUND_{r}_HISTORY_1_TARGET_{t}"],
        "rows":rows,
        "sqlite_binary_sha256":hashlib.sha256(exe.read_bytes()).hexdigest(),
        "claim_ceiling":"Local causal predictive repair only, not LAW-R2"
    }
    print(json.dumps(out,sort_keys=True,separators=(",",":")))

if __name__=="__main__":
    main()
