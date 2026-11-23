"""An exact one-location classical source repair to BOTH pre-existing P35-P7 arms.

Only runs on disposable original Chi source checkouts, not upstream.
"""
from pathlib import Path
import argparse
import subprocess

BEFORE="""func NewPattern(value string) Pattern {
\tp := Pattern{}
"""
AFTER="""func NewPattern(value string) Pattern {
\t// Header values are normalized at lookup; normalize patterns consistently.
\tvalue = strings.ToLower(value)
\tp := Pattern{}
"""

def apply(root:Path):
    path=root/"middleware"/"route_headers.go"
    src=path.read_text()
    assert src.count(BEFORE)==1, "source arm unexpected"
    assert "value = strings.ToLower(value)" not in src, "already modified"
    path.write_text(src.replace(BEFORE,AFTER,1))
    subprocess.run(["gofmt","-w",str(path)],cwd=root,check=True)
    diff=subprocess.check_output(["git","diff","--","middleware/route_headers.go"],cwd=root,text=True)
    assert "value = strings.ToLower(value)" in diff
    print("EVO1247_REPAIR_COMMON NewPattern lowercase input; original code remains ephemeral")
if __name__=="__main__":
    cli=argparse.ArgumentParser()
    cli.add_argument("--root",required=True,type=Path)
    apply(cli.parse_args().root)
