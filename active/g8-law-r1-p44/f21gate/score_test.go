package f21gate
import "testing"
func TestScoreCountsOnlyAdjudicated(t *testing.T){
 got,e:=ScoreEvaluations([]Evaluation{{PredictSafe,VerifiedImpossible},{PredictImpossible,VerifiedSafe},{PredictSafe,VerifiedSafe},{PredictImpossible,VerifiedImpossible},{Abstain,VerifiedSafe},{PredictSafe,Unresolved}})
 if e!=nil{t.Fatal(e)}
 want:=Score{Adjudicated:5,Unresolved:1,SafeClaims:2,FalseSafe:1,FalseImpossible:1,CorrectDecisions:2,Abstentions:1}
 if got!=want{t.Fatalf("got %+v want %+v",got,want)}
}
func TestUnknownDoesNotCertifyImpossibility(t *testing.T){got,e:=ScoreEvaluations([]Evaluation{{PredictImpossible,Unresolved}});if e!=nil||got.Adjudicated!=0||got.CorrectDecisions!=0{t.Fatalf("%+v %v",got,e)}}
func TestInvalidPredictionRejected(t *testing.T){_,e:=ScoreEvaluations([]Evaluation{{Decision("CERTAIN"),VerifiedSafe}});if e==nil{t.Fatal("unknown prediction accepted")}}
func TestInvalidTruthRejected(t *testing.T){_,e:=ScoreEvaluations([]Evaluation{{PredictSafe,Outcome("NOT_FOUND")}});if e==nil{t.Fatal("unproved impossibility accepted")}}
func TestEmptyCohortDoesNotProduceRate(t *testing.T){s,e:=ScoreEvaluations(nil);if e!=nil||s.Adjudicated!=0{t.Fatalf("%+v %v",s,e)}}
