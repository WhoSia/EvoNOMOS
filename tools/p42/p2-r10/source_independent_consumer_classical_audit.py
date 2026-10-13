#!/usr/bin/env python3
"""R10-P4 equal-source classical reference-count/observer analysis.

This is a restricted recognizer for exact original Go source semantics, NOT a
general static analyzer, and it makes predictions before consuming Go logs.
Unknown content => ABSTAIN; native outputs are used for checking only.
"""
import json
import re
import sys
from pathlib import Path

def require(cond, msg):
    if not cond:
        raise AssertionError("ABSTAIN_OR_MISMATCH: "+msg)

def flatten(s):
    return re.sub(r"\s+","",re.sub(r"//[^\n]*","",s))

def extract_body(s, signature):
    m=re.search(signature,s)
    require(m is not None,"missing Go signature "+signature)
    i=s.find("{",m.end())
    require(i>=0,"missing function start")
    depth=1
    for j in range(i+1,len(s)):
        if s[j]=="{":depth+=1
        elif s[j]=="}":
            depth-=1
            if depth==0:return flatten(s[i+1:j])
    raise AssertionError("unbalanced function")

def predict_source(grpc,thanos,otel):
    buffer_slice=(grpc/"mem/buffer_slice.go").read_text()
    buffers=(grpc/"mem/buffers.go").read_text()
    legacy=(thanos/"codec_stringlabels.go").read_text()
    slicelabels=(thanos/"codec_slicelabels.go").read_text()
    encoding=(otel/"encoding.go").read_text()
    mb=extract_body(buffer_slice,r"func\s+\(s\s+BufferSlice\)\s+MaterializeToBuffer\s*\(")
    require("iflen(s)==1{" in mb and "s[0].Ref()" in mb and "returns[0]" in mb,"original single-buffer reference retained")
    require("buf:=pool.Get(sLen)" in mb and "returnNewBuffer(buf,pool)" in mb,"original multibuffer copy and ownership")
    nb=extract_body(buffers,r"func\s+NewBuffer\s*\(")
    require("b.origData=data" in nb and "b.pool=pool" in nb and "b.refs.Add(1)" in nb,"gRPC original ref/init")
    free=extract_body(buffers,r"func\s+\(b\s+\*buffer\)\s+Free\s*\(")
    require("b.refs.Add(-1)" in free and "b.pool.Put(b.origData)" in free,"gRPC original last-ref release")
    default=extract_body(legacy,r"func\s+materializeForUnmarshal\s*\(")
    nop=extract_body(slicelabels,r"func\s+materializeForUnmarshal\s*\(")
    require("data.MaterializeToBuffer(mem.DefaultBufferPool())" in default,"Thanos pooled path")
    require("returnbuf.ReadOnlyData(),buf.Free" in default,"Thanos original cleanup path")
    require("data.MaterializeToBuffer(nopPool)" in nop and "returnbuf.ReadOnlyData(),nil" in nop,"Thanos nil-return path")
    marshal=extract_body(encoding,r"func\s+\(c\s+\*codecV2\)\s+Marshal\s*\(")
    require("buf:=otelBufferPool.Get(size)" in marshal and "m.MarshalProto((*buf)[:size])" in marshal
            and "return[]mem.Buffer{mem.NewBuffer(buf,otelBufferPool)},nil" in marshal,
            "OTEL source original own pool/use/free")
    return {
      "default":{"cleanup":True,"puts":1,"thanos_first":65,"otel_first":67,"otel_second":68},
      "slicelabels":{"cleanup":False,"puts":0,"thanos_first":65,"otel_first":67,"otel_second":68}
    }

def read_obs(log,tag):
    hits=re.findall(r"R10_P4_REAL_SOURCE_CROSS_MODULE variant=(\w+) thanos_first=(\d+) otel_first=(\d+) otel_second=(\d+) callback=(true|false) thanos_put=(\d+)",log)
    matches=[m for m in hits if m[0]==tag]
    require(len(matches)==1,"expected one independent original-Go observation for "+tag)
    m=matches[0]
    return {"cleanup":m[4]=="true","puts":int(m[5]),"thanos_first":int(m[1]),"otel_first":int(m[2]),"otel_second":int(m[3])}

def main():
    if len(sys.argv)!=6:
        raise SystemExit("usage: classical_p4.py grpc_dir thanos_dir otel_dir logs_dir out_json")
    grpc,than,otel,logs,out=map(Path,sys.argv[1:])
    computed=predict_source(grpc,than,otel)
    frozen=json.loads((Path(__file__).parent/"frozen_p4_independent_consumer_and_noncircular_solid.json").read_text())
    require(frozen["protocol"]=="EVONOMOS_P42_P2_R10_P4_INDEPENDENT_CLIENT_OWNERSHIP_AND_CONDITIONAL_SOLID_PRESEAL_V1","freeze mismatch")
    verified=[]
    for spec in frozen["predictions"]:
        tag=spec["tag"]
        expected={"cleanup":spec["cleanup_present"],"puts":spec["after_final_cleanup_put"],"thanos_first":spec["byte_first"],"otel_first":spec["otel_first"],"otel_second":68}
        require(computed[tag]==expected,"source / preseal disagreement "+tag)
        fname="default-original-go.log" if tag=="default" else "slicelabels-original-go.log"
        observed=read_obs((logs/fname).read_text(),tag)
        require(computed[tag]==observed,"classical / original Go disagreement "+tag)
        verified.append({"build_tag":tag,"source_based_classical_prediction":computed[tag],"native_original_go":observed})
        print("R10_P4_CLASSICAL_EQUAL_SOURCE_MATCH tag=%s puts=%d cleanup=%s"%(tag,observed["puts"],str(observed["cleanup"]).lower()))
    # Distinguishes genuine source constructs; reject a mutated Thanos release signature.
    broken=(than/"codec_stringlabels.go").read_text().replace("buf.Free","nil")
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        dest=Path(d)
        for src in [than/"codec_stringlabels.go",than/"codec_slicelabels.go"]:
            (dest/src.name).write_text(src.read_text())
        (dest/"codec_stringlabels.go").write_text(broken)
        try:predict_source(grpc,dest,otel)
        except AssertionError:pass
        else:raise AssertionError("classical source-control mutation should be rejected")
    out.write_text(json.dumps({"protocol":"R10_P4_EQUAL_SOURCE_CLASSICAL_ORIGINAL_GO_V1","models":verified,
      "native_model_agreement":"2_OF_2","source_mutation_rejected":True,
      "boundary":"finite exact fragment / not mechanically proven full-Go semantics / no novelty advantage"},indent=2)+"\n")
    print("R10_P4_TWO_REAL_CLIENT_BUILD_CONTEXTS_CLASSICAL_ADEQUACY_PASS")

if __name__=="__main__":main()
