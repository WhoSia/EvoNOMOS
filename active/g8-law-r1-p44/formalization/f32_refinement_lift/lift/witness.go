package lift
import("fmt";"sort")
// CounterWitness identifies a reproducible missing concrete source-edit option.
// It is diagnostic for the supplied finite graph, not a real-source witness.
type CounterWitness struct{
 ConcreteState string
 AbstractState string
 AbstractEdge Edge
 Reason string
}
// FirstUnliftableEdit is diagnostic only; use CheckTwoWay for FULL certificate.
func FirstUnliftableEdit(m Abstraction)(CounterWitness,bool,error){
 if e:=m.Concrete.valid();e!=nil{return CounterWitness{},false,e}
 if e:=m.Abstract.valid();e!=nil{return CounterWitness{},false,e}
 states:=make([]string,0,len(m.Concrete.Observations))
 for s:=range m.Concrete.Observations{states=append(states,s)}
 sort.Strings(states)
 for _,s:=range states{
  a,ok:=m.Alpha[s];if !ok{return CounterWitness{},false,fmt.Errorf("%w: unmapped state",ErrHold)}
  if _,ok:=m.Abstract.Out[a];!ok{return CounterWitness{},false,fmt.Errorf("%w: unknown abstract state",ErrHold)}
  for _,abstractEdge:=range m.Abstract.Out[a]{
   found:=false
   for _,concreteEdge:=range m.Concrete.Out[s]{
    p:=concreteEdge;p.To=m.Alpha[concreteEdge.To]
    if same(p,abstractEdge){found=true;break}
   }
   if !found{return CounterWitness{ConcreteState:s,AbstractState:a,AbstractEdge:abstractEdge,Reason:"abstract edit has no source-representative concrete witness"},true,nil}
  }
 }
 return CounterWitness{},false,nil
}
