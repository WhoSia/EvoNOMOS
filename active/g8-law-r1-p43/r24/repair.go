package r24

import ("container/heap";"errors";"math")
type Step struct{From,To,Right string;Cost int}
type RepairGraph struct{Safe map[string]bool;Goal map[string]bool;Steps []Step}
type item struct{State string;Cost int}
type queue []item
func(q queue)Len()int{return len(q)}
func(q queue)Less(i,j int)bool{return q[i].Cost<q[j].Cost}
func(q queue)Swap(i,j int){q[i],q[j]=q[j],q[i]}
func(q *queue)Push(x any){*q=append(*q,x.(item))}
func(q *queue)Pop()any{a:=*q;x:=a[len(a)-1];*q=a[:len(a)-1];return x}
var ErrUnsafeStart=errors.New("initial state violates protected contract")
var ErrInvalidCost=errors.New("negative edit cost")
// MinimumSafeCost: finite explicitly permission-labeled edit graph. Never general-Go impossibility.
func MinimumSafeCost(g RepairGraph,start string,rights map[string]bool)(int,bool,error){
 if !g.Safe[start]{return 0,false,ErrUnsafeStart}
 for _,e:=range g.Steps{if e.Cost<0{return 0,false,ErrInvalidCost}}
 dist:=map[string]int{start:0};pq:=&queue{{start,0}};heap.Init(pq)
 for pq.Len()>0{
  cur:=heap.Pop(pq).(item);if cur.Cost!=dist[cur.State]{continue}
  if g.Goal[cur.State]{return cur.Cost,true,nil}
  for _,e:=range g.Steps{
   if e.From!=cur.State||!rights[e.Right]||!g.Safe[e.To]||cur.Cost>math.MaxInt-e.Cost{continue}
   nc:=cur.Cost+e.Cost
   if d,ok:=dist[e.To];!ok||nc<d{dist[e.To]=nc;heap.Push(pq,item{e.To,nc})}
  }
 }
 return 0,false,nil
}
