#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

def need(text: str, token: str, label: str) -> None:
    if token not in text:
        raise SystemExit(f"fidelity failure: {label}")

def forbid(text: str, token: str, label: str) -> None:
    if token in text:
        raise SystemExit(f"fidelity failure: {label}")

def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--arm",required=True,choices=["WIDE_BOUNDARY_REUSE","CAPABILITY_SEGREGATED"])
    ap.add_argument("--subject",required=True,type=Path)
    a=ap.parse_args()

    core=(a.subject/"packages/trueforge-core/src/core/web-search/WebSearchProvider.ts").read_text()
    exa=(a.subject/"packages/trueforge-core/src/core/web-search/ExaWebSearchProvider.ts").read_text()
    web=(a.subject/"packages/trueforge-core/src/core/capabilities/builtins/WebSearch.ts").read_text()
    schema=(a.subject/"packages/trueforge/src/schemas/webSearchProvider.ts").read_text()
    catalog=(a.subject/"packages/trueforge/catalog/web-search-catalog.yaml").read_text()
    resolver=(a.subject/"packages/trueforge/src/websearch/providers.ts").read_text()

    for text,token,label in [
        (core,"Exa = 'exa'","Exa enum"),
        (schema,"type: z.literal('exa')","Exa schema"),
        (catalog,"- type: exa","Exa catalog"),
        (resolver,"new ExaWebSearchProvider","Exa resolver"),
        (exa,"async search(","Exa search"),
    ]:
        need(text,token,label)

    # Phase 1 must remain physically absent from treatment source.
    for text in [core,exa,web,schema,catalog,resolver]:
        forbid(text.lower(),"tavily","premature Tavily treatment")

    if a.arm=="WIDE_BOUNDARY_REUSE":
        need(core,"export interface IWebSearchProvider","wide interface")
        need(core,"  fetch(input:","wide mandatory fetch")
        need(exa,"async fetch(","wide truthful Exa fetch")
        forbid(web,"hasWebFetchCapability","wide must not change exposure semantics")
    else:
        need(core,"export interface IWebSearchCapability","seg search capability")
        need(core,"export interface IWebFetchCapability","seg fetch capability")
        need(core,"Partial<IWebFetchCapability>","seg optional composition")
        forbid(exa,"async fetch(","seg Exa must remain search-only")
        need(web,"hasWebFetchCapability","seg conditional exposure")
        need(web,"buildWebSearchOnlyInstruction","seg instruction fidelity")

    print("TREATMENT_FIDELITY_PASS")

if __name__=="__main__":
    main()
