import P40IssueSimulation

/- P40-MATH-B-P6 restricted source-branch bridge.
   The same two HEAD-case Go AST statements are separately extracted and
   compiled in Go. Lean checks the declared Boolean translation, not
   equivalence to arbitrary source programs or unknown router paths. -/
namespace P40Bridge

open P40IssueSimulation

def extractedHeadSelector (head get auto : Bool) : HeadTarget :=
  let selected := if head then HeadTarget.direct else HeadTarget.unavailable
  if auto && selected == HeadTarget.unavailable then
    if get then HeadTarget.fallback else HeadTarget.unavailable
  else selected

theorem source_branch_matches_declared_model (s : NativeSourceState) :
    extractedHeadSelector s.directHead s.registeredGet s.autoHead =
      sourceDispatch s := by
  cases s with
  | mk d g a n rev =>
      cases d <;> cases g <;> cases a <;> rfl

theorem source_branch_matches_observation_abstraction
    (s : NativeSourceState) :
    extractedHeadSelector s.directHead s.registeredGet s.autoHead =
      abstractDispatch (abstract s) := by
  rw [source_branch_matches_declared_model, head_dispatch_refines]

theorem bounded_single_bit_repair_certificate :
    extractedHeadSelector false true true = .fallback ∧
    extractedHeadSelector true true true = .direct ∧
    extractedHeadSelector false false true = .unavailable ∧
    extractedHeadSelector false true false = .unavailable := by decide

theorem unique_single_bit_repair
    (h g a : Bool)
    (oneBit :
       (h,g,a) = (true,true,true) ∨
       (h,g,a) = (false,false,true) ∨
       (h,g,a) = (false,true,false))
    (keepsHEADWithoutGETEffect :
       extractedHeadSelector h g a = .direct) :
       (h,g,a) = (true,true,true) := by
  cases h <;> cases g <;> cases a <;>
    simp_all [extractedHeadSelector]

theorem source_sliced_boundary_simulates_future_HEAD_steps
    (s : NativeSourceState) (n : Nat) :
    abstract (runSource n s) = runAbstract n (abstract s) :=
  head_finite_simulation n s

/- This theory does not certify the full Echo routing tree. The
   Echo #2619 wrong-handler countertrace is deliberately OUTSIDE the
   HEAD-case domain and must be transferred to P41 unresolved. -/
end P40Bridge
