package edgecert

import (
  "errors"
  "testing"
)

func fixtures()(Graph,Graph,Certificate){
 concrete:=Graph{Start:"s",States:map[string]State{
  "s":{Stage:1,Safe:true},"a":{Stage:1,Safe:true},"g":{Stage:1,Safe:true,Goal:true},
  "bad":{Stage:1,Safe:false},
 },Edges:[]Edge{
  {From:"s",To:"a",Right:"app-edit",Cost:2,Authorized:true},
  {From:"a",To:"g",Right:"app-edit",Cost:2,Authorized:true},
  {From:"s",To:"g",Right:"app-edit",Cost:7,Authorized:true},
  {From:"s",To:"g",Right:"upstream",Cost:0,Authorized:false},
  {From:"s",To:"bad",Right:"app-edit",Cost:0,Authorized:true},
  {From:"bad",To:"g",Right:"app-edit",Cost:0,Authorized:true},
 }}
 abstract:=Graph{Start:"S",States:map[string]State{
  "S":{Stage:1,Safe:true},"A":{Stage:1,Safe:true},"G":{Stage:1,Safe:true,Goal:true},
 },Edges:[]Edge{
  {From:"S",To:"A",Right:"app-edit",Cost:2,Authorized:true},
  {From:"A",To:"G",Right:"app-edit",Cost:2,Authorized:true},
  {From:"S",To:"G",Right:"app-edit",Cost:7,Authorized:true},
  {From:"S",To:"G",Right:"app-edit",Cost:1,Authorized:true}, // spurious
 }}
 cert:=Certificate{Image:map[string]string{"s":"S","a":"A","g":"G"}}
 return concrete,abstract,cert
}
func TestSoundLocalSimulationProducesCostSandwich(t *testing.T){
 c,a,cert:=fixtures()
 if e:=Verify(c,a,cert);e!=nil{t.Fatal(e)}
 k,e:=Shortest(c);if e!=nil||k!=4{t.Fatalf("exact finite cost=%d error=%v",k,e)}
 u,e:=CheckWitness(c,[]string{"s","a","g"});if e!=nil||u!=4{t.Fatal(u,e)}
 l,e:=Shortest(a);if e!=nil||l!=1||l>k||k>u{t.Fatalf("sandwich L=%d K=%d U=%d %v",l,k,u,e)}
 t.Logf("FINITECERT lower=%d exact=%d upper=%d",l,k,u)
 a.Edges=a.Edges[:len(a.Edges)-1]
 if e:=Verify(c,a,cert);e!=nil{t.Fatal(e)}
 l,e=Shortest(a);if e!=nil||l!=4||l!=k{t.Fatalf("refined L=%d K=%d %v",l,k,e)}
 t.Logf("REFINEDCERT lower=%d exact=%d upper=%d",l,k,u)
}
func TestOmittedSafeConcreteEdgeRejected(t *testing.T){
 c,a,cert:=fixtures();a.Edges=a.Edges[1:]
 if e:=Verify(c,a,cert);!errors.Is(e,ErrMissingTransition){t.Fatalf("unexpected %v",e)}
}
func TestOverpricedAbstractEditRejected(t *testing.T){
 c,a,cert:=fixtures();for i:=range a.Edges{if a.Edges[i].From=="S"&&a.Edges[i].To=="A" {a.Edges[i].Cost=3}}
 if e:=Verify(c,a,cert);!errors.Is(e,ErrMissingTransition){t.Fatalf("unexpected %v",e)}
}
func TestMissingGoalAndStageReflectionRejected(t *testing.T){
 c,a,cert:=fixtures();g:=a.States["G"];g.Goal=false;a.States["G"]=g
 if e:=Verify(c,a,cert);!errors.Is(e,ErrGoalOmission){t.Fatal(e)}
 _,a,cert=fixtures();g=a.States["A"];g.Stage=2;a.States["A"]=g
 if e:=Verify(c,a,cert);!errors.Is(e,ErrStageMismatch){t.Fatal(e)}
}
func TestUnauthorizedAndUnsafeShortcutsNotCounted(t *testing.T){
 c,_,_:=fixtures();cost,e:=Shortest(c)
 if e!=nil||cost!=4{t.Fatal(cost,e)}
 if _,e:=CheckWitness(c,[]string{"s","bad","g"});!errors.Is(e,ErrInvalidWitness){t.Fatal(e)}
 if _,e:=CheckWitness(c,[]string{"s","g"});e!=nil{t.Fatal(e)}
}
func TestUntrustedGraphCanHideRealEditAndYieldFalseSourceClaim(t *testing.T) {
 c,a,cert:=fixtures()
 a.Edges=a.Edges[:len(a.Edges)-1]
 if e:=Verify(c,a,cert);e!=nil{t.Fatal(e)}
 k,e:=Shortest(c);if e!=nil||k!=4{t.Fatal(k,e)}
 l,e:=Shortest(a);if e!=nil||l!=4{t.Fatal(l,e)}
 c.Edges=append(c.Edges,Edge{From:"s",To:"g",Right:"app-edit",Cost:1,Authorized:true})
 k,e=Shortest(c);if e!=nil||k!=1{t.Fatal(k,e)}
 if e:=Verify(c,a,cert);!errors.Is(e,ErrMissingTransition){t.Fatalf("missed source edit should invalidate prior lower certificate: %v",e)}
 t.Logf("SOURCE_COMPLETENESS_VIOLATION old_cert_lower=%d newly_discovered_concrete_cost=%d",l,k)
}
func TestAbstractUnsafeImageRejected(t *testing.T) {
 c,a,cert:=fixtures()
 v:=a.States["A"];v.Safe=false;a.States["A"]=v
 if e:=Verify(c,a,cert);!errors.Is(e,ErrMissingState){t.Fatalf("abstract image unsafe: %v",e)}
}
