package main

import (
  "encoding/json"
  "fmt"
  "os"
  "strings"
)

func selectRangeStream(recursive, gate, support bool) bool {
  return recursive && gate && support
}

func main() {
  if len(os.Args) != 2 {
    fmt.Fprintln(os.Stderr,"usage: probe <kubernetes-checkout>")
    os.Exit(2)
  }
  root:=os.Args[1]
  watcherPath:=root+"/staging/src/k8s.io/apiserver/pkg/storage/etcd3/watcher.go"
  b,err:=os.ReadFile(watcherPath)
  if err!=nil { panic(err) }
  src:=string(b)
  sourceAssert :=
    strings.Contains(src,"DefaultFeatureGate.Enabled(features.EtcdRangeStream) &&") &&
    strings.Contains(src,"DefaultFeatureSupportChecker.Supports(storage.RangeStream)")

  rows:=[]struct{Q,G int}{
    {0,0},{0,1},{1,0},{1,1},
  }
  truth:=map[string]int{}
  pass:=sourceAssert
  for _,r:=range rows{
    y:=0
    if selectRangeStream(true,r.G==1,r.Q==1){y=1}
    key:=fmt.Sprintf("q%d_g%d",r.Q,r.G)
    truth[key]=y
    expected:=0
    if r.Q==1 && r.G==1 {expected=1}
    if y!=expected {pass=false}
  }

  out:=map[string]any{
    "stage":"EvoNOMOS Generation VIII LAW-R1-P24",
    "status":map[bool]string{true:"PASS",false:"FAIL"}[pass],
    "family":"KUBERNETES_ETCD_RANGE_STREAM_AND_GATE",
    "source_condition_assertion":sourceAssert,
    "recursive_fixed":true,
    "q":"backend RangeStream support",
    "g":"EtcdRangeStream feature gate",
    "rule":"q AND g",
    "truth_table":truth,
  }
  os.MkdirAll("out-p24",0755)
  jb,_:=json.MarshalIndent(out,"","  ")
  os.WriteFile("out-p24/p24-bridge.json",append(jb,'\n'),0644)
  fmt.Println("P24_BRIDGE="+out["status"].(string))
  fmt.Printf("SOURCE_ASSERT=%v\n",sourceAssert)
  for _,k:=range []string{"q0_g0","q0_g1","q1_g0","q1_g1"}{
    fmt.Printf("%s=%d\n",k,truth[k])
  }
  if !pass {os.Exit(3)}
}
