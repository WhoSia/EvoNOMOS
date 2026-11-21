"""Adversarial source counterexample: unchanged direct functions can read global state.

A file-level unrelated edit of a global's writer can change the direct client,
so an unchanged-function checksum ALONE is not sound. The restricted AST guard
must refuse to certify preservation when it sees the unexpected global read.
"""
from pathlib import Path
import json
import subprocess
import tempfile
import argparse

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--baseline",required=True,type=Path)
    p.add_argument("--analyzer",required=True,type=Path)
    a=p.parse_args()
    original=a.baseline.read_text()
    assert "if !p.wildcard {" in original
    assert "return HeaderRouter{}" in original
    altered=original.replace("if !p.wildcard {","if !p.wildcard && sharedGate {",1)
    assert "import (\n" in altered
    marker=")\n\n// RouteHeaders"
    assert marker in altered
    altered=altered.replace(marker,")\n\nvar sharedGate = true\n\n// RouteHeaders",1)
    after=altered.replace("return HeaderRouter{}","sharedGate = false\n\treturn HeaderRouter{}",1)
    with tempfile.TemporaryDirectory(prefix="evo_unsafe_global_") as folder:
        base=Path(folder)/"before.go";next=Path(folder)/"after.go"
        base.write_text(altered);next.write_text(after)
        result=subprocess.run([str(a.analyzer),"--before",str(base),"--after",str(next)],
                              capture_output=True,text=True,check=True)
        v=json.loads(result.stdout)
        assert "NewPattern" not in v["changed_functions"]
        assert "Pattern.Match" not in v["changed_functions"]
        assert "RouteHeaders" in v["changed_functions"]
        assert not v["direct_declared_calls_purity_approved"]
        assert not v["direct_microclient_definitely_preserved"]
        assert v["direct_microclient_may_affect"]
        assert any("unapproved direct declaration" in s for s in v["warnings"])
        print("ADVERSARIAL_HIDDEN_GLOBAL_PASS", v["changed_functions"],
              "fail_closed_preserved",v["direct_microclient_definitely_preserved"])
if __name__=="__main__":main()
