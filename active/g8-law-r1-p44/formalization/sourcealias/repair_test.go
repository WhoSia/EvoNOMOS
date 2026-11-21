package sourcealias

import (
 "os"
 "os/exec"
 "path/filepath"
 "strings"
 "testing"
)

func TestActualASTSourceRepairMakesSharedFutureEditSafe(t *testing.T){
 before:=fixture(true)
 original,err:=Analyze(before);if err!=nil||!original.Shared||original.LegacyAfterWrite!="new"{t.Fatal(original,err)}
 repaired,err:=DetachFutureSource(before);if err!=nil{t.Fatal(err)}
 if repaired==before||!strings.Contains(repaired,"Future: q"){t.Fatal("actual Go AST source patch not produced")}
 after,err:=Analyze(repaired)
 if err!=nil||after.Shared||after.LegacyAfterWrite!="stable"||after.FutureAfterWrite!="new"{t.Fatal(after,err)}
 if count,err:=SafeSourcePatchCost(before);err!=nil||count!=1{t.Fatal(count,err)}
 if count,err:=SafeSourcePatchCost(repaired);err!=nil||count!=0{t.Fatal(count,err)}
 t.Log("GO_SOURCE_PATCH before_alias=true after_alias=false source_patch_cost=1 runtime_write_not_counted=true")
 dir:=t.TempDir()
 if err:=os.WriteFile(filepath.Join(dir,"go.mod"),[]byte("module fixture\n\ngo 1.23\n"),0644);err!=nil{t.Fatal(err)}
 if err:=os.WriteFile(filepath.Join(dir,"fixture.go"),[]byte(repaired),0644);err!=nil{t.Fatal(err)}
 test:="package fixture\nimport \"testing\"\nfunc TestRepairedNative(t *testing.T){c:=Build();Write(c);if c.Legacy.Value!=\"stable\"||c.Future.Value!=\"new\"{t.Fatal(\"regression\")}}\n"
 if err:=os.WriteFile(filepath.Join(dir,"fixture_test.go"),[]byte(test),0644);err!=nil{t.Fatal(err)}
 cmd:=exec.Command("go","test","-count=1","./...")
 cmd.Dir=dir;cmd.Env=append(os.Environ(),"GOWORK=off")
 output,err:=cmd.CombinedOutput()
 if err!=nil{t.Fatalf("generated source patch failed to compile and run: %v\n%s",err,output)}
 t.Log("NATIVE_REPAIRED_GO_SOURCE legacy_contract=true future_requirement=true")
}
func TestNoOpWhenAlreadyDisjointAndRejectOutOfScopeRepair(t *testing.T){
 already:=fixture(false)
 modified,err:=DetachFutureSource(already)
 if err!=nil||modified!=already{t.Fatal(err)}
 source:="//go:build ignore\n"+fixture(true)
 if _,err:=DetachFutureSource(source);err==nil{t.Fatal("out-of-grammar source patch allowed")}
}
