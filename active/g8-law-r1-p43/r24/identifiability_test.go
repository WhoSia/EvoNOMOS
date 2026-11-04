package r24
import "testing"
// Same initial client output does not identify future authorized repairability.
func TestSameInitialObservationOppositeFutureRepairFeasibility(t *testing.T){
 outputs:=map[string]string{"A0":"200/old","B0":"200/old"}
 if outputs["A0"]!=outputs["B0"]{t.Fatal("initial observations not matched")}
 a:=RepairGraph{Safe:map[string]bool{"A0":true,"A1":true},Goal:map[string]bool{"A1":true},Steps:[]Step{{"A0","A1","app",1}}}
 b:=RepairGraph{Safe:map[string]bool{"B0":true,"B1":true},Goal:map[string]bool{"B1":true}}
 cost,ok,e:=MinimumSafeCost(a,"A0",map[string]bool{"app":true});if e!=nil||!ok||cost!=1{t.Fatalf("A %d %v %v",cost,ok,e)}
 _,ok,e=MinimumSafeCost(b,"B0",map[string]bool{"app":true});if e!=nil||ok{t.Fatalf("B %v %v",ok,e)}
}
func TestDemandRelativeArchitectureCostReversal(t *testing.T){
 a:=RepairGraph{Safe:map[string]bool{"a0":true,"aX":true,"aY":true},Steps:[]Step{{"a0","aX","app",1},{"a0","aY","app",5}}}
 b:=RepairGraph{Safe:map[string]bool{"b0":true,"bX":true,"bY":true},Steps:[]Step{{"b0","bX","app",5},{"b0","bY","app",1}}}
 rights:=map[string]bool{"app":true}
 a.Goal=map[string]bool{"aX":true};b.Goal=map[string]bool{"bX":true}
 ax,ok,e:=MinimumSafeCost(a,"a0",rights);if e!=nil||!ok{t.Fatal(e)}
 bx,ok,e:=MinimumSafeCost(b,"b0",rights);if e!=nil||!ok{t.Fatal(e)}
 a.Goal=map[string]bool{"aY":true};b.Goal=map[string]bool{"bY":true}
 ay,ok,e:=MinimumSafeCost(a,"a0",rights);if e!=nil||!ok{t.Fatal(e)}
 by,ok,e:=MinimumSafeCost(b,"b0",rights);if e!=nil||!ok{t.Fatal(e)}
 if !(ax<bx&&ay>by){t.Fatalf("no reversal X=%d/%d Y=%d/%d",ax,bx,ay,by)}
}
