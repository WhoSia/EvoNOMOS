"""P40-P1 original Go source-revision court; no external modules or maintainer claims.
16 actual go test variants: 2 architectures x 2 protected-old-client cases x 2^2 edits.
"""
from __future__ import annotations
import concurrent.futures
import os
from pathlib import Path
import subprocess
import tempfile


def fixture(arch, protected, contract, method):
    port="type Port interface { Run() int"
    if contract and arch=="coupled":
        port+="; Next() int"
    port+=" }\n"
    extension="type Advanced interface { Port; Next() int }\n" if contract and arch=="split" else ""
    new_method="func (Fast) Next() int {return 42}\n" if method else ""
    freeze_old="var _ Port=Legacy{}\n" if protected else ""
    final=""
    new_test=""
    if contract and method:
        typ="Advanced" if arch=="split" else "Port"
        final=f"var _ {typ}=Fast{{}}\n"
        new_test=(f'func TestNew(t *testing.T) {{ var p {typ}=Fast{{}};'
                  'if p.Next()!=42 {t.Fatal("new capability")} }\n')
    source=("package specimen\n"+port+extension+
            "type Fast struct{}\nfunc (Fast) Run() int {return 7}\n"
            "type Legacy struct{}\nfunc (Legacy) Run() int {return 9}\n"+
            new_method+"func Old(p Port) int {return p.Run()}\n"
            "var _ Port=Fast{}\n"+freeze_old+final)
    legacy='if Old(Legacy{})!=9 {t.Fatal("legacy old contract")}' if protected else ""
    tests=('package specimen\nimport "testing"\n'
           'func TestOld(t *testing.T) {if Old(Fast{})!=7 {t.Fatal("fast old contract")};'+
           legacy+'}\n'+new_test)
    return source,tests


def test_one(spec):
    arch, protected, contract, method=spec
    with tempfile.TemporaryDirectory(prefix="evonomos-p40-") as tmp:
        folder=Path(tmp)
        src,tst=fixture(*spec)
        (folder/"go.mod").write_text("module example.org/evonomos/p40-court\n\ngo 1.22\n")
        (folder/"specimen.go").write_text(src)
        (folder/"specimen_test.go").write_text(tst)
        env=dict(os.environ,GOWORK="off",GOPROXY="off",GOSUMDB="off")
        proc=subprocess.run(["go","test","-count=1","./..."],cwd=folder,
                            env=env,text=True,capture_output=True,timeout=100)
        return spec,proc.returncode==0,(proc.stdout+proc.stderr)[:1200]


def main():
    specs=[(a,p,c,m) for a in ("coupled","split")
           for p in (False,True) for c in (False,True) for m in (False,True)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        cases=list(pool.map(test_one,specs))
    for arch in ("coupled","split"):
        for protected in (False,True):
            rows=[(c,m,ok,diag) for (a,p,c,m),ok,diag in cases
                  if a==arch and p==protected]
            states={(int(c),int(m)):ok for c,m,ok,_ in rows}
            expected=({(0,0):True,(0,1):True,(1,0):False,(1,1):False}
                      if arch=="coupled" and protected else
                      {(0,0):True,(0,1):True,(1,0):False,(1,1):True}
                      if arch=="coupled" else
                      {(0,0):True,(0,1):True,(1,0):True,(1,1):True})
            assert states==expected,(arch,protected,rows)
            count=(int(states[(0,1)])+int(states[(1,0)])) if states[(1,1)] else 0
            assert count==(0 if arch=="coupled" and protected else
                           1 if arch=="coupled" else 2)
            print(f"P40_GO_SOURCE_COURT arch={arch} protected={int(protected)} "
                  f"safe_orders={count} grid={states} PASS")
    invalid=[diag for _,ok,diag in cases if not ok]
    assert len(invalid)==3
    assert all("does not implement Port" in d or
               "missing method Next" in d for d in invalid),invalid
    print("P40_GO_TYPED_16_REVISION_MATRIX_PASS")
    print("P40_CLASSICAL_GO_METHOD_SET_AND_MENGER_COURT_NO_NOVEL_LAW_CLAIM")


if __name__=="__main__":
    main()
