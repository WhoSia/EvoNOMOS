#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path
def need(t,s,m):
    if s not in t: raise SystemExit("fidelity failure: "+m)
def forbid(t,s,m):
    if s in t: raise SystemExit("fidelity failure: "+m)
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--arm",required=True);ap.add_argument("--subject",required=True,type=Path);a=ap.parse_args()
    core=(a.subject/"packages/trueforge-core/src/core/web-search/WebSearchProvider.ts").read_text()
    tav=(a.subject/"packages/trueforge-core/src/core/web-search/TavilyWebSearchProvider.ts").read_text()
    schema=(a.subject/"packages/trueforge/src/schemas/webSearchProvider.ts").read_text()
    resolver=(a.subject/"packages/trueforge/src/websearch/providers.ts").read_text()
    for t,s,m in [(core,"Tavily = 'tavily'","enum"),(tav,"async search(","search"),(schema,"type: z.literal('tavily')","schema"),(resolver,"new TavilyWebSearchProvider","resolver"),(tav,"X-Tavily-Access-Mode","keyless"),(tav,"Authorization: 'Bearer '","bearer")]: need(t,s,m)
    if a.arm=="WIDE_BOUNDARY_REUSE":
        need(core,"  fetch(input:","wide mandatory fetch");need(tav,"async fetch(","wide extract")
        forbid(core,"Partial<IWebFetchCapability>","wide optional fetch")
    elif a.arm=="CAPABILITY_SEGREGATED":
        need(core,"Partial<IWebFetchCapability>","seg optional fetch");need(core,"hasWebFetchCapability","seg capability detector");forbid(tav,"async fetch(","seg Tavily fetch forbidden")
    else: raise SystemExit("unknown arm")
    print("TREATMENT_FIDELITY_PASS")
if __name__=="__main__":main()
