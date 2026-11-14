package ownercomposition

import (
 "strings"
 "testing"

 "github.com/spf13/pflag"
)

func TestOldClientSharedMerge(t *testing.T){
 a,b:=NewOwner("a",false),NewOwner("b",false)
 f:=SharedMerge(a,b)
 if err:=f.Parse([]string{"--tenant-a=alpha","--tenant-b=beta"});err!=nil{t.Fatal(err)}
 if *a.Tenant!="alpha"||*b.Tenant!="beta"{t.Fatalf("old mismatch: %q %q",*a.Tenant,*b.Tenant)}
}

func TestOldClientCheckedAndDirect(t *testing.T) {
 for _,variant:=range []string{"checked","direct"} {
  a,b:=NewOwner("a",false),NewOwner("b",false)
  var f *pflag.FlagSet
  if variant=="checked"{
   var err error;f,err=CheckedMerge(a,b);if err!=nil{t.Fatal(err)}
  }else{f=DirectRegister(a,b)}
  if err:=f.Parse([]string{"--tenant-a=alpha","--tenant-b=beta"});err!=nil{t.Fatal(err)}
  if *a.Tenant!="alpha"||*b.Tenant!="beta"{t.Fatalf("%s old mismatch",variant)}
 }
}

func TestOldClientPrefixAndIsolation(t *testing.T){
 f,a,b,_,_:=PrefixRename(false)
 if err:=f.Parse([]string{"--tenant-a=alpha","--tenant-b=beta"});err!=nil{t.Fatal(err)}
 if *a!="alpha"||*b!="beta"{t.Fatal("prefix failed old")}
 oA,oB:=NewOwner("a",false),NewOwner("b",false)
 if err:=oA.Flags.Parse([]string{"--tenant-a=alpha"});err!=nil{t.Fatal(err)}
 if err:=oB.Flags.Parse([]string{"--tenant-b=beta"});err!=nil{t.Fatal(err)}
 if *oA.Tenant!="alpha"||*oB.Tenant!="beta"{t.Fatal("isolated failed old")}
}

func TestNewDemandIndependentlyPassesEachOwner(t *testing.T){
 a,b:=NewOwner("a",true),NewOwner("b",true)
 if err:=a.Flags.Parse([]string{"--tenant-a=alpha","--channel=canary"});err!=nil{t.Fatal(err)}
 if err:=b.Flags.Parse([]string{"--tenant-b=beta","--channel=stable"});err!=nil{t.Fatal(err)}
 if *a.Channel!="canary"||*b.Channel!="stable"{t.Fatalf("local values wrong: %q %q",*a.Channel,*b.Channel)}
}

func TestNewDemandSharedMergeSilentlyDropsOwnerB(t *testing.T) {
 a,b:=NewOwner("a",true),NewOwner("b",true)
 f:=SharedMerge(a,b)
 // The actual original AddFlagSet silently leaves out the duplicate B flag.
 if f.Lookup("channel")==nil{t.Fatal("missing A channel")}
 if err:=f.Parse([]string{"--tenant-a=alpha","--tenant-b=beta","--channel=canary"});err!=nil{t.Fatal(err)}
 if *a.Tenant!="alpha"||*b.Tenant!="beta"{t.Fatal("old requirements must survive")}
 if *a.Channel!="canary"{t.Fatal("A was not bound")}
 if *b.Channel!="bdefault"{t.Fatalf("unexpected B binding %q",*b.Channel)}
 if *b.Channel=="stable"{t.Fatal("expected joint new D1 failure not reproduced")}
}

func TestNewDemandDirectAddFlagPanicsOnCollision(t *testing.T){
 a,b:=NewOwner("a",true),NewOwner("b",true)
 defer func(){
  recovered:=recover()
  if recovered==nil{t.Error("expected original source duplicate panic")}
  if recovered!=nil && !strings.Contains(recovered.(string),"flag redefined: channel"){
   t.Errorf("wrong panic: %v",recovered)
  }
 }()
 _=DirectRegister(a,b)
}

func TestNewDemandCheckedMergeExplicitlyRefuses(t *testing.T){
 a,b:=NewOwner("a",true),NewOwner("b",true)
 _,err:=CheckedMerge(a,b)
 if err==nil||!strings.Contains(err.Error(),"collision: channel"){t.Fatalf("should be explicit refusal: %v",err)}
}

func TestNewDemandStrongPrefixRivalSucceeds(t *testing.T){
 f,a,b,cA,cB:=PrefixRename(true)
 if err:=f.Parse([]string{"--tenant-a=alpha","--tenant-b=beta","--a-channel=canary","--b-channel=stable"});err!=nil{t.Fatal(err)}
 if *a!="alpha"||*b!="beta"||*cA!="canary"||*cB!="stable"{
  t.Fatalf("prefix rival wrong: a=%q b=%q ca=%q cb=%q",*a,*b,*cA,*cB)
 }
}

func TestNewDemandStrongIsolationRivalSucceeds(t *testing.T){
 a,b:=NewOwner("a",true),NewOwner("b",true)
 if err:=a.Flags.Parse([]string{"--tenant-a=alpha","--channel=canary"});err!=nil{t.Fatal(err)}
 if err:=b.Flags.Parse([]string{"--tenant-b=beta","--channel=stable"});err!=nil{t.Fatal(err)}
 if *a.Tenant!="alpha"||*b.Tenant!="beta"||*a.Channel!="canary"||*b.Channel!="stable"{t.Fatal("isolation rival wrong")}
}

func TestSourceAwareClassicDuplicateDetector(t *testing.T){
 a,b:=NewOwner("a",true),NewOwner("b",true)
 // Exact same normalized namespace as concrete pflag, no exotic algorithm.
 duplicates:=map[string]int{}
 for _,o:=range []Owner{a,b}{
  o.Flags.VisitAll(func(f *pflag.Flag){duplicates[f.Name]++})
 }
 if duplicates["channel"]!=2||duplicates["tenant-a"]!=1||duplicates["tenant-b"]!=1{
  t.Fatalf("classical name analysis failed: %+v",duplicates)
 }
}
