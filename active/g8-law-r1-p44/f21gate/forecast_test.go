package f21gate
import (
 "strings"
 "testing"
 "time"
)
func fixtureConditional() ForecastReceipt {
 return ForecastReceipt{Mode:DemandConditional,BaselineTreeSHA:strings.Repeat("1",40),PredictorSourceSHA:strings.Repeat("2",40),BaselineObservedAt:day("2026-11-05T08:00:00Z"),PredictorFrozenAt:day("2026-11-05T09:00:00Z"),DemandCreatedAt:day("2026-11-06T09:00:00Z"),DemandDisclosedAt:day("2026-11-06T09:00:00Z"),PredictionSealedAt:day("2026-11-06T10:00:00Z"),SealExternallyVerified:true,BuildVerified:true,RightsVerified:true,OldClientContractFrozen:true,ClassicalCompetitorFrozen:true}
}
func TestConditionalDemandMayBeReadBeforeForecast(t *testing.T){r:=fixtureConditional();r.IssueContentSeenBeforePrediction=true;g,e:=EvaluateForecast(r);if e!=nil||g!=ProspectiveEligible{t.Fatalf("%v %v",g,e)}}
func TestBlindDemandCannotBeRead(t *testing.T){r:=fixtureConditional();r.Mode=DemandBlind;r.IssueContentSeenBeforePrediction=true;g,_:=EvaluateForecast(r);if g!=Historical{t.Fatal(g)}}
func TestBlindPredictionMustPrecedeCreation(t *testing.T){r:=fixtureConditional();r.Mode=DemandBlind;r.PredictionSealedAt=r.PredictorFrozenAt.Add(time.Minute);g,e:=EvaluateForecast(r);if e!=nil||g!=ProspectiveEligible{t.Fatalf("%v %v",g,e)}}
func TestUnknownOutcomeIsNotFailure(t *testing.T){r:=fixtureConditional();r.OutcomeDisclosedAt=time.Time{};g,_:=EvaluateForecast(r);if g!=ProspectiveEligible{t.Fatal(g)}}
func TestLeakedFixIsHistorical(t *testing.T){r:=fixtureConditional();r.OutcomeSeenBeforePrediction=true;g,_:=EvaluateForecast(r);if g!=Historical{t.Fatal(g)}}
func TestMissingExternalSealIsHold(t *testing.T){r:=fixtureConditional();r.SealExternallyVerified=false;g,_:=EvaluateForecast(r);if g!=Unverified{t.Fatal(g)}}
func TestLateModelFreezeIsBacktest(t *testing.T){r:=fixtureConditional();r.PredictorFrozenAt=r.DemandCreatedAt.Add(time.Minute);g,_:=EvaluateForecast(r);if g!=Backtest{t.Fatal(g)}}
func TestPredictionAfterKnownOutcomeIsHistorical(t *testing.T){r:=fixtureConditional();r.OutcomeDisclosedAt=r.PredictionSealedAt;g,_:=EvaluateForecast(r);if g!=Historical{t.Fatal(g)}}
func TestPreDisclosureConditionalRejected(t *testing.T){r:=fixtureConditional();r.PredictionSealedAt=r.DemandDisclosedAt.Add(-time.Minute);g,e:=EvaluateForecast(r);if g!=Unverified||e==nil{t.Fatalf("%v %v",g,e)}}
