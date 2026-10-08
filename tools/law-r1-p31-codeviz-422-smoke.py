#!/usr/bin/env python3
"""Codeviz #422 bounded registry/load smoke across historical BUNDLED/SPLIT Go APIs.
This does not claim complete git-provider E2E coverage.
"""
from pathlib import Path
import argparse,subprocess,json

OLD=r'''package provider
import (
 "testing"
 "github.com/bevan/code-visualizer/internal/metric"
 "github.com/bevan/code-visualizer/internal/model"
 "github.com/bevan/code-visualizer/internal/palette"
)
type p31BundledProbe struct { calls int }
func (*p31BundledProbe) Name() metric.Name {return metric.Name("p31-probe")}
func (*p31BundledProbe) Kind() metric.Kind {return metric.Quantity}
func (*p31BundledProbe) Description() string{return "test"}
func (*p31BundledProbe) Dependencies() []metric.Name{return nil}
func (*p31BundledProbe) DefaultPalette() palette.PaletteName{return palette.Neutral}
func (p *p31BundledProbe) Load(_ *model.Directory) error {p.calls++;return nil}
func TestP31ProviderRegistryExecutionWithoutRendering(t *testing.T){
 reg:=newRegistry()
 p:=&p31BundledProbe{}
 reg.register(p)
 got,ok:=reg.get("p31-probe")
 if !ok||got==nil {t.Fatal("registry lookup failed")}
 if err:=got.Load(nil);err!=nil{t.Fatal(err)}
 if p.calls!=1 {t.Fatalf("loader calls=%d",p.calls)}
}
'''
NEW=r'''package provider
import (
 "testing"
 "github.com/bevan/code-visualizer/internal/metric"
 "github.com/bevan/code-visualizer/internal/model"
)
type p31SplitProbe struct {calls int}
func (p *p31SplitProbe) Load(_ *model.Directory) error{p.calls++;return nil}
func TestP31ProviderRegistryExecutionWithoutRendering(t *testing.T){
 reg:=newRegistry()
 p:=&p31SplitProbe{}
 reg.register(MetricDescriptor{Name:metric.Name("p31-probe"),Kind:metric.Quantity},p)
 desc,ok:=reg.get("p31-probe")
 if !ok||desc.Name!="p31-probe"{t.Fatal("descriptor lookup failed")}
 loader,ok:=reg.getLoader("p31-probe")
 if !ok||loader==nil{t.Fatal("loader lookup failed")}
 if err:=loader.Load(nil);err!=nil{t.Fatal(err)}
 if p.calls!=1{t.Fatalf("loader calls=%d",p.calls)}
}
'''
def write(tree,code):
 file=Path(tree)/"internal/provider/p31_registry_execution_test.go"
 if file.exists():raise RuntimeError("Existing P31 file")
 file.write_text(code)
 subprocess.run(["gofmt","-w",str(file)],check=True)
 return {"file":str(file),"lines":len(file.read_text().splitlines())}
def main():
 parser=argparse.ArgumentParser()
 parser.add_argument("--before",required=True);parser.add_argument("--after",required=True)
 a=parser.parse_args()
 print(json.dumps({"stage":"P31","requirement":"codeviz #422 provider execution only smoke subset","before":write(a.before,OLD),"after":write(a.after,NEW),"full_issue_422_completed":False}))
if __name__=="__main__":main()
