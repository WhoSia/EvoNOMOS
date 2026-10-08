#!/usr/bin/env python3
"""Prospectively frozen CPython 3.12.12 predictive-state census.
No outcome-selected sampling. Raw rows and exact bit-cover results are emitted.
"""
import codecs
import itertools
import json
import platform
import sys

PREFIXES = tuple(range(0xC2, 0xE0))
SUFFIXES = tuple(range(0x80, 0xC0))
assert len(PREFIXES) == 30 and len(SUFFIXES) == 64

def observe(prefix, suffix):
    decoder = codecs.getincrementaldecoder("utf-8")(errors="strict")
    now = decoder.decode(bytes((prefix,)), final=False)
    pending, flag = decoder.getstate()
    try:
        later = decoder.decode(bytes((suffix,)), final=True)
        future = {"ok": True, "utf8": later.encode("utf-8").hex()}
    except UnicodeDecodeError as exc:
        future = {"ok": False, "error": exc.__class__.__name__}
    return {
        "prefix": prefix, "suffix": suffix,
        "current": now,
        "pending_hex": pending.hex(), "pending_length": len(pending),
        "state_flag": flag,
        "coarse_W": [1, "cpython-codecs-utf8-incremental", [1,1,1,1], len(pending)],
        "future": future,
    }

def census():
    rows = [observe(p,s) for s in SUFFIXES for p in PREFIXES]
    edges = []
    per_suffix = {}
    for s in SUFFIXES:
        group = [r for r in rows if r["suffix"] == s]
        e = []
        for a,b in itertools.combinations(group,2):
            if a["coarse_W"] == b["coarse_W"] and a["future"] != b["future"]:
                e.append((a["prefix"], b["prefix"]))
        per_suffix[str(s)] = len(e)
        edges.extend((s,p,q) for p,q in e)
    return rows,edges,per_suffix

rows, edges, per_suffix = census()
repeated, edges_repeat, per_suffix_repeat = census()
assert rows == repeated and edges == edges_repeat and per_suffix == per_suffix_repeat

def separates(p,q,bits):
    return any(bool((p>>i)&1) != bool((q>>i)&1) for i in bits)

distinct_edges = sorted({(p,q) for _,p,q in edges})
minimal = []
for k in range(9):
    options = [list(bits) for bits in itertools.combinations(range(8),k)
               if all(separates(p,q,bits) for p,q in distinct_edges)]
    if options:
        minimal = options
        break
basis = minimal[0] if minimal else []
deletion_necessary = {str(i):not all(separates(p,q,[j for j in basis if j!=i])
                                         for p,q in distinct_edges)
                      for i in basis}
result = {
  "stage":"G8 LAW-R1-P30",
  "candidate":"CPython UTF-8 predictive collision census",
  "implementation":platform.python_implementation(),
  "runtime":sys.version,
  "source_commit_expected":"4a5632fbf9bf59477c540e3f53fa7cdbeea3e3f5",
  "population":{"prefixes":[f"{x:02x}" for x in PREFIXES],
                "suffixes":[f"{x:02x}" for x in SUFFIXES]},
  "rows":rows,
  "counts":{"measurements":len(rows),
            "collision_edges":len(edges),
            "distinct_collision_pairs":len(distinct_edges),
            "per_suffix_edges":per_suffix,
            "repeated_census_identical":True},
  "bit_cover":{"minimum_number_of_bits":len(basis),
               "all_minimal_bases":minimal,
               "deletion_necessary":deletion_necessary},
  "claims":{"external_mechanism_replications":0,"law_r2_authorized":False}
}
print(json.dumps(result,sort_keys=True,separators=(",",":")))
