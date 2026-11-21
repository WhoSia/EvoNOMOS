package costbounds

import (
 "errors"
 "testing"
)

func TestClassicalCEGARRepairCostSandwich(t *testing.T){
 concrete:=[]Concrete{{ID:"safe-4",AbstractID:"real",Cost:4}}
 levels:=[]map[string]int{
  {"spurious-1":1,"spurious-2":2,"real":4},
  {"spurious-2":2,"real":4},
  {"real":4},
 }
 upper,e:=UpperWitness(concrete[0],true,true,true)
 if e!=nil||upper!=4 {t.Fatal(e,upper)}
 want:=[]int{1,2,4}
 previous:=0
 for i,a:=range levels {
  if e=VerifyFiniteImage(concrete,a);e!=nil{t.Fatalf("refinement %d unsound: %v",i,e)}
  lower,e:=LowerBound(a)
  if e!=nil||lower!=want[i]||lower>upper||lower<previous{t.Fatalf("level=%d L=%d U=%d error=%v",i,lower,upper,e)}
  t.Logf("CLASSICAL_BOUND level=%d lower=%d upper=%d",i,lower,upper)
  previous=lower
 }
 if previous!=upper{t.Fatal("final bounds did not meet")}
}
func TestUnsoundAbstractionDetected(t *testing.T){
 concrete:=[]Concrete{{ID:"safe-4",AbstractID:"real",Cost:4}}
 if e:=VerifyFiniteImage(concrete,map[string]int{"spurious-1":1});!errors.Is(e,ErrUnsoundMapping){t.Fatalf("discarded concrete image accepted: %v",e)}
 if e:=VerifyFiniteImage(concrete,map[string]int{"real":5});!errors.Is(e,ErrUnsoundMapping){t.Fatalf("overpriced mapping accepted: %v",e)}
}
func TestOldClientAndRightViolationsRejectUpperBound(t *testing.T){
 w:=Concrete{ID:"unsafe",AbstractID:"a",Cost:1}
 for _,c:=range []struct{a,s,d bool}{{false,true,true},{true,false,true},{true,true,false}}{
  _,e:=UpperWitness(w,c.a,c.s,c.d)
  if !errors.Is(e,ErrInvalidWitness){t.Fatalf("invalid witness accepted %+v err=%v",c,e)}
 }
}
func TestEmptyAbstractSetNotClaimedConcreteFeasible(t *testing.T){
 l,e:=LowerBound(map[string]int{})
 if e!=nil||l<1000000{t.Fatalf("empty lower %d %v",l,e)}
 // A proof that no concrete paths exist additionally needs a SOUND, COMPLETE
 // image argument; an empty heuristic search result by itself is not proof.
 if e:=VerifyFiniteImage([]Concrete{{"p","p",4}},map[string]int{});!errors.Is(e,ErrUnsoundMapping){t.Fatal(e)}
}
