package online
import ("testing";"reflect")

func constructed() Game {
 return Game{
  Start:"s",
  Stage1:map[string]bool{"a":true,"b":true},
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
func TestEachFutureHasOfflineSafeRepairButNoOnlineCommitment(t *testing.T){
 g:=constructed()
 if c:=g.Commitments(); !reflect.DeepEqual(c,[]string{"a","b"}){t.Fatal(c)}
 o:=g.OfflinePerFuture()
 if !o["x"]||!o["y"]{t.Fatalf("offline requirement failed: %v",o)}
 if ok,s:=g.OnlineWinning();ok{t.Fatalf("unexpected online winning precommitment: %s",s)}
 t.Logf("OFFLINE_ALL=true ONLINE_WIN=false FAILURES=%v",g.CandidateFutureFailures())
}
func TestCommonCommitmentMakesOnlineWin(t *testing.T){
 g:=constructed()
 g.Edges["a"]=append(g.Edges["a"],Transition{To:"by",Cost:2,Authorized:true})
 if ok,s:=g.OnlineWinning();!ok||s!="a"{t.Fatalf("expected winning a: %v %q",ok,s)}
}
func TestUnapprovedOrUnsafeShortcutCannotFakePolicy(t *testing.T){
 g:=constructed()
 g.Edges["a"]=append(g.Edges["a"],Transition{To:"by",Cost:0,Authorized:false})
 g.Edges["b"]=append(g.Edges["b"],Transition{To:"ax",Cost:0,Authorized:false})
 if ok,_:=g.OnlineWinning();ok{t.Fatal("unapproved path admitted")}
 g.Edges["a"]=append(g.Edges["a"],Transition{To:"u",Cost:0,Authorized:true})
 g.Edges["u"]=[]Transition{{To:"by",Cost:0,Authorized:true}}
 g.Safe["u"]=false
 if ok,_:=g.OnlineWinning();ok{t.Fatal("unsafe intermediate admitted")}
}
func TestInformationTimingMatters(t *testing.T){
 g:=constructed()
 // If both futures are disclosed before the first commitment, each can
 // choose its own path; only the FORCED early decision creates the gap.
 for _,w:=range g.Futures{
  if !g.Reach("s",w.Goal){t.Fatalf("%s unreachable from first source",w.Name)}
 }
}
