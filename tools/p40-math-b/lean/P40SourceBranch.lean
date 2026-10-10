import P40IssueSimulation

/- P40-MATH-B-P6: source-slice-to-abstract logic bridge.
   The two imperative statements are extracted from original Echo Go AST and
   separately *executed* in Go against eight native Echo states; the Lean
   definition below is a translation of their bounded Boolean behavior.
   Theorem scope: this translation and declared HEAD model, NOT full-Go
   operational semantics, unspecified router fallbacks, or maintainer rights. -/
namespace P40SourceBranch

open P40IssueSimulation

def extractedHEAD (hasHead hasGet autoHEAD : Bool) : HeadTarget :=
  let r : HeadTarget := if hasHead then .direct else .unavailable
  if autoHEAD && r == .unavailable
  then if hasGet then .fallback else .unavailable
  else r

theorem extracted_head_matches_declared_semantics
    (s : NativeSourceState) :
    extractedHEAD s.directHead s.registeredGet s.autoHead =
      sourceDispatch s := by
  cases s with
  | mk h g a n rev =>
      cases h <;> cases g <;> cases a <;>
        decide

theorem extracted_head_matches_boundary (s : NativeSourceState) :
    extractedHEAD s.directHead s.registeredGet s.autoHead =
      abstractDispatch (abstract s) := by
  rw [extracted_head_matches_declared_semantics, head_dispatch_refines]

theorem no_get_side_effect_from_explicit_head
    (get auto : Bool) :
    extractedHEAD true get auto = .direct := by
  cases get <;> cases auto <;> decide

theorem no_handler_if_fallback_is_disabled
    (auto : Bool) :
    extractedHEAD false false auto = .unavailable := by
  cases auto <;> decide

theorem baseline_fallback_invokes_get :
    extractedHEAD false true true = .fallback := by decide

theorem original_bounded_requirement_fails :
    extractedHEAD false true true ≠ .direct := by decide

theorem exactly_one_of_three_single_bit_repairs_satisfies_head_without_get :
    extractedHEAD true true true = .direct ∧
      extractedHEAD false false true ≠ .direct ∧
      extractedHEAD false true false ≠ .direct := by decide

theorem minimal_repair_requires_explicit_handler
    (head get auto : Bool)
    (oneFlip :
      (head, get, auto) = (true, true, true) ∨
      (head, get, auto) = (false, false, true) ∨
      (head, get, auto) = (false, true, false))
    (safe : extractedHEAD head get auto = .direct) :
    (head, get, auto) = (true, true, true) := by
  rcases oneFlip with first | second | third
  · exact first
  · have hh : head = false ∧ get = false ∧ auto = true := by
      rcases second with ⟨rfl, rfl, rfl⟩
      exact ⟨rfl, rfl, rfl⟩
    rcases hh with ⟨rfl,rfl,rfl⟩
    contradiction
  · have hh : head = false ∧ get = true ∧ auto = false := by
      rcases third with ⟨rfl, rfl, rfl⟩
      exact ⟨rfl, rfl, rfl⟩
    rcases hh with ⟨rfl,rfl,rfl⟩
    contradiction

/- The route-identity countertrace observed in Echo issue #2619 is
   explicitly OUTSIDE the extracted HEAD case and this minimal repair
   certificate. No lemma here claims its repair, or a new general OO law. -/

end P40SourceBranch
