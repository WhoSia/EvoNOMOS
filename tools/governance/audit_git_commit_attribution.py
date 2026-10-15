#!/usr/bin/env python3
"""Read-only first-parent raw-Git attribution gate. Python 3.9+; no external packages."""
import argparse
import json
import re
import sys
import urllib.request

EXPECTED = "71053804+WhoSia@users.noreply.github.com"
API = "https://api.github.com/repos/WhoSia/EvoNOMOS/git/commits/"
TRAILER = re.compile(r"(?im)^\s*co-authored-by\s*:\s*(.+)$")
BOT = re.compile(r"(?i)\[bot\]|github-actions|dependabot|renovate|bot@")


def inspect(c, expected):
    faults = []
    for kind in ("author", "committer"):
        obj = c.get(kind) or {}
        if obj.get("email", "").casefold() != expected.casefold():
            faults.append(kind + ":unexpected-email")
        if BOT.search(obj.get("name", "") + " " + obj.get("email", "")):
            faults.append(kind + ":bot-marker")
    trailers = TRAILER.findall(c.get("message") or "")
    if trailers:
        faults.append("co-authored-by-present")
    return {"sha": c["sha"], "faults": faults,
            "author": c.get("author"), "committer": c.get("committer"),
            "coauthors": trailers,
            "signature": (c.get("verification") or {}).get("reason")}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--sha", required=True, help="Frozen full Git commit SHA")
    p.add_argument("--limit", type=int, default=10)
    p.add_argument("--email", default=EXPECTED)
    p.add_argument("--report", default="")
    a = p.parse_args()
    if not re.fullmatch(r"[0-9a-fA-F]{40}", a.sha) or not 1 <= a.limit <= 500:
        p.error("sha must be 40 hex digits, limit 1..500")
    sha = a.sha
    records = []
    try:
        for _ in range(a.limit):
            req = urllib.request.Request(API + sha, headers={
                "Accept": "application/vnd.github+json",
                "User-Agent": "EvoNOMOS-raw-git-audit",
                "X-GitHub-Api-Version": "2022-11-28"})
            with urllib.request.urlopen(req, timeout=20) as handle:
                obj = json.load(handle)
            if obj.get("sha", "").casefold() != sha.casefold():
                raise ValueError("SHA response mismatch")
            records.append(inspect(obj, a.email))
            parents = obj.get("parents") or []
            if not parents:
                break
            sha = parents[0]["sha"]
    except Exception as error:
        print(f"INCOMPLETE: {error}", file=sys.stderr)
        return 2
    report = {"start_sha": a.sha, "first_parent_only": True,
              "examined": len(records), "requested": a.limit,
              "not_identity_proof": True, "results": records}
    if a.report:
        with open(a.report, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
            f.write("\n")
    bad = sum(bool(x["faults"]) for x in records)
    print(f"{'FAIL' if bad else 'PASS'}: {len(records)} raw first-parent Git commits; {bad} attribution violations")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
