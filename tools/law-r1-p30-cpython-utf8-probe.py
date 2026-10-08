#!/usr/bin/env python3
import codecs
import json
import platform
import sys

def arm(prefix):
    decoder = codecs.getincrementaldecoder("utf-8")(errors="strict")
    now = decoder.decode(bytes([prefix]), final=False)
    raw_buffer, flags = decoder.getstate()
    before = dict(Q=1,R="cpython-codecs-utf8-incremental",G=[1,1,1,1],H_pending_length=len(raw_buffer),H_pending_hex=raw_buffer.hex(),H_flag=flags,O_now=now)
    try:
        later = decoder.decode(bytes([0xA9]), final=True)
        future = dict(ok=1,unicode=later,utf8=later.encode("utf-8").hex())
    except UnicodeDecodeError as exc:
        future = dict(ok=0,error=exc.__class__.__name__)
    return dict(before=before,future=future)
a=arm(0xC2)
b=arm(0xC3)
def public_W(x):
    z=x["before"]
    return {k:z[k] for k in ("Q","R","G","H_pending_length")}
current_equal=a["before"]["O_now"]==b["before"]["O_now"]==""
same_W=public_W(a)==public_W(b)
future_different=a["future"]!=b["future"]
prospective_pending_content_separates=a["before"]["H_pending_hex"]!=b["before"]["H_pending_hex"]
record={
 "stage":"G8 LAW-R1-P30","candidate":"CPython UTF-8 incremental decoder",
 "runtime":sys.version,"implementation":platform.python_implementation(),
 "arm_a":a,"arm_b":b,
 "current_equal":current_equal,
 "same_W":same_W,
 "future_different":future_different,
 "prospective_pending_content_separates":prospective_pending_content_separates
}
print(json.dumps(record,indent=2,sort_keys=True,ensure_ascii=False))
