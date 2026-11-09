package closure

import (
 "errors"
 "os"
 "path/filepath"
 "strings"
 "testing"
)

const sourceA="package fixture\ntype Left struct { Value string }\nfunc Legacy() string {return \"old\"}\nfunc FutureA() string {p := &Left{Value: \"a0\"}; return p.Value}\n"
const sourceB="package fixture\ntype Right struct { Value string }\nfunc FutureB() string {p := &Right{Value: \"b0\"}; return p.Value}\n"
var grants=map[string]bool{"A":true,"B":true}
func setup(t *testing.T)string{
 t.Helper()
 dir:=t.TempDir()
 for name,src:=range map[string]string{"go.mod":ModuleText,"a.go":sourceA,"b.go":sourceB}{
  if err:=os.WriteFile(filepath.Join(dir,name),[]byte(src),0600);err!=nil{t.Fatal(err)}
 }
 return dir
}
func modify(t *testing.T,dir,name,src string){
 t.Helper();if err:=os.WriteFile(filepath.Join(dir,name),[]byte(src),0600);err!=nil{t.Fatal(err)}
}
func expectHold(t *testing.T,dir string){
 t.Helper();if _,e:=Check(dir,grants);!errors.Is(e,ErrHold){t.Fatalf("expected HOLD, got %v",e)}
}
func TestPositiveFrozenGoBuild(t *testing.T){
 r,e:=Check(setup(t),grants)
 if e!=nil||r.Grade!=Grade||r.Legacy!="old"||r.A!="a0"||r.B!="b0"||
   len(r.FrozenSHA256)!=64||len(r.ASTSourceSHA256)!=64||len(r.CompilerGoFiles)!=2{
  t.Fatal(r,e)
 }
 if !strings.Contains(r.RightsEvidence,"no independent owner"){t.Fatal("overclaimed authenticated rights")}
}
func TestAdditionalBuildFilesHOLD(t *testing.T){
 files:=[]struct{name,content string;directory bool}{
  {"excluded.go","//go:build never\npackage fixture\n",false},
  {"hidden_test.go","package fixture\n",false},
  {"native.c","int foo(){return 0;}",false},
  {"go.work","go 1.23\n",false},
  {"go.sum","",false},
  {".hidden","",false},
  {"README.md","",false},
  {"subdir","",true},
 }
 for _,f:=range files{t.Run(f.name,func(t *testing.T){
  dir:=setup(t)
  if f.directory{if e:=os.Mkdir(filepath.Join(dir,f.name),0700);e!=nil{t.Fatal(e)}
  }else{modify(t,dir,f.name,f.content)}
  expectHold(t,dir)
 })}
}
func TestModuleDriftHOLD(t *testing.T){
 mods:=[]string{
  "module evil.example\n\ngo 1.23\n",
  "module example.com/evonomos-f31-closed\n\ngo 1.24\n",
  ModuleText+"require evil.example/v v1.0.0\n",
 }
 for i,v:=range mods{
  t.Run(string(rune('A'+i)),func(t *testing.T){dir:=setup(t);modify(t,dir,"go.mod",v);expectHold(t,dir)})
 }
}
func TestSymlinkRefused(t *testing.T){
 dir:=setup(t)
 if e:=os.Remove(filepath.Join(dir,"a.go"));e!=nil{t.Fatal(e)}
 other:=filepath.Join(t.TempDir(),"source.go")
 if e:=os.WriteFile(other,[]byte(sourceA),0600);e!=nil{t.Fatal(e)}
 if e:=os.Symlink(other,filepath.Join(dir,"a.go"));e!=nil{t.Skip(e)}
 expectHold(t,dir)
}
func TestExtraGlobalAndCrossCallHOLD(t *testing.T){
 for _,s:=range []string{
  sourceA+"var shared=&Left{Value:\"unsafe\"}\n",
  strings.Replace(sourceA,"return p.Value","return FutureB()",1),
 }{
  dir:=setup(t);modify(t,dir,"a.go",s);expectHold(t,dir)
 }
}
func TestUnverifiedGrantHOLD(t *testing.T){
 if _,e:=Check(setup(t),map[string]bool{"A":true});!errors.Is(e,ErrHold){t.Fatal(e)}
}
func TestFrozenSHAChangesWithLiteral(t *testing.T){
 old,e:=Check(setup(t),grants);if e!=nil{t.Fatal(e)}
 dir:=setup(t);modify(t,dir,"a.go",strings.Replace(sourceA,"\"a0\"","\"new\"",1))
 next,e:=Check(dir,grants);if e!=nil{t.Fatal(e)}
 if old.FrozenSHA256==next.FrozenSHA256||old.ASTSourceSHA256==next.ASTSourceSHA256||
   next.A!="new"||next.B!="b0"{t.Fatal("source change not bound")}
}
