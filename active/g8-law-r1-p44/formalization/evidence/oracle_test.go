package evidence
import ("errors";"testing")
func TestFiniteSafeOnlyWithSoundOverapproximation(t *testing.T){
 actual:=[]Trace{{"a",true},{"b",true}}
 under:=Evidence{Under:[]Trace{{"a",true}},UnderCertified:true}
 if e:=VerifyFiniteCoverage(actual,under);e!=nil{t.Fatal(e)}
 if v,_:=Judge(under);v!=Unknown{t.Fatalf("one successful trace must not prove safety: %s",v)}
 over:=Evidence{Over:[]Trace{{"a",true},{"b",true},{"extra",true}},OverCertified:true}
 if e:=VerifyFiniteCoverage(actual,over);e!=nil{t.Fatal(e)}
 if v,_:=Judge(over);v!=Safe{t.Fatalf("sound overapprox must prove safety: %s",v)}
}
func TestReachableBadTraceProvesViolation(t *testing.T){
 actual:=[]Trace{{"ok",true},{"bad",false}}
 under:=Evidence{Under:[]Trace{{"bad",false}},UnderCertified:true}
 if e:=VerifyFiniteCoverage(actual,under);e!=nil{t.Fatal(e)}
 if v,_:=Judge(under);v!=Unsafe{t.Fatalf("reachable bad witness denied: %s",v)}
 t.Log("INCORRECTNESS_WITNESS proven_unsafe=true")
}
func TestPhantomBugWitnessRejected(t *testing.T){
 real:=[]Trace{{"ok",true}}
 under:=Evidence{Under:[]Trace{{"unreal",false}},UnderCertified:true}
 if e:=VerifyFiniteCoverage(real,under);!errors.Is(e,ErrFalseUnder){t.Fatalf("false reachable error admitted: %v",e)}
}
func TestHiddenBadExecutionInvalidatesOverapproxSafety(t *testing.T){
 real:=[]Trace{{"ok",true},{"bad",false}}
 fake:=Evidence{Over:[]Trace{{"ok",true}},OverCertified:true}
 if e:=VerifyFiniteCoverage(real,fake);!errors.Is(e,ErrFalseOver){t.Fatalf("hidden bad path not detected: %v",e)}
 if v,_:=Judge(Evidence{Over:fake.Over});v!=Unknown{t.Fatalf("unproven completeness must be unknown: %s",v)}
 t.Log("SOURCE_OBSERVER_COMPLETENESS missing_bad_trace_detected=true")
}
func TestAuthorizedRepairPathNeedsAllCheckpointProofs(t *testing.T){
 cert:=func(id string,good bool)Revision{
  e:=Evidence{Over:[]Trace{{id,good}},OverCertified:true}
  return Revision{ID:id,Evidence:e,GoalHolds:id=="goal"}
 }
 states:=map[string]Revision{"start":cert("start",true),"mid":cert("mid",true),"goal":cert("goal",true)}
 edits:=[]Edit{{"start","mid",true},{"mid","goal",true}}
 if v,e:=CheckPathProof(states,edits,[]string{"start","mid","goal"});e!=nil||v!=Safe{t.Fatalf("expected safe path %s %v",v,e)}
 mid:=states["mid"];mid.Evidence=Evidence{Under:[]Trace{{"bad",false}},UnderCertified:true};states["mid"]=mid
 if v,_:=CheckPathProof(states,edits,[]string{"start","mid","goal"});v!=Unsafe{t.Fatalf("unsafe intermediate allowed: %s",v)}
 mid.Evidence=Evidence{Under:[]Trace{{"good",true}},UnderCertified:true};states["mid"]=mid
 if v,_:=CheckPathProof(states,edits,[]string{"start","mid","goal"});v!=Unknown{t.Fatalf("absence of universal proof wrongly accepted: %s",v)}
 states["mid"]=cert("mid",true)
 edits[1].Authorized=false
 if v,_:=CheckPathProof(states,edits,[]string{"start","mid","goal"});v!=Unknown{t.Fatalf("unauthorized edit accepted: %s",v)}
}
func TestConflictingEvidenceCannotBothProve(t *testing.T){
 e:=Evidence{Under:[]Trace{{"bad",false}},UnderCertified:true,Over:[]Trace{{"good",true}},OverCertified:true}
 if _,err:=Judge(e);!errors.Is(err,ErrConflict){t.Fatal(err)}
}
