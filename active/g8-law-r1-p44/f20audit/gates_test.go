package f20audit
import "testing"

func TestHistoricalEvidenceCannotBecomeBlindPrediction(t *testing.T){
 forged:=FuturePredictionReceipt{
  PredictorCommitSHA:"1111111111111111111111111111111111111111",
  PredictorSealedBeforeDemandDisclosure:true,
  IndependentDemandSet:true,
  SourceAndRightsSealedBeforeDisclosure:true,
  FullOriginalClientObserverDefined:true,
  ResultsNotReadBeforePrediction:true,
 }
 for _,c:=range OriginalCohort(){
  got:=Grade(c,true,forged)
  if got!=HistoricalReplay{t.Fatalf("history leak upgraded to prediction: %s %v",c.ID,got)}
  if got:=Grade(c,false,forged);got!=MetadataOnly{t.Fatalf("unverified original log upgraded: %s %v",c.ID,got)}
 }
 t.Log("F20_LEAKAGE_GATE three_retrospective_cases_no_prospective_claim=true")
}
func TestStrictFuturePredictionRequirementsConjunctive(t *testing.T){
 c:=OriginalCohort()[0];c.SubjectDisclosedBeforeOracle=false
 r:=FuturePredictionReceipt{
  PredictorCommitSHA:"1111111111111111111111111111111111111111",
  PredictorSealedBeforeDemandDisclosure:true,
  IndependentDemandSet:true,
  SourceAndRightsSealedBeforeDisclosure:true,
  FullOriginalClientObserverDefined:true,
  ResultsNotReadBeforePrediction:true,
 }
 if Grade(c,true,r)!=ProspectiveHeldOut{t.Fatal("fully stipulated future conditions incorrectly rejected")}
 r.IndependentDemandSet=false
 if Grade(c,true,r)==ProspectiveHeldOut{t.Fatal("demand leakage accepted")}
 r.IndependentDemandSet=true;r.ResultsNotReadBeforePrediction=false
 if Grade(c,true,r)==ProspectiveHeldOut{t.Fatal("result leakage accepted")}
 // A supplied boolean truth claim is an input, not proof its provenance is genuine.
}
