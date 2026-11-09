// Package lift checks classical two-way simulation between user-supplied
// complete finite edit graphs. It does NOT extract Go source or attest rights.
package lift
import (
 "errors"
 "fmt"
 "container/heap"
 "math"
)
var ErrHold=errors.New("HOLD: abstract edit option not certified")
type Edge struct { Actor,Demand string; Cost int; To string }
type Graph struct { Initial string; Observations map[string]string; Out map[string][]Edge }
type Abstraction struct { Abstract,Concrete Graph; Alpha map[string]string }
type Receipt struct { Grade string; ProjectionEdges,LiftObligations,ObservationPairs int }
func(g Graph)valid()error{
 if len(g.Observations)==0||len(g.Out)!=len(g.Observations){return fmt.Errorf("%w: incomplete table",ErrHold)}
 if _,ok:=g.Observations[g.Initial];!ok{return fmt.Errorf("%w: no initial",ErrHold)}
 for s:=range g.Observations{if _,ok:=g.Out[s];!ok{return fmt.Errorf("%w: no outgoing table",ErrHold)}}
 for s,edges:=range g.Out{
  if _,ok:=g.Observations[s];!ok{return fmt.Errorf("%w: undeclared state",ErrHold)}
  for _,e:=range edges{
   if e.Actor==""||e.Demand==""||e.Cost<0{return fmt.Errorf("%w: bad label",ErrHold)}
   if _,ok:=g.Observations[e.To];!ok{return fmt.Errorf("%w: unknown target",ErrHold)}
  }
 }
 return nil
}
func same(a,b Edge)bool{return a.Actor==b.Actor&&a.Demand==b.Demand&&a.Cost==b.Cost&&a.To==b.To}
// CheckTwoWay is a strong bisimulation check along the declared Alpha map.
// A failed condition means HOLD, not that no source repair is possible.
func CheckTwoWay(m Abstraction)(Receipt,error){
 if e:=m.Abstract.valid();e!=nil{return Receipt{},e}
 if e:=m.Concrete.valid();e!=nil{return Receipt{},e}
 if len(m.Alpha)!=len(m.Concrete.Observations)||m.Alpha[m.Concrete.Initial]!=m.Abstract.Initial{
  return Receipt{},fmt.Errorf("%w: incomplete/incorrect abstraction",ErrHold)
 }
 r:=Receipt{Grade:"FINITE_TWO_WAY_EDIT_SIMULATION_UNATTESTED"}
 for c,obs:=range m.Concrete.Observations{
  a,ok:=m.Alpha[c];if !ok{return Receipt{},fmt.Errorf("%w: missing alpha",ErrHold)}
  o,ok:=m.Abstract.Observations[a];if !ok||o!=obs{return Receipt{},fmt.Errorf("%w: observation",ErrHold)}
  r.ObservationPairs++
  for _,ce:=range m.Concrete.Out[c]{
   dest,ok:=m.Alpha[ce.To];if !ok{return Receipt{},fmt.Errorf("%w: unknown alpha dest",ErrHold)}
   p:=ce;p.To=dest;found:=false
   for _,ae:=range m.Abstract.Out[a]{if same(p,ae){found=true;break}}
   if !found{return Receipt{},fmt.Errorf("%w: concrete edge lacks abstract projection",ErrHold)}
   r.ProjectionEdges++
  }
  for _,ae:=range m.Abstract.Out[a]{
   found:=false
   for _,ce:=range m.Concrete.Out[c]{
    p:=ce;p.To=m.Alpha[ce.To]
    if same(p,ae){found=true;break}
   }
   if !found{return Receipt{},fmt.Errorf("%w: abstract edge cannot lift at %s",ErrHold,c)}
   r.LiftObligations++
  }
 }
 return r,nil
}
type node struct{state string;k,price int}
type pq []*node
func(p pq)Len()int{return len(p)}
func(p pq)Less(i,j int)bool{return p[i].price<p[j].price}
func(p pq)Swap(i,j int){p[i],p[j]=p[j],p[i]}
func(p *pq)Push(x any){*p=append(*p,x.(*node))}
func(p *pq)Pop()any{a:=*p;x:=a[len(a)-1];*p=a[:len(a)-1];return x}
// MinDemandEventCost computes an exact finite edit EVENT word, not
// persistent state-goal satisfaction. Infeasible returns math.MaxInt.
func MinDemandEventCost(g Graph,start string,word []string)(int,error){
 if err:=g.valid();err!=nil{return 0,err}
 if _,ok:=g.Observations[start];!ok{return 0,fmt.Errorf("%w: start",ErrHold)}
 type key struct{state string;k int}
 d:=map[key]int{{start,0}:0}
 q:=pq{&node{start,0,0}};heap.Init(&q)
 for q.Len()!=0{
  cur:=heap.Pop(&q).(*node)
  if cur.price!=d[key{cur.state,cur.k}]{continue}
  if cur.k==len(word){return cur.price,nil}
  for _,e:=range g.Out[cur.state]{
   if e.Demand!=word[cur.k]{continue}
   if cur.price>math.MaxInt-e.Cost{return 0,fmt.Errorf("%w: cost overflow",ErrHold)}
   nk:=key{e.To,cur.k+1};v:=cur.price+e.Cost
   if old,ok:=d[nk];!ok||v<old{d[nk]=v;heap.Push(&q,&node{e.To,cur.k+1,v})}
  }
 }
 return math.MaxInt,nil
}
func HiddenRightCounterexample()Abstraction{
 a:=Graph{Initial:"x0",Observations:map[string]string{"x0":"old","x1":"old"},Out:map[string][]Edge{
  "x0":{{Actor:"a-owner",Demand:"A",Cost:1,To:"x0"},{Actor:"b-owner",Demand:"B",Cost:2,To:"x1"}},
  "x1":{},
 }}
 c:=Graph{Initial:"open",Observations:map[string]string{"open":"old","closed":"old","repaired":"old"},Out:map[string][]Edge{
  "open":{{Actor:"a-owner",Demand:"A",Cost:1,To:"closed"},{Actor:"b-owner",Demand:"B",Cost:2,To:"repaired"}},
  "closed":{{Actor:"a-owner",Demand:"A",Cost:1,To:"closed"}},"repaired":{},
 }}
 return Abstraction{Abstract:a,Concrete:c,Alpha:map[string]string{"open":"x0","closed":"x0","repaired":"x1"}}
}
