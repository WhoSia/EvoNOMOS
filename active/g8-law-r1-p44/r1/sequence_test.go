package r1

import "testing"

// This independent-source pair is a intentionally predicted classical tie:
// both systems receive only application-owned route insertion rights.
// Stagewise tests check all old inputs and all previously added demands.
func TestStagewiseAuthorizedTwoDemandTie(t *testing.T){
 for stage:=0;stage<=2;stage++{
  a,b:=Standard(stage),FullChi(stage)
  misses,e:=Compare(a,b,Broad());if e!=nil||len(misses)>0{t.Fatalf("stage=%d original protected mismatch %v %v",stage,misses,e)}
  goals:=[]struct{path,want string}{}
  if stage>=1{goals=append(goals,struct{path,want string}{"/lookup/alpha","lookup:alpha"})}
  if stage>=2{goals=append(goals,struct{path,want string}{"/lookup/alpha/meta","meta:alpha"})}
  for _,g:=range goals{
   p:=Probe{"GET",g.path}
   x,e:=ObserveWire(a,p);if e!=nil{t.Fatal(e)}
   y,e:=ObserveWire(b,p);if e!=nil{t.Fatal(e)}
   if x.Status!=200||y.Status!=200||x.Body!=g.want||y.Body!=g.want{t.Fatalf("stage=%d goal=%s std=%+v chi=%+v",stage,g.path,x,y)}
  }
  t.Logf("SAFE_STAGE stage=%d protected=%d added_goals=%d standard_total_synthetic=%d chi_total_synthetic=%d",stage,len(Broad()),len(goals),stage,3+stage)
 }
}
