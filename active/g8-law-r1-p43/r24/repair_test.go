package r24
import "testing"
func TestStagewiseSafetyRejectsUnsafeShortcut(t *testing.T){
 g:=RepairGraph{Safe:map[string]bool{"start":true,"unsafe":false,"goal":true},Goal:map[string]bool{"goal":true},
 Steps:[]Step{{"start","unsafe","adapter",1},{"unsafe","goal","adapter",1},{"start","goal","public",4}}}
 cost,ok,err:=MinimumSafeCost(g,"start",map[string]bool{"adapter":true,"public":true})
 if err!=nil||!ok||cost!=4{t.Fatalf("safe cost: %d %v %v",cost,ok,err)}
 _,ok,err=MinimumSafeCost(g,"start",map[string]bool{"adapter":true})
 if err!=nil||ok{t.Fatalf("unsafe shortcut accepted: %v %v",ok,err)}
}
func TestRightsMonotonicityAndClassicalTie(t *testing.T){
 g:=RepairGraph{Safe:map[string]bool{"s":true,"a":true,"b":true,"g":true},Goal:map[string]bool{"g":true},
 Steps:[]Step{{"s","a","A",2},{"a","g","B",1},{"s","b","C",1},{"b","g","B",4}}}
 rs:=[]string{"A","B","C"}
 for p:=0;p<8;p++{for q:=0;q<8;q++{if p&q!=p{continue}
  a,b:=map[string]bool{},map[string]bool{}
  for i,r:=range rs{a[r]=p&(1<<i)!=0;b[r]=q&(1<<i)!=0}
  c1,o1,e1:=MinimumSafeCost(g,"s",a);c2,o2,e2:=MinimumSafeCost(g,"s",b)
  if e1!=nil||e2!=nil||o1&&(!o2||c2>c1){t.Fatalf("rights monotonicity: %b to %b",p,q)}
 }}
}
func TestInvalidCostAndStartRejected(t *testing.T){
 g:=RepairGraph{Safe:map[string]bool{"s":false},Steps:[]Step{{"s","t","A",1}}}
 if _,_,e:=MinimumSafeCost(g,"s",nil);e!=ErrUnsafeStart{t.Fatal(e)}
 g.Safe["s"]=true;g.Steps[0].Cost=-1
 if _,_,e:=MinimumSafeCost(g,"s",nil);e!=ErrInvalidCost{t.Fatal(e)}
}
