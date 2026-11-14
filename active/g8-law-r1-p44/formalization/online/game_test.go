package online

import ("reflect";"testing")

func constructed()Game{
 return Game{
  Start:"s",
  Stage1:map[string]bool{"a":true,"b":true,"ax":true,"by":true},
  Checkpoint:map[string]bool{"a":true,"b":true},
  Safe:map[string]bool{"s":true,"a":true,"b":true,"ax":true,"by":true},
  Edges:map[string][]Transition{
   "s":{{To:"a",Cost:1,Authorized:true},{To:"b",Cost:1,Authorized:true}},
   "a":{{To:"ax",Cost:1,Authorized:true}},
   "b":{{To:"by",Cost:1,Authorized:true}},
  },
  Futures:[]World{
   {Name:"x",Goal:map[string]bool{"ax":true}},
   {Name:"y",Goal:map[string]bool{"by":true}},
  },
 }
}
func TestOfflinePerFutureDoesNotGuaranteeNonanticipatingStrategy(t *testing.T){
 g:=constructed()
 if c:=g.Commitments();!reflect.DeepEqual(c,[]string{"a","b"}){t.Fatal(c)}
 o:=g.OfflinePerFuture()
 if !o["x"]||!o["y"]{t.Fatalf("offline future fails: %v",o)}
 if ok,s:=g.OnlineWinning();ok{t.Fatalf("nonanticipating policy should fail: %s",s)}
 t.Logf("OFFLINE_ALL=true ONLINE_WIN=false FAILURES=%v",g.CandidateFutureFailures())
}
func TestCommonCommitmentMakesOnlineWin(t *testing.T){
 g:=constructed()
 g.Edges["a"]=append(g.Edges["a"],Transition{To:"by",Cost:2,Authorized:true})
 if ok,s:=g.OnlineWinning();!ok||s!="a"{t.Fatalf("expected winning a: %v %q",ok,s)}
}
func TestUnauthorizedOrUnsafeShortcutCannotFakePolicy(t *testing.T){
 g:=constructed()
 g.Edges["a"]=append(g.Edges["a"],Transition{To:"by",Cost:0,Authorized:false})
 if ok,_:=g.OnlineWinning();ok{t.Fatal("unauthorized path accepted")}
 g.Edges["a"]=append(g.Edges["a"],Transition{To:"u",Cost:0,Authorized:true})
 g.Edges["u"]=[]Transition{{To:"by",Cost:0,Authorized:true}}
 g.Safe["u"]=false
 if ok,_:=g.OnlineWinning();ok{t.Fatal("unsafe intermediate accepted")}
}
func TestEarlierAcceptedContractMustSurviveLaterRepair(t *testing.T){
 g:=constructed()
 g.Safe["u"]=true
 g.Edges["a"]=append(g.Edges["a"],Transition{To:"u",Cost:0,Authorized:true})
 g.Edges["u"]=[]Transition{{To:"by",Cost:0,Authorized:true}}
 if !g.Reach("a",g.Futures[1].Goal,false){t.Fatal("unprotected path should exist")}
 if g.Reach("a",g.Futures[1].Goal,true){t.Fatal("stage-one contract regressed but path accepted")}
 if ok,_:=g.OnlineWinning();ok{t.Fatal("false online winner through contract regression")}
}
func TestDecisionTimingNotOnlyGraphReachability(t *testing.T){
 g:=constructed()
 for _,w:=range g.Futures{
  if !g.Reach("s",w.Goal,false){t.Fatalf("%s unreachable before disclosure",w.Name)}
 }
}

func TestAbstractExtraSystemEditProducesSpuriousOnlineWinningClaim(t *testing.T){
 concrete:=constructed()
 if ok,_:=concrete.OnlineWinning();ok{t.Fatal("concrete must be losing")}
 // The abstract model invents one *system* edit not present in concrete.
 // Existential system overapproximation is UNSOUND for proving winning.
 abstract:=constructed()
 abstract.Edges["a"]=append(abstract.Edges["a"],Transition{To:"by",Cost:0,Authorized:true})
 if ok,s:=abstract.OnlineWinning();!ok||s!="a"{t.Fatalf("expected spurious abstract winning policy, got %v %s",ok,s)}
 t.Log("POLARITY system-overapprox=false-positive-winning")
}
func TestAbstractExtraEnvironmentDemandProducesSpuriousLosingClaim(t *testing.T){
 concrete:=constructed()
 concrete.Edges["a"]=append(concrete.Edges["a"],Transition{To:"by",Cost:1,Authorized:true})
 if ok,_:=concrete.OnlineWinning();!ok{t.Fatal("concrete winner absent")}
 // Overapproximating the environment's allowable demands with a new
 // impossible z may be conservative for verifying WIN but can produce
 // spurious LOSING verdicts.
 abstract:=concrete
 abstract.Futures=append([]World{},concrete.Futures...)
 abstract.Futures=append(abstract.Futures,World{Name:"z",Goal:map[string]bool{"zgoal":true}})
 if ok,_:=abstract.OnlineWinning();ok{t.Fatal("expected spurious loss under extra environment demand")}
 t.Log("POLARITY environment-overapprox=false-negative-winning")
}
