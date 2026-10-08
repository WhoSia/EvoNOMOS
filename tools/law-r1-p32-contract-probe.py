#!/usr/bin/env python3
"""P32 exact-source certificate-notification contract negative control.

Checks pinned Uptime Kuma call/default/template source; no real transport oracle
and no claim of a prospective discovery.
"""
import argparse, hashlib, json, re
from pathlib import Path

BIRTH = "398482d590daaac0d44e288c9be3bc6f6667f8b8"
BLOBS = {
    "server/model/monitor.js":"2ad572e53ed051825425f8783c91195cbd243d77",
    "server/notification-providers/notification-provider.js":"42079176c01cd2e6d46160bb6f6408d4ba263fd7",
    "server/notification.js":"b1a42d003a92e3760f6d33a4be59784a9cb4dbf2"
}

def checked(world):
    src = {}
    custody = {}
    for path, expected in BLOBS.items():
        raw=(world/path).read_bytes()
        sha=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
        if sha!=expected: raise ValueError(f"unmatched source {path}: {sha}")
        src[path]=raw.decode("utf-8")
        custody[path]={"git_blob":sha,"sha256":hashlib.sha256(raw).hexdigest()}
    def one_section(path,marker,n=4000):
        s=src[path]
        ix=s.find(marker)
        if ix<0 or s.find(marker,ix+len(marker))>=0: raise ValueError("missing/ambiguous marker "+marker)
        return s[ix:ix+n]

    p=one_section("server/model/monitor.js","async sendCertNotificationByTargetDays(")
    anchor="await Notification.send("
    k=p.find(anchor); close=p.find("\n                );",k)
    if k<0 or close<0: raise ValueError("unrecognized bounded call")
    args=p[k+len(anchor):close]
    # Mask the JS template literal before separating top-level comma arguments.
    args=re.sub(r"\x60[^\x60]*\x60",'"MESSAGE"',args,flags=re.S)
    n=0; depth=0;quote=None;escape=False
    for c in args:
        if quote:
            if escape:escape=False
            elif c=="\\":escape=True
            elif c==quote:quote=None
        elif c in "'\"":quote=c
        elif c in "([{":depth+=1
        elif c in ")]}":depth-=1
        elif c=="," and depth==0:n+=1
    if quote or depth!=0:raise ValueError("unbalanced bounded call")
    argc=n+1
    assert argc==2,argc
    assert "JSON.parse(notification.config)" in args

    dispatch=one_section("server/notification.js","static async send(notification, msg, monitorJSON = null, heartbeatJSON = null)")
    assert "this.providerList[notification.type].send(notification, msg, monitorJSON, heartbeatJSON)" in dispatch
    template=one_section("server/notification-providers/notification-provider.js","async renderTemplate(template, msg, monitorJSON, heartbeatJSON)")
    for term in ['let monitorName = "Monitor Name not available";',
                 'let monitorHostnameOrURL = "testing.hostname";',
                 'if (monitorJSON !== null)',
                 'monitorName = monitorJSON["name"]',
                 "monitorHostnameOrURL = this.extractAddress(monitorJSON)"]:
        if term not in template:raise ValueError("missing template fallback/branch "+term)

    return {
        "schema":"P32_CERT_CONTEXT_SOURCE_NEGATIVE_CONTROL_V1",
        "birth_commit":BIRTH,"custody":custody,
        "post_birth_real_issue":"https://github.com/louislam/uptime-kuma/issues/7639",
        "issue_outcome_was_read_before_analysis":True,
        "certificate_notification_call_argument_count":argc,
        "dispatcher_monitor_context_has_default_null":True,
        "template_dummy_defaults_for_null_monitor_context":True,
        "typed_path":["monitor.js::sendCertNotificationByTargetDays",
                      "notification.js::Notification.send",
                      "notification-provider.js::renderTemplate"],
        "membership_registry_location_does_not_repair_missing_call_argument":True,
        "CSDG_B2_can_also_represent_this_context_flow":True,
        "behavioral_oracle":"NOT_EXECUTED",
        "novelty":"NO_H_VS_B2_DISCRIMINATION",
        "authority":"BOUNDED_STATIC_SOURCE_SIGNATURE_CHECK_ONLY"
    }

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--world",type=Path,required=True)
    ap.add_argument("--out",type=Path,required=True)
    a=ap.parse_args()
    out=checked(a.world)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("P32_CONTRACT_CONTEXT_SOURCE_NEGATIVE_CONTROL=PASS")
