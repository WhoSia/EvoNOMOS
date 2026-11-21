// Package aliascourt is a bounded Go runtime experiment on heap aliasing.
// Source-edit rights and finite abstract graph are explicitly supplied;
// this module does not discover real Go source edit rights automatically.
package aliascourt

type Cell struct { Value string }
type Clients struct { Legacy, Future *Cell }

// Observe emits the JOINT pair from two client references.
func Observe(c Clients) (string,string) {
 return c.Legacy.Value,c.Future.Value
}

func Shared(initial string) Clients {
 p:=&Cell{Value:initial}
 return Clients{Legacy:p,Future:p}
}
func Detached(initial string) Clients {
 return Clients{Legacy:&Cell{Value:initial},Future:&Cell{Value:initial}}
}
func Aliased(c Clients) bool {return c.Legacy==c.Future}

// WriteFuture is an authorized proposed operation, but not necessarily
// old-client safe: aliasing makes it modify the Legacy-visible location.
func WriteFuture(c Clients,value string) {c.Future.Value=value}

// SplitFuture explicitly establishes a fresh disjoint heap cell.
// It is a separate allowed structural modification costing one unit.
func SplitFuture(c *Clients) {
 c.Future=&Cell{Value:c.Future.Value}
}

type State struct {
 Alias bool
 Legacy, Future string
}
type Edge struct{To State; Operation string; Cost int}

// Enumerate is a COMPLETE bounded classical reference graph ONLY for the
// declared two operations SplitFuture and WriteFuture("new").
// No claim that these are all legal Go source changes.
func Enumerate(s State) []Edge {
 var out []Edge
 if s.Alias {
  out=append(out,Edge{State{false,s.Legacy,s.Future},"split",1})
 }
 target:="new"
 if s.Future!=target {
  dest:=State{s.Alias,s.Legacy,target}
  if s.Alias {dest.Legacy=target}
  out=append(out,Edge{dest,"write-future",1})
 }
 return out
}

// SafeCost is an exhaustive BFS preserving an old-client-visible value
// at EVERY declared edit checkpoint.
func SafeCost(initial State,oldValue,goal string) int {
 if initial.Legacy!=oldValue{return -1}
 dist:=map[State]int{initial:0}
 queue:=[]State{initial}
 for len(queue)>0{
  s:=queue[0];queue=queue[1:]
  if s.Future==goal{return dist[s]}
  for _,e:=range Enumerate(s){
   if e.To.Legacy!=oldValue {continue}
   if _,ok:=dist[e.To];ok{continue}
   dist[e.To]=dist[s]+e.Cost
   queue=append(queue,e.To)
  }
 }
 return -1
}

// Marginal-only tracking is unsound for client behavior because a write to
// an aliased pointer changes BOTH legacy and future observations.
func NaiveLocalWriteCost(s State,target string)int{
 if s.Future==target{return 0}
 return 1
}
