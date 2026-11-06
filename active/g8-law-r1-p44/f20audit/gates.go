package f20audit

type EvidenceGrade string
const (
 MetadataOnly EvidenceGrade="C1_GIT_METADATA"
 HistoricalReplay EvidenceGrade="C3_ORIGINAL_GO_PARENT_POST_REPRODUCED"
 ProspectiveHeldOut EvidenceGrade="C5_GENUINELY_PRE_REVEAL_PREDICTION"
)
type FuturePredictionReceipt struct{
 PredictorCommitSHA string
 PredictorSealedBeforeDemandDisclosure bool
 IndependentDemandSet bool
 SourceAndRightsSealedBeforeDisclosure bool
 FullOriginalClientObserverDefined bool
 ResultsNotReadBeforePrediction bool
}

// Grade never upgrades historical regression reproduction into a prediction.
// C3 assumes an external verifier checked the matching original GitHub CI job;
// one boolean receipt here does not itself authenticate the GitHub service.
func Grade(c OriginalCase, originalJobLogsVerified bool, future FuturePredictionReceipt)EvidenceGrade {
 if c.Validate()!=nil{return MetadataOnly}
 if !originalJobLogsVerified{return MetadataOnly}
 if c.SubjectDisclosedBeforeOracle{return HistoricalReplay}
 if !hexCommit.MatchString(future.PredictorCommitSHA)||
 !future.PredictorSealedBeforeDemandDisclosure||
 !future.IndependentDemandSet||
 !future.SourceAndRightsSealedBeforeDisclosure||
 !future.FullOriginalClientObserverDefined||
 !future.ResultsNotReadBeforePrediction{
  return HistoricalReplay
 }
 return ProspectiveHeldOut
}
