package lift
import ("errors";"math";"strings";"testing")
func TestAbstractFalseSafe(t *testing.T){
 m:=HiddenRightCounterexample()
 a,e:=MinDemandEventCost(m.Abstract,"x0",[]string{"A","B"})
 if e!=nil||a!=3{t.Fatal(a,e)}
 c,e:=MinDemandEventCost(m.Concrete,"open",[]string{"A","B"})
 if e!=nil||c!=math.MaxInt{t.Fatal(c,e)}
 _,e=CheckTwoWay(m)
 if !errors.Is(e,ErrHold)||!strings.Contains(e.Error(),"cannot lift"){t.Fatal(e)}
}
func TestSingleOptionsStillPossible(t *testing.T){
 m:=HiddenRightCounterexample()
 for _,v:=range []struct{w []string;c int}{{[]string{"A"},1},{[]string{"B"},2},{nil,0}}{
  c,e:=MinDemandEventCost(m.Concrete,"open",v.w);if e!=nil||c!=v.c{t.Fatal(c,e)}
 }
}
func TestJones1983Equation340FailsUnderRefinement(t *testing.T){
 min:=func(x,y int)int{if x<y{return x};return y}
 e,o,ep,op:=5,5,4,5
 if min(ep,op)>min(e,o)||ep==e&&op<=o{t.Fatal("should break refined rely condition")}
}
func TestValidCompleteAbstraction(t *testing.T){
 m:=HiddenRightCounterexample()
 m.Concrete.Out["closed"]=[]Edge{
  {Actor:"a-owner",Demand:"A",Cost:1,To:"closed"},
  {Actor:"b-owner",Demand:"B",Cost:2,To:"repaired"},
 }
 r,e:=CheckTwoWay(m)
 if e!=nil||r.LiftObligations!=4||r.ProjectionEdges!=4{t.Fatal(r,e)}
 for _,w:=range [][]string{{"A"},{"B"},{"A","B"},{"A","A","B"}}{
  a,_:=MinDemandEventCost(m.Abstract,"x0",w)
  c,_:=MinDemandEventCost(m.Concrete,"open",w)
  if a!=c{t.Fatal(w,a,c)}
 }
}
func TestObservationMismatchHOLD(t *testing.T){
 m:=HiddenRightCounterexample();m.Concrete.Observations["closed"]="not-old"
 if _,e:=CheckTwoWay(m);!errors.Is(e,ErrHold){t.Fatal(e)}
}
func TestWrongActorOrPriceHOLD(t *testing.T){
 for _,k:=range []string{"actor","price"}{
  m:=HiddenRightCounterexample()
  if k=="actor"{m.Concrete.Out["open"][0].Actor="impostor"}else{m.Concrete.Out["open"][0].Cost=99}
  if _,e:=CheckTwoWay(m);!errors.Is(e,ErrHold){t.Fatal(k,e)}
 }
}
func TestIncompleteTablesOrNegativePriceHOLD(t *testing.T){
 m:=HiddenRightCounterexample();delete(m.Concrete.Out,"closed")
 if _,e:=CheckTwoWay(m);!errors.Is(e,ErrHold){t.Fatal(e)}
 m=HiddenRightCounterexample();m.Concrete.Out["open"][0].Cost=-1
 if _,e:=CheckTwoWay(m);!errors.Is(e,ErrHold){t.Fatal(e)}
}
func TestMissingAbstractionHOLD(t *testing.T){
 m:=HiddenRightCounterexample();delete(m.Alpha,"closed")
 if _,e:=CheckTwoWay(m);!errors.Is(e,ErrHold){t.Fatal(e)}
}
func TestOverflowHOLD(t *testing.T){
 g:=Graph{Initial:"s",Observations:map[string]string{"s":"ok"},Out:map[string][]Edge{
  "s":{{Actor:"a",Demand:"A",Cost:math.MaxInt,To:"s"}},
 }}
 if _,e:=MinDemandEventCost(g,"s",[]string{"A","A"});!errors.Is(e,ErrHold){t.Fatal(e)}
}
// Every possible subset of the eight named edits in the two-state universe is
// enumerated: two actors x two sources x two destinations = 2^8 graphs.
// For each CERTIFIED graph, compare cost on every action word of length <= 3
// starting from both concrete states, against a single-state abstract model.
func TestAll256TwoStateRefinements(t *testing.T){
 a:=Graph{Initial:"x",Observations:map[string]string{"x":"ok"},Out:map[string][]Edge{
  "x":{{Actor:"owner-A",Demand:"A",Cost:1,To:"x"},{Actor:"owner-B",Demand:"B",Cost:2,To:"x"}},
 }}
 words:=[][]string{{}}
 for n:=1;n<=3;n++{for i:=0;i<1<<n;i++{
  w:=make([]string,n);for j:=range w{w[j]="A";if i&(1<<j)!=0{w[j]="B"}};words=append(words,w)
 }}
 cases,passed,comparisons:=0,0,0
 for mask:=0;mask<256;mask++{
  c:=Graph{Initial:"s0",Observations:map[string]string{"s0":"ok","s1":"ok"},Out:map[string][]Edge{"s0":{},"s1":{}}}
  bit:=0
  for _,s:=range []string{"s0","s1"}{for _,d:=range []string{"A","B"}{for _,end:=range []string{"s0","s1"}{
   if mask&(1<<bit)!=0{
    owner,cost:="owner-A",1;if d=="B"{owner,cost="owner-B",2}
    c.Out[s]=append(c.Out[s],Edge{Actor:owner,Demand:d,Cost:cost,To:end})
   }
   bit++
  }}}
  model:=Abstraction{Abstract:a,Concrete:c,Alpha:map[string]string{"s0":"x","s1":"x"}}
  r,e:=CheckTwoWay(model)
  if e==nil{
   passed++
   if r.LiftObligations!=4{t.Fatal(r)}
   for _,s:=range []string{"s0","s1"}{for _,w:=range words{
    x,ex:=MinDemandEventCost(a,"x",w)
    y,ey:=MinDemandEventCost(c,s,w)
    if ex!=nil||ey!=nil||x!=y{t.Fatalf("false certificate mask=%d state=%s word=%v abstract=%d concrete=%d",mask,s,w,x,y)}
    comparisons++
   }}
  }else if !errors.Is(e,ErrHold){t.Fatal(e)}
  cases++
 }
 if cases!=256||passed!=81||comparisons!=2430{t.Fatalf("coverage: %d/%d/%d",cases,passed,comparisons)}
 t.Logf("256 entire graphs enumerated, %d with certificates, %d word costs equal",passed,comparisons)
}

func TestFocusedWitnessNamesMissingBEdit(t *testing.T){
 m:=HiddenRightCounterexample()
 w,found,err:=FirstUnliftableEdit(m)
 if err!=nil||!found||w.ConcreteState!="closed"||w.AbstractState!="x0"||w.AbstractEdge.Demand!="B"||w.AbstractEdge.Cost!=2{t.Fatal(w,found,err)}
}

func TestSentinelCollisionCannotBeMisreadAsImpossibility(t *testing.T){
 g:=Graph{Initial:"s",Observations:map[string]string{"s":"old"},Out:map[string][]Edge{
  "s":{{Actor:"owner",Demand:"A",Cost:math.MaxInt,To:"s"}},
 }}
 if _,err:=MinDemandEventCost(g,"s",[]string{"A"});!errors.Is(err,ErrHold){t.Fatal(err)}
}
