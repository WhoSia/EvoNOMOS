package sourcealias

import (
 "errors"
 "os"
 "os/exec"
 "path/filepath"
 "strconv"
 "strings"
 "testing"
)

func fixture(shared bool) string {
 header:="package fixture\ntype Cell struct{Value string}\ntype Clients struct{Legacy,Future *Cell}\nfunc Build() Clients{\np:=&Cell{Value:\"stable\"}\n"
 if shared {return header+"return Clients{Legacy:p,Future:p}\n}\n"+writeSource}
 return header+"q:=&Cell{Value:\"stable\"}\nreturn Clients{Legacy:p,Future:q}\n}\n"+writeSource
}
const writeSource="func Write(c Clients){c.Future.Value=\"new\"}\n"

func TestDerivesSharedAliasAndWriteFootprint(t *testing.T){
 shared,e:=Analyze(fixture(true));if e!=nil{t.Fatal(e)}
 disjoint,e:=Analyze(fixture(false));if e!=nil{t.Fatal(e)}
 if !shared.Shared||shared.LegacyAfterWrite!="new"||shared.FutureAfterWrite!="new"{t.Fatal(shared)}
 if disjoint.Shared||disjoint.LegacyAfterWrite!="stable"||disjoint.FutureAfterWrite!="new"{t.Fatal(disjoint)}
 t.Log("SOURCE_DERIVED_ALIAS shared=true legacy_after_write=new disjoint=false legacy_after_write=stable")
}
func TestSourceDerivedAliasMatchesNativeGoRuntime(t *testing.T){
 for _,shared:=range []bool{true,false}{
  src:=fixture(shared);derived,e:=Analyze(src);if e!=nil{t.Fatal(e)}
  dir:=t.TempDir()
  if e:=os.WriteFile(filepath.Join(dir,"go.mod"),[]byte("module fixture\n\ngo 1.23\n"),0644);e!=nil{t.Fatal(e)}
  if e:=os.WriteFile(filepath.Join(dir,"fixture.go"),[]byte(src),0644);e!=nil{t.Fatal(e)}
  test:="package fixture\nimport \"testing\"\nfunc TestActual(t *testing.T){c:=Build();if c.Legacy.Value!=\"stable\"||c.Future.Value!=\"stable\"{t.Fatal(\"bad initial\")};Write(c);if c.Legacy.Value!="+strconv.Quote(derived.LegacyAfterWrite)+"||c.Future.Value!="+strconv.Quote(derived.FutureAfterWrite)+"{t.Fatal(\"static/runtime disagreement\")}}\n"
  if e:=os.WriteFile(filepath.Join(dir,"fixture_test.go"),[]byte(test),0644);e!=nil{t.Fatal(e)}
  cmd:=exec.Command("go","test","-count=1","./...")
  cmd.Dir=dir;cmd.Env=append(os.Environ(),"GOWORK=off")
  output,e:=cmd.CombinedOutput()
  if e!=nil{t.Fatalf("shared=%v source/runtime mismatch: %v\n%s",shared,e,output)}
  t.Logf("NATIVE_SOURCE_ALIAS shared=%v runtime_matches_static=true",shared)
 }
}
func TestRejectUnmodeledSourceEffectsAndCompilerDirectives(t *testing.T){
 original:=fixture(true)
 invalid:=[]string{
  "//go:build ignore\n"+original,
  original+"\nfunc Hidden(c Clients){c.Legacy.Value=\"new\"}\n",
  strings.Replace(original,"c.Future.Value=\"new\"","c.Legacy.Value=\"new\"",1),
  strings.Replace(original,"c.Future.Value=\"new\"","c.Future.Value=\"new\";c.Legacy.Value=\"new\"",1),
  strings.Replace(original,"&Cell{Value:\"stable\"}","&Cell{Value:\"other\"}",1),
  strings.Replace(original,"Legacy:p,Future:p","Legacy:p,Future:unknown",1),
  strings.Replace(original,"return Clients{Legacy:p,Future:p}","return Clients{Legacy:&Cell{Value:\"stable\"},Future:p}",1),
 }
 for i,src:=range invalid {
  if _,e:=Analyze(src);!errors.Is(e,ErrOutsideGrammar){t.Fatalf("unmodeled source case %d accepted: %v",i,e)}
 }
 t.Logf("SOURCE_ESCAPE_CONTROLS rejected=%d",len(invalid))
}
func TestRelativeCostAndClassicalAliasAwareBaseline(t *testing.T){
 a,e:=Analyze(fixture(true));if e!=nil{t.Fatal(e)}
 b,e:=Analyze(fixture(false));if e!=nil{t.Fatal(e)}
 // Editing rights are independently declared, NOT source-extracted.
 cost:=func(r Result)int{if r.Shared{return 2};return 1}
 if cost(a)!=2||cost(b)!=1{t.Fatalf("bounded cost shared=%d disjoint=%d",cost(a),cost(b))}
 t.Log("CLASSICAL_ALIAS_BASELINE shared_safe_cost=2 detached_safe_cost=1 method=exact_two_operation_BFS")
}
