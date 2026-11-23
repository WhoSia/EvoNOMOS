"""Apply one research-owned, narrowly scoped real original-source repair.

Only intended to operate on ephemeral external original Chi v5.1.0 copy.
No upstream change, no code agent, no long-term architecture claim.
"""
import argparse
from pathlib import Path
import subprocess

BEFORE = """\t\t\t\tif ntyp == ntRegexp && xn.rex != nil {
\t\t\t\t\tif !xn.rex.MatchString(xsearch[:p]) {
\t\t\t\t\t\tcontinue
\t\t\t\t\t}
\t\t\t\t} else if strings.IndexByte(xsearch[:p], '/') != -1 {
\t\t\t\t\t// avoid a match across path segments
\t\t\t\t\tcontinue
\t\t\t\t}
"""
GUARD = """\t\t\t\t// A route parameter must not cross a path segment.
\t\t\t\tif strings.IndexByte(xsearch[:p], '/') != -1 {
\t\t\t\t\tcontinue
\t\t\t\t}
\t\t\t\tif ntyp == ntRegexp && xn.rex != nil {
\t\t\t\t\tif !xn.rex.MatchString(xsearch[:p]) {
\t\t\t\t\t\tcontinue
\t\t\t\t\t}
\t\t\t\t}
"""
HELPER = """\t\t\t\t// A route parameter must not cross a path segment.
\t\t\t\tif !validSingleSegment(xsearch[:p]) {
\t\t\t\t\tcontinue
\t\t\t\t}
\t\t\t\tif ntyp == ntRegexp && xn.rex != nil {
\t\t\t\t\tif !xn.rex.MatchString(xsearch[:p]) {
\t\t\t\t\t\tcontinue
\t\t\t\t\t}
\t\t\t\t}
"""
HELPER_FUNC = """// validSingleSegment restricts a parameter to one URL path segment.
func validSingleSegment(s string) bool {
\treturn strings.IndexByte(s, '/') == -1
}

"""
ANCHOR = "// Recursive edge traversal by checking all nodeTyp groups along the way."

def apply(root:Path,arm:str):
    path=root/"tree.go"
    text=path.read_text()
    assert text.count(BEFORE)==1, "Original source changed, abort"
    if arm=="inline": changed=text.replace(BEFORE,GUARD,1)
    else:
        assert arm=="helper" and text.count(ANCHOR)==1
        changed=text.replace(BEFORE,HELPER,1).replace(ANCHOR,HELPER_FUNC+ANCHOR,1)
    assert changed!=text
    path.write_text(changed)
    subprocess.run(["gofmt","-w","tree.go"],cwd=root,check=True)
    changedfiles=subprocess.check_output(["git","diff","--name-only"],cwd=root,text=True).splitlines()
    assert changedfiles==["tree.go"],f"Unexpected modified upstream source: {changedfiles}"
    print("EVO1188_ARM",arm,"MODIFIED_SOURCE_FILES",changedfiles,"ADDED_HELPER",arm=="helper")
if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--root",type=Path,required=True)
    ap.add_argument("--arm",choices=("inline","helper"),required=True)
    opts=ap.parse_args()
    apply(opts.root,opts.arm)
