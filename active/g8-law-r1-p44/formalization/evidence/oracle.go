// Package evidence is a finite classical reference court for over- and
// under-approximate source-observation proofs, not a source soundness engine.
package evidence
import ("errors";"sort")
type Verdict string
const ( Safe Verdict="PROVED_SAFE"; Unsafe Verdict="PROVED_VIOLATION"; Unknown Verdict="UNKNOWN" )
var ErrFalseUnder=errors.New("under-approximation contains unrealizable trace")
var ErrFalseOver=errors.New("over-approximation omits realizable trace")
var ErrConflict=errors.New("conflicting safe and violation certificates")
type Trace struct{ Label string; ContractHolds bool }
type Evidence struct{ Under,Over []Trace; UnderCertified,OverCertified bool }
// VerifyFiniteCoverage uses full ground truth in a SMALL REFERENCE MODEL.
// It cannot certify real-source provenance or completeness by itself.
func VerifyFiniteCoverage(real []Trace,e Evidence)error{
 actual:=map[string]bool{}
 for _,x:=range real{actual[x.Label]=x.ContractHolds}
 if e.UnderCertified {for _,x:=range e.Under{
  hold,ok:=actual[x.Label];if !ok||hold!=x.ContractHolds{return ErrFalseUnder}
 }}
 if e.OverCertified{
  over:=map[string]bool{}
  for _,x:=range e.Over{over[x.Label]=x.ContractHolds}
  for _,x:=range real{if h,ok:=over[x.Label];!ok||h!=x.ContractHolds{return ErrFalseOver}}
 }
 return nil
}
// Judge accepts proof-status flags only if their external proof obligations
// have been discharged. Flags MUST NOT be sourced from passing sample tests.
func Judge(e Evidence)(Verdict,error){
 fail:=false
 if e.UnderCertified {for _,x:=range e.Under{if !x.ContractHolds{fail=true}}}
 allSafe:=e.OverCertified
 if allSafe{for _,x:=range e.Over{if !x.ContractHolds{allSafe=false;break}}}
 if fail&&allSafe{return Unknown,ErrConflict}
 if fail{return Unsafe,nil}
 if allSafe{return Safe,nil}
 return Unknown,nil
}
type Revision struct{ ID string; Evidence Evidence; GoalHolds bool }
type Edit struct{ From,To string; Authorized bool }
// CheckPathProof requires a universal safety proof at EVERY release checkpoint,
// plus a declared goal. Any UNKNOWN or witnessed violating checkpoint rejects.
func CheckPathProof(states map[string]Revision, edits []Edit, path []string)(Verdict,error){
 if len(path)==0{return Unknown,nil}
 for i,id:=range path{
  state,ok:=states[id];if !ok{return Unknown,nil}
  v,e:=Judge(state.Evidence);if e!=nil{return Unknown,e}
  if v!=Safe{return v,nil}
  if i==0{continue}
  exists:=false
  for _,t:=range edits{if t.From==path[i-1]&&t.To==id&&t.Authorized{exists=true}}
  if !exists{return Unknown,nil}
 }
 if !states[path[len(path)-1]].GoalHolds{return Unknown,nil}
 return Safe,nil
}
// StableLabels assists deterministic finite countermodel reporting.
func StableLabels(traces []Trace)[]string{out:=make([]string,0,len(traces));for _,t:=range traces{out=append(out,t.Label)};sort.Strings(out);return out}
