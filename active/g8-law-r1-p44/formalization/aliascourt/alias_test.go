package aliascourt

import "testing"

func TestNativeGoSharedWriteBreaksOldClient(t *testing.T){
 c:=Shared("stable")
 if !Aliased(c){t.Fatal("expected same Go heap cell")}
 WriteFuture(c,"new")
 legacy,future:=Observe(c)
 if legacy!="new"||future!="new"{t.Fatalf("aliased observation %q/%q",legacy,future)}
 t.Log("SHARED_ALIAS_WRITE legacy=new future=new old_client_regressed=true")
}
func TestNativeGoSeparateWritePreservesOldClient(t *testing.T){
 c:=Detached("stable")
 if Aliased(c){t.Fatal("expected distinct cells")}
 WriteFuture(c,"new")
 legacy,future:=Observe(c)
 if legacy!="stable"||future!="new"{t.Fatalf("separate observation %q/%q",legacy,future)}
 t.Log("DISJOINT_WRITE legacy=stable future=new safe=true")
}
func TestExplicitSplitThenWriteRepairsAliasedCase(t *testing.T){
 c:=Shared("stable")
 SplitFuture(&c)
 if Aliased(c){t.Fatal("split retained alias")}
 WriteFuture(c,"new")
 legacy,future:=Observe(c)
 if legacy!="stable"||future!="new"{t.Fatalf("split and write %q/%q",legacy,future)}
 t.Log("SHARED_SPLIT_WRITE legacy=stable future=new safe=true")
}
func TestEqualInitialClientObservationDifferentFutureSafeCost(t *testing.T){
 shared:=Shared("stable");separate:=Detached("stable")
 al,af:=Observe(shared);bl,bf:=Observe(separate)
 if al!=bl||af!=bf{t.Fatal("initial joint observations differ")}
 s:=State{Alias:true,Legacy:al,Future:af}
 d:=State{Alias:false,Legacy:bl,Future:bf}
 if got:=SafeCost(s,"stable","new");got!=2{t.Fatalf("shared cost %d",got)}
 if got:=SafeCost(d,"stable","new");got!=1{t.Fatalf("separate cost %d",got)}
 if got:=NaiveLocalWriteCost(s,"new");got!=1{t.Fatalf("expected falsely optimistic local-only cost %d",got)}
 t.Log("ALIAS_COST initial_observations_equal=true shared_safe=2 separate_safe=1 naive_shared=1 classical_exact_tie=true")
}
func TestAuthorizedPatchSetAndPriorContractSensitivity(t *testing.T){
 s:=State{Alias:true,Legacy:"stable",Future:"stable"}
 edges:=Enumerate(s)
 if len(edges)!=2{t.Fatalf("expected split and write only, got %+v",edges)}
 for _,ed:=range edges{
  if ed.Cost!=1{t.Fatal(ed)}
  if ed.Operation=="write-future"&&ed.To.Legacy=="stable"{t.Fatal("missing alias effect")}
  if ed.Operation=="split"&&(ed.To.Alias||ed.To.Legacy!="stable"){t.Fatal("bad disjointness change")}
 }
 if got:=SafeCost(s,"different","new");got!=-1{t.Fatalf("preexisting client contract ignored %d",got)}
}
