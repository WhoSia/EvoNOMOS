package formal
import "testing"
func TestCompleteThreeBitSourceEditLattice(t *testing.T){
 for s:=uint8(0);s<8;s++{for goal:=uint8(0);goal<8;goal++{for rights:=uint8(0);rights<8;rights++{
  got,ok:=CostFromState(s,goal,rights)
  missing:=goal &^ s;wantOK:=missing &^ rights==0
  if ok!=wantOK{t.Fatalf("s=%03b goal=%03b rights=%03b feasible=%v want=%v",s,goal,rights,ok,wantOK)}
  if ok{want:=0;for b:=uint8(1);b<8;b<<=1{if missing&b!=0{want++}};if got!=want{t.Fatalf("cost s=%b goal=%b rights=%b got=%d want=%d",s,goal,rights,got,want)}}
 }}}
}
func TestSyntheticCostLedgerPredeclared(t *testing.T){for n:=0;n<=3;n++{a,b:=PredictedCost(n);if a!=n||b!=3+n{t.Fatalf("n=%d a=%d b=%d",n,a,b)}}}
func TestInvalidRightsAreRejected(t *testing.T){if _,ok:=CostFromState(0,1,8);ok{t.Fatal("unknown right accepted")}}
