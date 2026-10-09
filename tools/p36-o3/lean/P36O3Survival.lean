import Init

/-!
P36-O3. Classical indistinguishable-state obstruction.
This is an exact lemma about functions, NOT a theorem that any arbitrary
Go source actually discards all closure identity. The native original-Go
ERASE/RETAIN treatments separately check that source premise.
-/

namespace EvoNOMOS.P36

universe u v w

theorem erased_history_cannot_be_reconstructed_for_two_answers
    {History : Type u} {Snapshot : Type v} {Answer : Type w}
    (erase : History → Snapshot)
    (required : History → Answer)
    (h₁ h₂ : History)
    (same_retained_snapshot : erase h₁ = erase h₂)
    (different_required_answers : required h₁ ≠ required h₂) :
    ¬ ∃ restore : Snapshot → Answer,
       restore (erase h₁) = required h₁ ∧
       restore (erase h₂) = required h₂ := by
  intro candidate
  obtain ⟨restore, first, second⟩ := candidate
  have contradiction : required h₁ = required h₂ := by
    calc
      required h₁ = restore (erase h₁) := first.symm
      _ = restore (erase h₂) := congrArg restore same_retained_snapshot
      _ = required h₂ := second
  exact different_required_answers contradiction

-- This lemma applies only if a source-specific observation map really
-- erases the distinguishing history. Public response equivalence alone
-- does not prove equal private Go snapshots, so actual source premises
-- remain a separate empirical and semantic obligation.

end EvoNOMOS.P36
