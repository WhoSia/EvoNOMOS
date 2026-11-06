package f21gate

import (
 "errors"
 "time"
)

// ForecastMode separates predicting a still-unseen demand from predicting its
// repair feasibility once disclosed but BEFORE any repair outcome is revealed.
type ForecastMode string
const (
 DemandBlind ForecastMode = "DEMAND_BLIND"
 DemandConditional ForecastMode = "DEMAND_CONDITIONAL_REPAIR"
)
type ForecastReceipt struct {
 Mode ForecastMode
 BaselineTreeSHA string
 PredictorSourceSHA string
 BaselineObservedAt time.Time
 PredictorFrozenAt time.Time
 DemandCreatedAt time.Time
 DemandDisclosedAt time.Time
 PredictionSealedAt time.Time
 OutcomeDisclosedAt time.Time // zero when still unknown
 IssueContentSeenBeforePrediction bool
 OutcomeSeenBeforePrediction bool
 SealExternallyVerified bool
 BuildVerified bool
 RightsVerified bool
 OldClientContractFrozen bool
 ClassicalCompetitorFrozen bool
}
// EvaluateForecast concerns evidence eligibility, NEVER predictive correctness.
// Caller-provided flags and timestamps alone are not external attestation.
func EvaluateForecast(r ForecastReceipt)(Grade,error){
 if r.Mode!=DemandBlind && r.Mode!=DemandConditional {return Unverified,errors.New("unknown forecast mode")}
 if !sha40.MatchString(r.BaselineTreeSHA)||!sha40.MatchString(r.PredictorSourceSHA){return Unverified,errors.New("invalid source identifier")}
 if r.BaselineObservedAt.IsZero()||r.PredictorFrozenAt.IsZero()||r.DemandCreatedAt.IsZero()||r.DemandDisclosedAt.IsZero()||r.PredictionSealedAt.IsZero(){return Unverified,errors.New("incomplete clock evidence")}
 if r.DemandCreatedAt.After(r.DemandDisclosedAt){return Unverified,errors.New("creation after disclosure")}
 if r.BaselineObservedAt.After(r.PredictorFrozenAt){return Unverified,errors.New("source inspected after policy freeze")}
 if r.PredictionSealedAt.Before(r.PredictorFrozenAt){return Unverified,errors.New("prediction sealed before model freeze")}
 if !r.PredictorFrozenAt.Before(r.DemandCreatedAt){return Backtest,nil}
 if r.OutcomeSeenBeforePrediction||(!r.OutcomeDisclosedAt.IsZero()&&!r.PredictionSealedAt.Before(r.OutcomeDisclosedAt)){return Historical,nil}
 if r.Mode==DemandBlind {
   if r.IssueContentSeenBeforePrediction||!r.PredictionSealedAt.Before(r.DemandCreatedAt){return Historical,nil}
 }else{
   if r.PredictionSealedAt.Before(r.DemandDisclosedAt){return Unverified,errors.New("conditional forecast predates input disclosure")}
 }
 if !r.SealExternallyVerified||!r.BuildVerified||!r.RightsVerified||!r.OldClientContractFrozen||!r.ClassicalCompetitorFrozen{return Unverified,nil}
 return ProspectiveEligible,nil
}
