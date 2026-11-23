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

func f19pair(shared bool, aux string)SourcePair{
 return SourcePair{Core:fixture(shared),Auxiliary:"package fixture\nfunc Aux() string {return "+aux+"}\n"}
}
func TestF19RealSourceChangeRetainsSliceWhileFromScratchAgrees(t *testing.T){
 base:=f19pair(true,`"old"`)
 cert,seal,err:=IssueSlice(base);if err!=nil{t.Fatal(err)}
 for _,v:=range []string{`"new"`,`"alternative"`,`"other"`}{
  changed:=f19pair(true,v)
  verdict,err:=VerifySlice(changed,cert,seal)
  if err!=nil||verdict!=SliceReused{t.Fatalf("changed auxiliary %s not reusable: %s %v",v,verdict,err)}
  classical,err:=ClassicalFullSliceReanalysis(changed)
  if err!=nil||classical.Shared!=cert.Shared||classical.LegacyAfterWrite!=cert.LegacyAfterWrite{t.Fatal(classical,err)}
  classicCache,err:=ClassicalDependencyCache(changed,cert.CoreTokenDigest)
  if err!=nil||!classicCache{t.Fatalf("equal information rival could not reuse: %v",err)}
  t.Logf("F19_CHANGED_AUX real_source_changed=true value=%s slice_reused=true classical_cache_reused=true",v)
 }
}
func TestF19CoreAliasEditInvalidates(t *testing.T){
 cert,seal,err:=IssueSlice(f19pair(true,`"x"`));if err!=nil{t.Fatal(err)}
 next:=f19pair(false,`"y"`)
 status,err:=VerifySlice(next,cert,seal)
 if err!=nil||status!=SliceInvalid{t.Fatalf("cross-footprint change accepted %s %v",status,err)}
 ground,err:=ClassicalFullSliceReanalysis(next)
 if err!=nil||ground.Shared||ground.LegacyAfterWrite!="stable"{t.Fatal(ground,err)}
 t.Log("F19_CORE_DEPENDENCY_CHANGE correctly_invalidated=true")
}
func TestF19HiddenInitializerAndCrossFileEscapeRejected(t *testing.T){
 base:=f19pair(true,`"x"`);cert,seal,err:=IssueSlice(base);if err!=nil{t.Fatal(err)}
 bad:=[]SourcePair{
  {base.Core,"package fixture\nvar global = func() string {panic(\"hidden\")}()\nfunc Aux() string{return \"ok\"}\n"},
  {base.Core,"package fixture\nfunc init(){panic(\"hidden\")}\nfunc Aux() string{return \"ok\"}\n"},
  {base.Core,"package fixture\nfunc Aux() string{return Build().Legacy.Value}\n"},
  {base.Core,"package fixture\nfunc Aux() string{return \"x\"}\nfunc Mutate(c Clients){c.Legacy.Value=\"new\"}\n"},
  {base.Core,"//go:build ignore\npackage fixture\nfunc Aux() string{return \"x\"}\n"},
  {base.Core,"package fixture\nimport \"unsafe\"\nfunc Aux() string{return \"x\"}\n"},
  {base.Core,"package fixture\nfunc Aux() string{return \"x\"}\n//go:linkname Aux hidden\n"},
  {base.Core,"package fixture\nfunc Aux() string{return \"x\"} /* even harmless comments forbidden */\n"},
  {base.Core,"package fixture\nfunc Aux(){ }\n"},
  {base.Core,"package fixture\nfunc Build() Clients{return Clients{}}\n"},
  {base.Core, "package fixture\nfunc Aux() string{return notDeclared}\n"},
 }
 for i,p:=range bad{
  status,err:=VerifySlice(p,cert,seal)
  if status!=SliceUnknown||!errors.Is(err,ErrSliceScope){t.Fatalf("unsafe auxiliary %d accepted %s %v",i,status,err)}
 }
 t.Logf("F19_CLOSED_WORLD_REJECT invalid_revisions=%d",len(bad))
}
func TestF19ChangedCoreInDifferentNameFailsClosed(t *testing.T){
 base:=f19pair(true,`"x"`);cert,seal,err:=IssueSlice(base);if err!=nil{t.Fatal(err)}
 next:=SourcePair{Core:strings.Replace(base.Core,"p:=&Cell","root:=&Cell",1),Auxiliary:base.Auxiliary}
 status,err:=VerifySlice(next,cert,seal)
 if status!=SliceUnknown||err==nil{t.Fatalf("ill-typed source should reject %s %v",status,err)}
}
func TestF19UntrustedCertificateTamperingRejected(t *testing.T){
 base:=f19pair(false,`"x"`);cert,seal,err:=IssueSlice(base);if err!=nil{t.Fatal(err)}
 cert.Shared=true
 status,err:=VerifySlice(base,cert,seal)
 if status!=SliceUnknown||!errors.Is(err,ErrCertificateIntegrity){t.Fatal(status,err)}
}
func TestF19NativeGoCompilesAndRunsChangedAuxiliary(t *testing.T){
 for _,shared:=range []bool{true,false}{
  for _,v:=range []string{`"old"`,`"new"`}{
   pair:=f19pair(shared,v)
   if err:=AcceptSourcePair(pair);err!=nil{t.Fatal(err)}
   ground,err:=ClassicalFullSliceReanalysis(pair);if err!=nil{t.Fatal(err)}
   dir:=t.TempDir()
   if err:=os.WriteFile(filepath.Join(dir,"go.mod"),[]byte("module fixture\n\ngo 1.23\n"),0644);err!=nil{t.Fatal(err)}
   if err:=os.WriteFile(filepath.Join(dir,"fixture.go"),[]byte(pair.Core),0644);err!=nil{t.Fatal(err)}
   if err:=os.WriteFile(filepath.Join(dir,"aux.go"),[]byte(pair.Auxiliary),0644);err!=nil{t.Fatal(err)}
   test:="package fixture\nimport \"testing\"\nfunc TestNative(t *testing.T){c:=Build();Write(c);if c.Legacy.Value!="+
    strconv.Quote(ground.LegacyAfterWrite)+ "{t.Fatal(\"legacy\")};if c.Future.Value!=\"new\"{t.Fatal(\"future\")};if Aux()!="+v+"{t.Fatal(\"aux\")}}\n"
   if err:=os.WriteFile(filepath.Join(dir,"fixture_test.go"),[]byte(test),0644);err!=nil{t.Fatal(err)}
   cmd:=exec.Command("go","test","-count=1","./...");cmd.Dir=dir;cmd.Env=append(os.Environ(),"GOWORK=off")
   out,err:=cmd.CombinedOutput();if err!=nil{t.Fatalf("native source failed shared=%v aux=%s: %v\n%s",shared,v,err,out)}
  }
 }
 t.Log("F19_NATIVE_CHANGED_SOURCE four_two_file_packages_compiled_executed=true")
}
