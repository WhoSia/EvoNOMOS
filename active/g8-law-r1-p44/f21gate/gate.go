package f21gate

import (
 "errors"
 "fmt"
 "regexp"
 "time"
)

// Grade is provenance eligibility, never predictive accuracy or source safety.
type Grade string
const (
 Historical Grade = "C3_HISTORICAL"
 Backtest Grade = "C4_CHRONOLOGICAL_BACKTEST"
 ProspectiveEligible Grade = "C5_PROSPECTIVE_ELIGIBLE_ONLY"
)
type Receipt struct {
 Project string
 BaselineTreeSHA string
 PredictionID string
 PredictorSourceSHA string
 SelectorID string
 PredictionSealedAt time.Time
 DemandDisclosedAt time.Time
 DemandCreatedAt time.Time
 SourceSeenAt time.Time
 DemandSubjectSeenBeforeSeal bool
 PatchOrOutcomeSeenBeforeSeal bool
 IndependentSelectorVerified bool
 BaselineBuildVerified bool
 RightsVerified bool
 OldClientContractFrozen bool
 ClassicalCompetitorFrozen bool
 LiveFutureDemand bool
}
var sha40=regexp.MustCompile(`^[0-9a-f]{40}$`)
// Classify rejects claim promotion from public historical issues and unsealed baselines.
// Receipt fields are claims; this function does not independently authenticate a seal.
func Classify(r Receipt) (Grade,error) {
 if r.Project=="" || r.PredictionID=="" || r.SelectorID=="" { return Historical,errors.New("missing provenance identity") }
 if !sha40.MatchString(r.BaselineTreeSHA) || !sha40.MatchString(r.PredictorSourceSHA) { return Historical,errors.New("invalid pinned SHA") }
 if r.PredictionSealedAt.IsZero() || r.DemandDisclosedAt.IsZero() || r.SourceSeenAt.IsZero() || r.DemandCreatedAt.IsZero() { return Historical,errors.New("missing UTC chronology") }
 if r.SourceSeenAt.After(r.PredictionSealedAt) {return Historical,errors.New("baseline observed after prediction seal")}
 if r.DemandSubjectSeenBeforeSeal || r.PatchOrOutcomeSeenBeforeSeal || !r.PredictionSealedAt.Before(r.DemandDisclosedAt) {return Historical,nil}
 if !r.LiveFutureDemand || !r.PredictionSealedAt.Before(r.DemandCreatedAt) {return Backtest,nil}
 if !(r.IndependentSelectorVerified && r.BaselineBuildVerified && r.RightsVerified && r.OldClientContractFrozen && r.ClassicalCompetitorFrozen) {return Backtest,nil}
 if !r.DemandCreatedAt.Before(r.DemandDisclosedAt) {return Historical,fmt.Errorf("inconsistent demand creation/disclosure chronology")}
 return ProspectiveEligible,nil
}
