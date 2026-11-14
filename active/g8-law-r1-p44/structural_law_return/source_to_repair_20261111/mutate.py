"""Small exact-source finite Go maintenance grammar, not global repair synthesis."""
from pathlib import Path
import argparse
import subprocess

OPS=("none","constructor","route_both","remove_lookup_lower","match_lower")
PARENTS={
 "constructor":("func NewPattern(value string) Pattern {\n\tp := Pattern{}",
  "func NewPattern(value string) Pattern {\n\tvalue = strings.ToLower(value)\n\tp := Pattern{}"),
 "route_both":("NewPattern(match)", "NewPattern(strings.ToLower(match))"),
 "remove_lookup_lower":("strings.ToLower(r.Header.Get(", "r.Header.Get("),
 "match_lower":(
  "func (p Pattern) Match(v string) bool {\n\tif !p.wildcard {\n\t\treturn p.prefix == v\n\t}\n\treturn len(v) >= len(p.prefix+p.suffix) && strings.HasPrefix(v, p.prefix) && strings.HasSuffix(v, p.suffix)\n}",
  "func (p Pattern) Match(v string) bool {\n\tprefix := strings.ToLower(p.prefix)\n\tsuffix := strings.ToLower(p.suffix)\n\tif !p.wildcard {\n\t\treturn prefix == v\n\t}\n\treturn len(v) >= len(prefix+suffix) && strings.HasPrefix(v, prefix) && strings.HasSuffix(v, suffix)\n}"
 ),
}
def apply(root,op):
    if op not in OPS:raise ValueError("illegal action")
    p=root/"middleware"/"route_headers.go"
    s=p.read_text()
    if op=="none":
        return {"operator":op,"sites":0}
    if op=="route_both":
        # independent RouteAny loop site + direct Route site, not just global name match.
        direct="HeaderRoute{MatchOne: NewPattern(match), Middleware: middlewareHandler}"
        anysite="patterns = append(patterns, NewPattern(m))"
        if s.count(direct)!=1 or s.count(anysite)!=1:raise ValueError("unrecognized production source")
        t=s.replace(direct,"HeaderRoute{MatchOne: NewPattern(strings.ToLower(match)), Middleware: middlewareHandler}").replace(anysite,"patterns = append(patterns, NewPattern(strings.ToLower(m)))")
        sites=2
    else:
        old,new=PARENTS[op]
        expected=1
        if s.count(old)!=expected:raise ValueError("original source shape drift %s %d"%(op,s.count(old)))
        if op=="remove_lookup_lower":
            # preserve the one closing parenthesis of Header.Get(...)
            # source contains strings.ToLower(r.Header.Get(header)), remove outer wrapper only.
            marker="strings.ToLower(r.Header.Get("
            import re
            t,n=re.subn(r"strings\.ToLower\((r\.Header\.Get\([\w.]+\))\)",r"\1",s)
            if n!=1:raise ValueError("unexpected request sites "+str(n))
        else:t=s.replace(old,new,1)
        sites=1
    if t==s:raise ValueError("no-op repair")
    p.write_text(t)
    subprocess.run(["gofmt","-w",str(p)],check=True,cwd=root)
    return {"operator":op,"sites":sites}
if __name__=="__main__":
    cli=argparse.ArgumentParser()
    cli.add_argument("--root",type=Path,required=True)
    cli.add_argument("--operation",choices=OPS,required=True)
    args=cli.parse_args()
    print(apply(args.root,args.operation))
