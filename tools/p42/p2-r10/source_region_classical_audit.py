#!/usr/bin/env python3
"""A deliberately bounded, source-aware classical points-to/region competitor.

Information budget: the same exact pinned grpc Go source, authored repaired
Go source trees and selected client sizes available to the native runner.
No runtime log or prereg label is read by the predictor; only by the auditor.
Unknown statements deliberately yield ABSTAIN, not successful extrapolation.
This is NOT a general Go static analyzer and claims no novel TCS law.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

CANDIDATES = ["base_shared", "provider_repair", "adapter_repair", "nop_repair"]
SIZES = (1024, 1025, 2048)

class Abstain(Exception):
    pass

def require(predicate: bool, reason: str) -> None:
    if not predicate:
        raise Abstain(reason)

def compact(s: str) -> str:
    return re.sub(r"\s+", "", re.sub(r"//[^\n]*", "", s))

def func_body(source: str, pattern: str) -> str:
    match = re.search(pattern, source)
    require(match is not None, "missing expected signature "+pattern)
    start = source.find("{", match.end())
    require(start >= 0, "missing source function body")
    depth = 1
    for i in range(start+1, len(source)):
        if source[i] == "{": depth += 1
        elif source[i] == "}":
            depth -= 1
            if depth == 0: return source[start+1:i]
    raise Abstain("unbalanced source")

def parse_real_grpc_library(grpc: Path) -> int:
    pool = (grpc/"mem/buffer_pool.go").read_text()
    buffers = (grpc/"mem/buffers.go").read_text()
    all_pool = compact(pool)
    all_buf = compact(buffers)
    require("bufferPoolingThreshold=1<<10" in all_buf, "unknown original threshold")
    thresh_func = compact(func_body(buffers, r"func\s+IsBelowBufferPoolingThreshold\s*\(\s*size\s+int\s*\)\s*bool\s*"))
    require("returnsize<=bufferPoolingThreshold" in thresh_func, "unknown threshold predicate")

    copy_src = compact(func_body(buffers, r"func\s+Copy\s*\(\s*data\s+\[\]byte\s*,\s*pool\s+BufferPool\s*\)\s*Buffer\s*"))
    for piece in ("ifIsBelowBufferPoolingThreshold(len(data))", "make(SliceBuffer,len(data))",
                  "copy(buf,data)", "returnbuf", "buf:=pool.Get(len(data))",
                  "copy(*buf,data)", "returnNewBuffer(buf,pool)"):
        require(piece in copy_src, "grpc mem.Copy changed or unknown: "+piece)
    require(copy_src.index("returnbuf") < copy_src.index("buf:=pool.Get(len(data))"),"unexpected copy branch")

    new_buf = compact(func_body(buffers, r"func\s+NewBuffer\s*\(\s*data\s+\*\[\]byte\s*,\s*pool\s+BufferPool\s*\)\s*Buffer\s*"))
    for piece in ("b.origData=data", "b.data=*data", "b.pool=pool","returnb"):
        require(piece in new_buf, "unknown grpc NewBuffer ownership: "+piece)
    free_buf = compact(func_body(buffers, r"func\s+\(b\s+\*buffer\)\s+Free\s*\(\s*\)\s*"))
    require("b.pool.Put(b.origData)" in free_buf,"unknown grpc reference release")
    nop = compact(func_body(pool, r"func\s+\(NopBufferPool\)\s+Get\s*\(\s*length\s+int\s*\)\s+\*\[\]byte\s*"))
    require("make([]byte,length)" in nop and "return&b" in nop,"unknown original Nop get")
    return 1024

def parse_candidate(root: Path, original: Path) -> tuple[str,bool]:
    root_code=compact((root/"root.go").read_text())
    pcode=(root/"provider.go").read_text()
    provider_get=compact(func_body(pcode,r"func\s+\(p\s+\*sharedPool\)\s+Get\s*\(\s*n\s+int\s*\)\s+\*\[\]byte\s*"))
    provider_put=compact(func_body(pcode,r"func\s+\(p\s+\*sharedPool\)\s+Put\s*\(\s*b\s+\*\[\]byte\s*\)\s*"))
    require("p.puts++" in provider_put,"unknown authored provider return accounting")
    if "v:=p.backing[:n]" in provider_get and "p.backing=make([]byte,n)" in provider_get:
        shared_region="shared"
    elif "v:=make([]byte,n)" in provider_get and "p.backing[:n]" not in provider_get:
        shared_region="fresh"
    else: raise Abstain("unrecognized authored provider allocation semantics")

    if "returnselection{mem.NopBufferPool{},func()int{return0}}" in root_code:
        return "fresh", False
    if ("b:=&legacyPool{}" in root_code and
        "returnselection{&legacyAdapter{b},func()int{returnb.puts}}" in root_code):
        adapter_code=(root/"adapter.go").read_text()
        adapter_get=compact(func_body(adapter_code,r"func\s+\(p\s+\*legacyAdapter\)\s+Get\s*\(\s*n\s+int\s*\)\s+\*\[\]byte\s*"))
        adapter_put=compact(func_body(adapter_code,r"func\s+\(p\s+\*legacyAdapter\)\s+Put\s*\(\s*v\s+\*\[\]byte\s*\)\s*"))
        old_get=compact(func_body(adapter_code,r"func\s+\(p\s+\*legacyPool\)\s+Get\s*\(\s*n\s+int\s*\)\s+\[\]byte\s*"))
        old_put=compact(func_body(adapter_code,r"func\s+\(p\s+\*legacyPool\)\s+Put\s*\(\s*b\s+\[\]byte\s*\)\s*"))
        require("v:=p.backend.Get(n)" in adapter_get and "return&v" in adapter_get,"unknown adapter Get")
        require("returnmake([]byte,n)" in old_get,"unknown legacy allocation")
        require("p.backend.Put(*v)" in adapter_put and "p.puts++" in old_put,"unknown legacy release")
        return "fresh",True
    if ("p:=&sharedPool{}" in root_code and
        "returnselection{p,func()int{returnp.puts}}" in root_code):
        return shared_region,True
    raise Abstain("unrecognized provider selection/root assembly")

def predict(grpc:Path,root:Path,threshold:int, size:int)->dict:
    region,accounted=parse_candidate(root,grpc)
    if size<=threshold: return {"first":65,"puts":0,"region":"slice-copy"}
    return {"first":66 if region=="shared" else 65,"puts":2 if accounted else 0,"region":region}

def negative_controls(grpc:Path,gen:Path,thresh:int)->None:
    base=gen/"base_shared"
    root = (base/"root.go").read_text()
    provider = (base/"provider.go").read_text()
    # Do not actually overwrite any generated/native Go candidate; use a temp isolated copy.
    import tempfile, shutil
    with tempfile.TemporaryDirectory() as tmp:
        t=Path(tmp)
        shutil.copytree(base,t/"case")
        p=t/"case"
        (p/"provider.go").write_text(provider.replace("v:=p.backing[:n]","v:=make([]byte,n)"))
        require(predict(grpc,p,thresh,2048)["first"]==65,"mutation did not flip alias prediction")
        (p/"provider.go").write_text(provider.replace("v:=p.backing[:n]","v:=unknown()"))
        try: predict(grpc,p,thresh,2048)
        except Abstain: pass
        else: raise AssertionError("unknown provider semantics must abstain")
        (p/"provider.go").write_text(provider)
        (p/"root.go").write_text((gen/"nop_repair"/"root.go").read_text())
        require(predict(grpc,p,thresh,2048)["puts"]==0,"root mutation did not flip return prediction")
        # Fail-closed original grpc core mutation: copy original files to separate temp source.
        shutil.copytree(grpc/"mem",t/"original"/"mem")
        buffers=t/"original"/"mem"/"buffers.go"
        body=buffers.read_text()
        require("pool.Get(len(data))" in body,"missing source mutation anchor")
        buffers.write_text(body.replace("pool.Get(len(data))","anotherSource(len(data))",1))
        try: parse_real_grpc_library(t/"original")
        except Abstain: pass
        else: raise AssertionError("unknown original Copy should abstain")

def parse_go_receipts(s:str)->dict:
    # These are observed independent native-Go values; never supplied to predictor.
    pattern=r"R10_BOUNDARY name=([a-z_]+) size=(\d+) first=(\d+) returned=(\d+)"
    rows={(m[1],int(m[2])):{"first":int(m[3]),"puts":int(m[4])}
         for m in re.finditer(pattern,s)}
    pattern2=r"R10_NATIVE name=([a-z_]+) first=(\d+) isolated=(true|false) returned=(\d+)"
    for m in re.finditer(pattern2,s):
        rows[(m[1],2048)]={"first":int(m[2]),"puts":int(m[4])}
    return rows

def main()->None:
    if len(sys.argv)!=5:
        raise SystemExit("usage: source_region_classical_audit.py ORIGINAL_GRPC GENERATED_GO NATIVE_LOG OUT_JSON")
    grpc,gen,log,out=map(Path,sys.argv[1:])
    threshold=parse_real_grpc_library(grpc)
    frozen=json.loads((Path(__file__).parent/"frozen_threshold_region_and_classical_rival.json").read_text())
    require(threshold==frozen["upstream"]["pool_threshold_bytes"],"threshold mismatch with sealed prediction")
    native=parse_go_receipts(log.read_text())
    records=[]
    for name in CANDIDATES:
        for size in SIZES:
            result=predict(grpc,gen/name,threshold,size)
            expected=next(x for x in frozen["predictions"] if x["size"]==size)
            if result["first"]!=expected["observed_first"][name] or result["puts"]!=expected["returned_puts"][name]:
                raise AssertionError("classical model disagrees with frozen prediction "+name+"/"+str(size))
            if native.get((name,size))!={"first":result["first"],"puts":result["puts"]}:
                raise AssertionError("independent source analysis disagrees with original Go "+name+"/"+str(size))
            records.append({"candidate":name,"size":size,"source_region":result["region"],
                            "classical_prediction":{"first":result["first"],"puts":result["puts"]},
                            "original_go_observed":native[(name,size)]})
            print("R10_CLASSICAL_MATCH name=%s size=%d region=%s first=%d puts=%d"
                  %(name,size,result["region"],result["first"],result["puts"]))
    negative_controls(grpc,gen,threshold)
    out.write_text(json.dumps({"protocol":"R10_SOURCE_GROUNDED_CLASSICAL_REGION_AUDIT_V1",
       "bounded_classical_matches":len(records),"mutation_controls":4,
       "nonclaims":["No full Go analysis","No new-law advantage","Same source and demand evidence as native run"],
       "cases":records},indent=2)+"\n")
    print("R10_CLASSICAL_MATCH_12_OF_12_AND_FOUR_NEGATIVE_CONTROLS_PASS")

if __name__=="__main__":
    main()
