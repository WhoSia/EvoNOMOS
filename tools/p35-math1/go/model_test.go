package math1
import "testing"

func TestFirstSeparatorLengthOne(t *testing.T){
 r:=Evaluate()
 if !r.DepthZeroEqual||r.DepthOneEqual||r.FirstLength!=1||len(r.FirstSeparator)!=1||r.FirstSeparator[0]!=Tick{
  t.Fatalf("wrong minimal trace witness: %+v",r)
 }
}
func TestPrivateStateProbeBreaksOriginalObservation(t *testing.T){
 if !EqUpTo(3,Silent(),false,Silent(),true){t.Fatal("silent states unexpectedly observable")}
 if Silent().Run(false,nil)==Silent().Run(true,nil){t.Fatal("state probe did not distinguish empty word")}
}
func TestIndependentProductExhaustiveBounded(t *testing.T){
 n,v:=CheckSmallProducts(2,16)
 if n==0||v!=0{t.Fatalf("product congruence finite check cases=%d violations=%d",n,v)}
 t.Logf("MATH1_BOUNDED_PRODUCT_CASES=%d VIOLATIONS=%d",n,v)
}
func TestTraceDepthFiltrationBounded(t *testing.T){
 ms:=AllMachines(16)
 for _,a:=range ms{for _,b:=range ms{
  for _,sa:=range []bool{false,true}{for _,sb:=range []bool{false,true}{
   for k:=0;k<3;k++{
    if EqUpTo(k+1,a,sa,b,sb) && !EqUpTo(k,a,sa,b,sb){t.Fatal("antitonicity counterexample")}
   }
  }}
 }}
}
