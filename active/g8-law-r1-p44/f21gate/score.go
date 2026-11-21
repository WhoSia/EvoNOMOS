package f21gate
import "fmt"
// All predictions are about authorized safe repair under a fixed edit/observer scope.
type Decision string
const (
 PredictSafe Decision = "SAFE"
 PredictImpossible Decision = "IMPOSSIBLE"
 Abstain Decision = "ABSTAIN"
)
type Outcome string
const (
 VerifiedSafe Outcome = "SAFE_REPAIR_WITNESSED"
 VerifiedImpossible Outcome = "IMPOSSIBILITY_CERTIFIED"
 Unresolved Outcome = "UNRESOLVED"
)
type Evaluation struct {Prediction Decision;Truth Outcome}
type Score struct {Adjudicated int;Unresolved int;SafeClaims int;FalseSafe int;FalseImpossible int;CorrectDecisions int;Abstentions int}
// Absence of a repair witness never counts as an impossibility proof.
func ScoreEvaluations(rows []Evaluation)(Score,error){
 var out Score
 for i,r:=range rows {
  if r.Prediction!=PredictSafe && r.Prediction!=PredictImpossible && r.Prediction!=Abstain {return Score{},fmt.Errorf("row %d: unknown prediction",i)}
  if r.Truth!=VerifiedSafe && r.Truth!=VerifiedImpossible && r.Truth!=Unresolved {return Score{},fmt.Errorf("row %d: unknown outcome",i)}
  if r.Truth==Unresolved {out.Unresolved++;continue}
  out.Adjudicated++
  if r.Prediction==Abstain {out.Abstentions++;continue}
  if r.Prediction==PredictSafe {out.SafeClaims++}
  if (r.Prediction==PredictSafe && r.Truth==VerifiedSafe)||(r.Prediction==PredictImpossible && r.Truth==VerifiedImpossible){out.CorrectDecisions++}
  if r.Prediction==PredictSafe && r.Truth==VerifiedImpossible {out.FalseSafe++}
  if r.Prediction==PredictImpossible && r.Truth==VerifiedSafe {out.FalseImpossible++}
 }
 return out,nil
}
