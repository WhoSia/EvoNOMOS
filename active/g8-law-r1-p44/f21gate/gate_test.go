package f21gate
import (
 "strings"
 "testing"
 "time"
)
func day(s string) time.Time {t,e:=time.Parse(time.RFC3339,s);if e!=nil {panic(e)};return t}
func valid() Receipt {return Receipt{Project:"synthetic-independent",BaselineTreeSHA:strings.Repeat("a",40),PredictorSourceSHA:strings.Repeat("b",40),PredictionID:"sealed-001",SelectorID:"external-001",SourceSeenAt:day("2026-11-05T08:00:00Z"),PredictionSealedAt:day("2026-11-05T09:00:00Z"),DemandCreatedAt:day("2026-11-06T09:00:00Z"),DemandDisclosedAt:day("2026-11-06T10:00:00Z"),IndependentSelectorVerified:true,BaselineBuildVerified:true,RightsVerified:true,OldClientContractFrozen:true,ClassicalCompetitorFrozen:true,LiveFutureDemand:true}}
func TestProspectiveOnlyEligibilityNotAccuracy(t *testing.T){r:=valid();g,e:=Classify(r);if e!=nil||g!=ProspectiveEligible {t.Fatalf("%v %v",g,e)}}
func TestKnownIssueSubjectCannotBeProspective(t *testing.T){r:=valid();r.DemandSubjectSeenBeforeSeal=true;g,_:=Classify(r);if g!=Historical {t.Fatal(g)}}
func TestPatchLeakCannotBeProspective(t *testing.T){r:=valid();r.PatchOrOutcomeSeenBeforeSeal=true;g,_:=Classify(r);if g!=Historical {t.Fatal(g)}}
func TestRevealedBeforeSealCannotBeProspective(t *testing.T){r:=valid();r.DemandDisclosedAt=r.PredictionSealedAt;r.DemandCreatedAt=r.PredictionSealedAt.Add(-time.Hour);g,_:=Classify(r);if g!=Historical{t.Fatal(g)}}
func TestArchivedDemandIsBacktest(t *testing.T){r:=valid();r.DemandCreatedAt=day("2024-01-01T00:00:00Z");r.LiveFutureDemand=false;g,_:=Classify(r);if g!=Backtest{t.Fatal(g)}}
func TestAbsentIndependentSelectorIsNotProspective(t *testing.T){r:=valid();r.IndependentSelectorVerified=false;g,_:=Classify(r);if g!=Unverified{t.Fatal(g)}}
func TestAbsentRightsIsNotProspective(t *testing.T){r:=valid();r.RightsVerified=false;g,_:=Classify(r);if g!=Unverified{t.Fatal(g)}}
func TestUnfrozenOldClientIsNotProspective(t *testing.T){r:=valid();r.OldClientContractFrozen=false;g,_:=Classify(r);if g!=Unverified{t.Fatal(g)}}
func TestUnfrozenRivalIsNotProspective(t *testing.T){r:=valid();r.ClassicalCompetitorFrozen=false;g,_:=Classify(r);if g!=Unverified{t.Fatal(g)}}
func TestInvalidSHARejected(t *testing.T){r:=valid();r.BaselineTreeSHA="bad";_,e:=Classify(r);if e==nil {t.Fatal("accepted invalid SHA")}}
func TestSourceAfterPredictionRejected(t *testing.T){r:=valid();r.SourceSeenAt=day("2026-11-05T11:00:00Z");_,e:=Classify(r);if e==nil{t.Fatal("accepted reverse chronology")}}
func TestMissingReceiptRejected(t *testing.T){r:=valid();r.PredictionID="";_,e:=Classify(r);if e==nil{t.Fatal("accepted missing ID")}}
func TestInvalidDemandChronologyRejected(t *testing.T){r:=valid();r.DemandCreatedAt=r.DemandDisclosedAt.Add(time.Hour);_,e:=Classify(r);if e==nil{t.Fatal("accepted impossible chronology")}}

func TestMissingBuildIsHold(t *testing.T){r:=valid();r.BaselineBuildVerified=false;g,_:=Classify(r);if g!=Unverified{t.Fatal(g)}}
func TestCreatedAfterDisclosedRejectedEvenForBacktest(t *testing.T){r:=valid();r.LiveFutureDemand=false;r.DemandCreatedAt=r.DemandDisclosedAt.Add(time.Hour);_,e:=Classify(r);if e==nil{t.Fatal("accepted impossible chronology")}}

func TestPublicIssueCreationEqualsDisclosure(t *testing.T){r:=valid();r.DemandDisclosedAt=r.DemandCreatedAt;g,e:=Classify(r);if e!=nil||g!=ProspectiveEligible{t.Fatalf("ordinary public GitHub issue: %v %v",g,e)}}
func TestFutureDemandFalseLiveFlagHolds(t *testing.T){r:=valid();r.LiveFutureDemand=false;g,e:=Classify(r);if e!=nil||g!=Unverified{t.Fatalf("future demand cannot become retrospective: %v %v",g,e)}}
