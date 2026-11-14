package lift
import("testing";"math")
func TestFourCertificatePolarities(t *testing.T){
 lower:=HiddenRightCounterexample()
 r,e:=ProofPolarity(lower)
 if e!=nil||r.Level!=LowerOnly||!r.ForwardProjection||r.BackwardLifting{t.Fatal(r,e)}
 b,e:=BoundForWord(lower,[]string{"A","B"})
 if e!=nil||b.AbstractCost!=3||!b.LowerCertified||b.UpperCertified{t.Fatal(b,e)}
 upper:=Abstraction{
  Abstract:Graph{Initial:"x",Observations:map[string]string{"x":"old"},Out:map[string][]Edge{"x":{{Actor:"owner",Demand:"A",Cost:1,To:"x"}}}},
  Concrete:Graph{Initial:"c",Observations:map[string]string{"c":"old"},Out:map[string][]Edge{"c":{{Actor:"owner",Demand:"A",Cost:1,To:"c"},{Actor:"owner",Demand:"B",Cost:2,To:"c"}}}},
  Alpha:map[string]string{"c":"x"},
 }
 r,e=ProofPolarity(upper)
 if e!=nil||r.Level!=UpperOnly||r.ForwardProjection||!r.BackwardLifting{t.Fatal(r,e)}
 c,_:=MinDemandEventCost(upper.Concrete,"c",[]string{"B"})
 a,_:=MinDemandEventCost(upper.Abstract,"x",[]string{"B"})
 if c!=2||a!=math.MaxInt{t.Fatal(c,a)}
 exact:=upper
 exact.Concrete.Out["c"]=exact.Concrete.Out["c"][:1]
 r,e=ProofPolarity(exact);if e!=nil||r.Level!=Exact{t.Fatal(r,e)}
 unknown:=HiddenRightCounterexample()
 unknown.Concrete.Out["open"]=append(unknown.Concrete.Out["open"],Edge{Actor:"other",Demand:"C",Cost:2,To:"open"})
 r,e=ProofPolarity(unknown)
 if e!=nil||r.Level!=Unknown||r.ForwardProjection||r.BackwardLifting{t.Fatal(r,e)}
}
func TestProjectionOnlyCertifiesLowerBoundNotConstructivePath(t *testing.T){
 m:=HiddenRightCounterexample()
 b,e:=BoundForWord(m,[]string{"C"})
 if e!=nil||b.Level!=LowerOnly||b.AbstractCost!=math.MaxInt||!b.LowerCertified||b.UpperCertified{t.Fatal(b,e)}
}
