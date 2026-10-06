package main

import (
  "encoding/json"
  "fmt"
  "os"
  "os/exec"
  "path/filepath"
  "strings"
)

type Row struct {
  Name string
  Intervention string
  Target string
  Q int
  G int
  Y int
  CfgHasAtomicPtr bool
  CompileOK bool
}

func run(dir string, args ...string) (bool,string) {
  cmd:=exec.Command(args[0],args[1:]...)
  cmd.Dir=dir
  b,err:=cmd.CombinedOutput()
  return err==nil,string(b)
}

func writeProbe(dir, dep, target string, q,g int) (Row,error) {
  if err:=os.RemoveAll(dir);err!=nil{return Row{},err}
  if err:=os.MkdirAll(filepath.Join(dir,"src"),0755);err!=nil{return Row{},err}
  features:=""
  if g==1 { features=", features = [\"alloc\"]" }
  cargo:=fmt.Sprintf("[package]\nname=\"p27_bevy_probe\"\nversion=\"0.0.0\"\nedition=\"2021\"\n\n[lib]\npath=\"src/lib.rs\"\n\n[dependencies]\nbevy_platform={path=%q,default-features=false%s}\n",filepath.ToSlash(dep),features)
  expected:=q*g
  source:=fmt.Sprintf("#![no_std]\nconst Y: bool = bevy_platform::cfg::arc!();\nconst EXPECTED: bool = %v;\nconst _: () = assert!(Y == EXPECTED);\npub fn p27_native_arc_backend() -> bool { Y }\n", expected==1)
  if err:=os.WriteFile(filepath.Join(dir,"Cargo.toml"),[]byte(cargo),0644);err!=nil{return Row{},err}
  if err:=os.WriteFile(filepath.Join(dir,"src","lib.rs"),[]byte(source),0644);err!=nil{return Row{},err}

  cfg:=exec.Command("rustc","--print","cfg","--target",target)
  cfgOut,err:=cfg.CombinedOutput()
  if err!=nil{return Row{},fmt.Errorf("rustc cfg: %v %s",err,cfgOut)}
  atomic:=strings.Contains(string(cfgOut),`target_has_atomic="ptr"`)
  ok,out:=run(dir,"cargo","check","--quiet","--target",target)
  if !ok{return Row{},fmt.Errorf("probe %s failed: %s",filepath.Base(dir),out)}
  return Row{Target:target,Q:q,G:g,Y:expected,CfgHasAtomicPtr:atomic,CompileOK:ok},nil
}

func main(){
  dep:=os.Getenv("P27_BEVY_PLATFORM")
  if dep=="" { dep="out-p27/bevy/crates/bevy_platform" }
  abs,err:=filepath.Abs(dep);if err!=nil{panic(err)}
  base:="out-p27/bevy-probes"
  cells:=[]struct{name,intervention,target string;q,g int}{
    {"BASELINE_111","baseline","x86_64-unknown-linux-gnu",1,1},
    {"UPSTREAM_DROP","drop","thumbv6m-none-eabi",0,1},
    {"UPSTREAM_RESTORE","restore","x86_64-unknown-linux-gnu",1,1},
    {"LOCAL_GATE_DROP","gate_drop","x86_64-unknown-linux-gnu",1,0},
  }
  rows:=make([]Row,0,len(cells))
  pass:=true
  for _,c:=range cells{
    r,err:=writeProbe(filepath.Join(base,c.name),abs,c.target,c.q,c.g)
    if err!=nil{fmt.Fprintln(os.Stderr,err);os.Exit(2)}
    r.Name=c.name;r.Intervention=c.intervention
    if r.CfgHasAtomicPtr!=(c.q==1){pass=false}
    if r.Y != c.q*c.g {pass=false}
    rows=append(rows,r)
  }
  payload:=map[string]any{
    "stage":"EvoNOMOS Generation VIII LAW-R1-P27",
    "mechanism":"BEVY_NATIVE_ARC_BACKEND_GATE",
    "rival":"N0_LAYER_INDEPENDENT_MEDIATION",
    "upstream_commit":"6c21ef6884886f32a1bbd3da84522ba42c5f3ddf",
    "status":map[bool]string{true:"PASS",false:"FAIL"}[pass],
    "rows":rows,
    "drop_delta":[]int{-1,0,-1},
    "restore_delta":[]int{1,0,1},
    "gate_drop_delta":[]int{0,-1,-1},
  }
  os.MkdirAll("out-p27",0755)
  b,_:=json.MarshalIndent(payload,"","  ")
  os.WriteFile("out-p27/p27-bevy.json",b,0644)
  fmt.Println("P27_BEVY="+payload["status"].(string))
  for _,r:=range rows{fmt.Printf("%s q=%d g=%d y=%d atomic=%v\n",r.Name,r.Q,r.G,r.Y,r.CfgHasAtomicPtr)}
  if !pass{os.Exit(3)}
}
