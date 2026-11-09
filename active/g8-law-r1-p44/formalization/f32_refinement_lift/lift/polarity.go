package lift
import "fmt"
type ProofLevel string
const(
 Exact ProofLevel="EXACT_COST_EQUALITY"
 LowerOnly ProofLevel="SOUND_COST_LOWER_BOUND_ONLY"
 UpperOnly ProofLevel="CONSTRUCTIVE_COST_UPPER_BOUND_ONLY"
 Unknown ProofLevel="HOLD_INSUFFICIENT_PATH_RELATION"
)
type PolarityReceipt struct{
 Level ProofLevel
 ForwardProjection,BackwardLifting bool
 Grade string
}
type CostBound struct{
 Level ProofLevel
 AbstractCost int
 LowerCertified,UpperCertified bool
}
// ProofPolarity reports the two independent graph simulation obligations.
// False is not proof of real-world impossibility: graph completeness and rights
// are explicitly UNATTESTED caller premises.
func ProofPolarity(m Abstraction)(PolarityReceipt,error){
 if e:=m.Abstract.valid();e!=nil{return PolarityReceipt{},e}
 if e:=m.Concrete.valid();e!=nil{return PolarityReceipt{},e}
 if len(m.Alpha)!=len(m.Concrete.Observations)||m.Alpha[m.Concrete.Initial]!=m.Abstract.Initial{
  return PolarityReceipt{},fmt.Errorf("%w: incomplete abstraction",ErrHold)
 }
 for c,obs:=range m.Concrete.Observations{
  a,ok:=m.Alpha[c];if !ok{return PolarityReceipt{},fmt.Errorf("%w: unmapped",ErrHold)}
  actual,ok:=m.Abstract.Observations[a];if !ok||actual!=obs{return PolarityReceipt{},fmt.Errorf("%w: observation",ErrHold)}
 }
 forward,backward:=true,true
 for c:=range m.Concrete.Observations{
  a:=m.Alpha[c]
  for _,ce:=range m.Concrete.Out[c]{
   found:=false
   for _,ae:=range m.Abstract.Out[a]{
    if ce.Actor==ae.Actor&&ce.Demand==ae.Demand&&ce.Cost==ae.Cost&&m.Alpha[ce.To]==ae.To{found=true;break}
   }
   if !found{forward=false}
  }
  for _,ae:=range m.Abstract.Out[a]{
   found:=false
   for _,ce:=range m.Concrete.Out[c]{
    if ce.Actor==ae.Actor&&ce.Demand==ae.Demand&&ce.Cost==ae.Cost&&m.Alpha[ce.To]==ae.To{found=true;break}
   }
   if !found{backward=false}
  }
 }
 level:=Unknown
 if forward&&backward{level=Exact}else if forward{level=LowerOnly}else if backward{level=UpperOnly}
 return PolarityReceipt{Level:level,ForwardProjection:forward,BackwardLifting:backward,Grade:"FINITE_GRAPH_POLICY_AND_SOURCE_UNATTESTED"},nil
}
func BoundForWord(m Abstraction,w []string)(CostBound,error){
 r,err:=ProofPolarity(m);if err!=nil{return CostBound{},err}
 price,err:=MinDemandEventCost(m.Abstract,m.Abstract.Initial,w);if err!=nil{return CostBound{},err}
 return CostBound{Level:r.Level,AbstractCost:price,LowerCertified:r.ForwardProjection,UpperCertified:r.BackwardLifting},nil
}
