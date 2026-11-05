package f20audit
import ("errors";"testing")
func TestObserverScopeCannotBeOverstated(t *testing.T){
 for _,c:=range OriginalCohort(){
  if err:=CanSupport(c,SameTestInput);err!=nil{t.Fatal(c.ID,err)}
  if err:=CanSupport(c,EntirePublicAPI);!errors.Is(err,ErrScopePromotion){
   t.Fatalf("%s broad public API scope inferred from single test",c.ID)
  }
  if err:=CanSupport(c,CompleteClientContexts);!errors.Is(err,ErrScopePromotion){
   t.Fatalf("%s full old client coverage inferred from one test",c.ID)
  }
 }
 t.Log("F20_OBSERVER_SCOPE only_exact_native_test_inputs_certified=true")
}
