package cert

import (
 "errors"
 "fmt"
 "os"
 "os/exec"
 "path/filepath"
 "strings"
 "testing"
)

const aSource="package fixture\ntype Left struct { Value string }\nfunc Legacy() string { return \"old\" }\nfunc FutureA() string { p := &Left{Value: \"a0\"}; return p.Value }\n"
const bSource="package fixture\ntype Right struct { Value string }\nfunc FutureB() string { p := &Right{Value: \"b0\"}; return p.Value }\n"
var rights=map[string]bool{"A":true,"B":true}

func write(t *testing.T,a,b string)string{
 t.Helper()
 dir:=t.TempDir()
 for name,src:=range map[string]string{"a.go":a,"b.go":b}{
  if err:=os.WriteFile(filepath.Join(dir,name),[]byte(src),0600);err!=nil{t.Fatal(err)}
 }
 return dir
}
func change(src,old,next string)string{return strings.Replace(src,old,next,1)}
func mustHold(t *testing.T,a,b string){
 t.Helper()
 _,err:=CheckDir(write(t,a,b),rights)
 if !errors.Is(err,ErrHold){t.Fatalf("expected HOLD, got %v",err)}
}
func TestSafeFreshPointer(t *testing.T){
 r,err:=CheckDir(write(t,aSource,bSource),rights)
 if err!=nil||r.Legacy!="old"||r.A!="a0"||r.B!="b0"||len(r.SourceSHA256)!=64||r.Grade!="DIRECTORY_AST_FRESH_POINTER_RIGHTS_UNVERIFIED"{t.Fatal(r,err)}
}
func TestUnsafePointerCasesHOLD(t *testing.T){
 cases:=map[string][2]string{
  "global":{aSource+"var shared = &Left{Value:\"x\"}\n",bSource},
  "pointer-field":{change(aSource,"Value string","Value *string"),bSource},
  "interface-field":{change(aSource,"Value string","Value interface{}"),bSource},
  "function-call":{change(aSource,"return p.Value","return FutureB()"),bSource},
  "cross-type":{change(aSource,"&Left{","&Right{"),bSource},
  "dynamic":{change(aSource,"Value: \"a0\"","Value: FutureB()"),bSource},
  "pointer-escape":{change(aSource,"return p.Value","saved = p; return p.Value"),bSource},
  "local-alias":{change(aSource,"return p.Value","q := p; return q.Value"),bSource},
  "other-variable":{change(aSource,"return p.Value","return q.Value"),bSource},
  "no-address":{change(aSource,"&Left{","Left{"),bSource},
  "import":{change(aSource,"package fixture","package fixture\nimport \"fmt\""),bSource},
  "build-tag":{aSource+"//go:build ignore\n",bSource},
  "extra-func":{aSource+"func init(){}\n",bSource},
  "package":{change(aSource,"package fixture","package unrelated"),bSource},
  "method":{aSource+"func (x *Left) Mutate(){}\n",bSource},
  "raw-string":{change(aSource,"\"a0\"","`a0`"),bSource},
  "extra-statement":{change(aSource,"return p.Value","_ = p; return p.Value"),bSource},
  "cross-b":{aSource,change(bSource,"return p.Value","return FutureA()")},
 }
 for name,v:=range cases{t.Run(name,func(t *testing.T){mustHold(t,v[0],v[1])})}
}
func TestDirectoryAndGrantsHOLD(t *testing.T){
 d:=write(t,aSource,bSource)
 os.WriteFile(filepath.Join(d,"hidden.go"),[]byte("package fixture"),0600)
 if _,err:=CheckDir(d,rights);!errors.Is(err,ErrHold){t.Fatal(err)}
 d2:=write(t,aSource,bSource)
 os.Remove(filepath.Join(d2,"a.go"))
 if err:=os.Symlink(filepath.Join(d2,"b.go"),filepath.Join(d2,"a.go"));err==nil{
  if _,e:=CheckDir(d2,rights);!errors.Is(e,ErrHold){t.Fatal(e)}
 }
 if _,e:=CheckDir(write(t,aSource,bSource),map[string]bool{"A":true});!errors.Is(e,ErrHold){t.Fatal(e)}
}
func TestTwoOrderSourceEditWitnesses(t *testing.T){
 aa:=change(aSource,"\"a0\"","\"new\"")
 bb:=change(bSource,"\"b0\"","\"new\"")
 start:=write(t,aSource,bSource)
 afterA:=write(t,aa,bSource)
 afterB:=write(t,aSource,bb)
 end:=write(t,aa,bb)
 for _,v:=range []struct{before,after,port string}{{start,afterA,"A"},{afterA,end,"B"},{start,afterB,"B"},{afterB,end,"A"}}{
  receipt,err:=CheckEdit(v.before,v.after,v.port,rights)
  if err!=nil||receipt.Cost!=1||receipt.Before.SourceSHA256==receipt.After.SourceSHA256{t.Fatal(receipt,err)}
 }
 r,err:=CheckDir(end,rights)
 if err!=nil||r.A!="new"||r.B!="new"||r.Legacy!="old"{t.Fatal(r,err)}
}
func TestCrossFileOrNonliteralEditHOLD(t *testing.T){
 start:=write(t,aSource,bSource)
 both:=write(t,change(aSource,"\"a0\"","\"new\""),change(bSource,"\"b0\"","\"new\""))
 whitespace:=write(t,change(change(aSource,"\"a0\"","\"new\""),"package fixture","package  fixture"),bSource)
 for _,v:=range []struct{dir,port string}{{both,"A"},{whitespace,"A"},{start,"A"},{both,"unknown"}}{
  if _,e:=CheckEdit(start,v.dir,v.port,rights);!errors.Is(e,ErrHold){t.Fatal(e)}
 }
}
func native(t *testing.T,dir string,a,b string,alias bool){
 t.Helper()
 var src string
 if alias{
  src="package fixture\nimport \"testing\"\nfunc TestObservedAlias(t *testing.T) { if Legacy()!=\"old\"||FutureA()!=\"a0\"{t.Fatal(\"old contract\")}; if FutureB()!=\"new\"||FutureA()!=\"new\"||Legacy()!=\"old\"{t.Fatal(\"alias not observed\")} }\n"
 }else{
  src=fmt.Sprintf("package fixture\nimport \"testing\"\nfunc TestClient(t *testing.T){if Legacy()!=\"old\"||FutureA()!=%q||FutureB()!=%q{t.Fatal(\"client\")}}\n",a,b)
 }
 if e:=os.WriteFile(filepath.Join(dir,"client_test.go"),[]byte(src),0600);e!=nil{t.Fatal(e)}
 cmd:=exec.Command("go","test","-count=1","./...")
 cmd.Dir=dir;cmd.Env=append(os.Environ(),"GO111MODULE=off")
 out,e:=cmd.CombinedOutput();if e!=nil{t.Fatalf("native Go error %v\n%s",e,out)}
}
func TestFourNativeFreshPointerVariants(t *testing.T){
 for _,a:=range []string{"a0","new"}{for _,b:=range []string{"b0","new"}{
  t.Run(a+"_"+b,func(t *testing.T){
   dir:=write(t,change(aSource,"\"a0\"",fmt.Sprintf("%q",a)),change(bSource,"\"b0\"",fmt.Sprintf("%q",b)))
   if _,e:=CheckDir(dir,rights);e!=nil{t.Fatal(e)}
   native(t,dir,a,b,false)
  })
 }}
}
func TestSharedPointerCounterexampleInRealGo(t *testing.T){
 a:="package fixture\ntype Left struct {Value string}\nvar shared = &Left{Value:\"a0\"}\nfunc Legacy() string{return \"old\"}\nfunc FutureA() string{return shared.Value}\n"
 b:="package fixture\ntype Right struct{Value string}\nfunc FutureB() string{shared.Value=\"new\";return shared.Value}\n"
 mustHold(t,a,b)
 native(t,write(t,a,b),"","",true)
}
