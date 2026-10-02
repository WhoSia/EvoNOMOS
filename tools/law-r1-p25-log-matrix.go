package main

import (
	"encoding/json"
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
)

type Cell struct {
	Name string `json:"name"`
	Target string `json:"target"`
	Q int `json:"q"`
	G int `json:"g"`
	ControlOK bool `json:"control_ok"`
	ProbeOK bool `json:"probe_ok"`
	Y int `json:"y"`
	CfgHasAtomicPtr bool `json:"cfg_has_atomic_ptr"`
	ProbeErrorContainsMissingItem bool `json:"probe_error_contains_missing_item"`
}

func run(dir string, args ...string) (bool,string) {
	cmd:=exec.Command(args[0],args[1:]...)
	cmd.Dir=dir
	b,err:=cmd.CombinedOutput()
	return err==nil,string(b)
}

func writeCase(root, name, target string, q,g int, upstream string) (Cell,error) {
	dir:=filepath.Join(root,name)
	if err:=os.MkdirAll(filepath.Join(dir,"src"),0755);err!=nil{return Cell{},err}
	features:=""
	if g==1 { features=", features = [\"alloc\"]" }
	toml:=fmt.Sprintf("[package]\nname=\"p25_%s\"\nversion=\"0.0.0\"\nedition=\"2021\"\n\n[dependencies]\nlog = { path = %q, default-features = false%s }\n",strings.ToLower(name),upstream,features)
	if err:=os.WriteFile(filepath.Join(dir,"Cargo.toml"),[]byte(toml),0644);err!=nil{return Cell{},err}

	cfgCmd:=exec.Command("rustc","--print","cfg","--target",target)
	cfgBytes,err:=cfgCmd.CombinedOutput()
	if err!=nil{return Cell{},fmt.Errorf("rustc cfg %s: %v: %s",target,err,cfgBytes)}
	hasAtomic:=strings.Contains(string(cfgBytes),`target_has_atomic="ptr"`)

	control:=`#![no_std]
pub fn level() -> log::Level { log::Level::Info }
`
	if err:=os.WriteFile(filepath.Join(dir,"src","lib.rs"),[]byte(control),0644);err!=nil{return Cell{},err}
	controlOK,controlOut:=run(dir,"cargo","check","--quiet","--target",target)
	if !controlOK {
		return Cell{},fmt.Errorf("control failed %s: %s",name,controlOut)
	}

	probe:=`#![no_std]
pub use log::set_boxed_logger;
`
	if err:=os.WriteFile(filepath.Join(dir,"src","lib.rs"),[]byte(probe),0644);err!=nil{return Cell{},err}
	probeOK,probeOut:=run(dir,"cargo","check","--target",target)
	missing:=strings.Contains(probeOut,"set_boxed_logger") && (strings.Contains(probeOut,"no `set_boxed_logger`") || strings.Contains(probeOut,"unresolved import"))
	y:=0
	if probeOK { y=1 }
	return Cell{Name:name,Target:target,Q:q,G:g,ControlOK:controlOK,ProbeOK:probeOK,Y:y,CfgHasAtomicPtr:hasAtomic,ProbeErrorContainsMissingItem:missing},nil
}

func main(){
	root:="out-p25"
	upstream,err:=filepath.Abs(filepath.Join(root,"log-upstream"))
	if err!=nil{panic(err)}
	cases:=[]struct{name,target string;q,g int}{
		{"Q0_G0","thumbv6m-none-eabi",0,0},
		{"Q0_G1","thumbv6m-none-eabi",0,1},
		{"Q1_G0","x86_64-unknown-linux-gnu",1,0},
		{"Q1_G1","x86_64-unknown-linux-gnu",1,1},
	}
	var cells []Cell
	pass:=true
	for _,c:=range cases{
		cell,err:=writeCase(root,c.name,c.target,c.q,c.g,upstream)
		if err!=nil{fmt.Fprintln(os.Stderr,err);os.Exit(2)}
		if cell.CfgHasAtomicPtr != (c.q==1) { pass=false }
		expected:=0
		if c.q==1 && c.g==1 {expected=1}
		if cell.Y!=expected {pass=false}
		if !cell.ProbeOK && !cell.ProbeErrorContainsMissingItem { pass=false }
		cells=append(cells,cell)
	}
	payload:=map[string]any{
		"stage":"EvoNOMOS Generation VIII LAW-R1-P25",
		"family":"RUST_LOG_BOXED_LOGGER_CAPABILITY_GATE",
		"upstream_commit":"27e3cf7a021dab43430a70cb2909c06ca8141f79",
		"status":map[bool]string{true:"PASS",false:"FAIL"}[pass],
		"cells":cells,
		"truth_table":[]int{cells[0].Y,cells[1].Y,cells[2].Y,cells[3].Y},
	}
	b,_:=json.MarshalIndent(payload,"","  ")
	os.WriteFile(filepath.Join(root,"p25-rust-log.json"),append(b,'\n'),0644)
	fmt.Println("P25_RUST_LOG="+payload["status"].(string))
	for _,c:=range cells{fmt.Printf("%s=%d control=%v atomic_ptr=%v\n",c.Name,c.Y,c.ControlOK,c.CfgHasAtomicPtr)}
	if !pass {os.Exit(3)}
}
