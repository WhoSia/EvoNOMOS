"""P37-E4 original-source audit for bounded owner/capability graph provenance.

Only asserts exact source-API call-site evidence and SHA digests; it does NOT
derive a complete source-edit graph and must not claim semantic program proof.
"""
import hashlib
import json
import sys
from pathlib import Path

repo_root=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(".").resolve()
checks={
    "Gorilla_CookieStore_New_DecodeMulti":(
        "original-gorilla-sessions/store.go","securecookie.DecodeMulti("),
    "Gorilla_CookieStore_Save_EncodeMulti":(
        "original-gorilla-sessions/store.go","securecookie.EncodeMulti("),
    "SCS_Load_server_side_StoreFind":(
        "original-scs/data.go","s.doStoreFind(ctx, token)"),
    "SCS_Commit_server_side_StoreCommit":(
        "original-scs/data.go","s.doStoreCommit(ctx, sd.token, b, sd.expiry)"),
    "SCS_new_opaque_random_token":(
        "original-scs/data.go","func generateToken() (string, error)"),
    "Bridge_Server_authorized_Load":(
        "tools/p37-e4/bridge.go","b.Server.Load(context.Background(),cookie.Value)"),
    "Bridge_Gorilla_authorized_New":(
        "tools/p37-e4/bridge.go","b.Gorilla.New(req,cookieName)"),
}
receipts={}
for name,(file,needle) in checks.items():
    src=(repo_root/file).read_bytes()
    assert needle in src.decode("utf-8"),(name,file,needle)
    receipts[name]={"path":file,"sha256":hashlib.sha256(src).hexdigest(),"observed_callsite":needle}
print(json.dumps({"source_gate":"PASS_SOURCE_CALLSITE_EVIDENCE_ONLY",
                  "type":"P37_E4_AUTHORITY_CAPABILITY_API_EVIDENCE",
                  "facts":receipts,"limitations":[
                      "Not a complete source edit graph",
                      "Research-authored bridge and reader capability model",
                      "Strong classical prior predicts observed compatibility"
                  ]},indent=2,sort_keys=True))
