// Package costbounds provides a finite reference test for the classical
// lower/upper repair-cost sandwich. It is NOT a source-level Go soundness proof.
package costbounds

import (
 "errors"
 "math"
)

var (
 ErrUnsoundMapping = errors.New("a concrete feasible repair is not represented with non-increasing abstract cost")
 ErrInvalidCost = errors.New("negative repair cost")
 ErrInvalidWitness = errors.New("witness is unauthorized or fails declared old-client contract")
)

// Concrete represents an independently validated, finite-model safe source
// repair path. AbstractID is the identity of its abstract image.
type Concrete struct {
 ID string
 AbstractID string
 Cost int
}

// VerifyFiniteImage checks the inclusion/cost premise in a FINITE REFERENCE
// model where every concrete admissible path is supplied. Production soundness
// requires an independent proof that this input enumerates ALL concrete paths.
func VerifyFiniteImage(concrete []Concrete, abstract map[string]int) error {
 for _,cost := range abstract {
  if cost<0 { return ErrInvalidCost }
 }
 for _,path := range concrete {
  if path.Cost<0 { return ErrInvalidCost }
  a,ok := abstract[path.AbstractID]
  if !ok || a>path.Cost { return ErrUnsoundMapping }
 }
 return nil
}

// LowerBound returns the minimum abstract candidate cost.
// Empty abstract set convention is +infinity, represented as math.MaxInt.
func LowerBound(abstract map[string]int)(int,error) {
 min:=math.MaxInt
 for _,cost:=range abstract {
  if cost<0 {return 0,ErrInvalidCost}
  if cost<min {min=cost}
 }
 return min,nil
}

// UpperWitness validates the externally asserted permission and staged
// old-contract predicates for the supplied ONE concrete path.
func UpperWitness(w Concrete, authorized,stagewiseSafe,fulfillsDemand bool)(int,error){
 if w.Cost<0{return 0,ErrInvalidCost}
 if !authorized||!stagewiseSafe||!fulfillsDemand{return 0,ErrInvalidWitness}
 return w.Cost,nil
}
