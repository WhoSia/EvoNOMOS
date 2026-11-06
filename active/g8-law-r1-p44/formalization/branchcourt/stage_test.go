package branchcourt
import "testing"

// A previously accepted flag=false client must continue observing "on".
// A future demand now wants flag=true to produce "beta".
func TestFutureDemandWithoutRegressionAndImpossibleAlternative(t *testing.T){
 g,e:=Enumerate(fixture,Policy{Allowed:[]string{"off","on","beta"}})
 if e!=nil{t.Fatal(e)}
 start:=State{"off","on"}
 permitted:=func(s State)bool{
  source,exists:=g.Sources[s];if !exists{return false}
  legacy,future,err:=Observe(source,false)
  return err==nil&&legacy=="stable"&&future=="on"
 }
 safeDistance:=func(goal State)int{
  if !permitted(start)||!permitted(goal){return -1}
  distance:=map[State]int{start:0};queue:=[]State{start}
  for len(queue)>0 {
   s:=queue[0];queue=queue[1:]
   if s==goal{return distance[s]}
   for _,ed:=range g.Edges {
    if ed.From!=s||!permitted(ed.To){continue}
    if _,ok:=distance[ed.To];ok{continue}
    distance[ed.To]=distance[s]+ed.Cost;queue=append(queue,ed.To)
   }
  }
  return -1
 }
 if got:=safeDistance(State{"beta","on"});got!=1{t.Fatalf("safe evolution cost %d",got)}
 unconstrained,e:=ExactDistance(g,start,State{"beta","off"})
 if e!=nil||unconstrained!=2{t.Fatal(unconstrained,e)}
 if got:=safeDistance(State{"beta","off"});got!=-1{t.Fatalf("client-regressing goal accepted %d",got)}
 t.Log("STAGED_CLIENT_PRECONDITION safe_future_change_cost=1 forbidden_old_client_regression=true")
}
