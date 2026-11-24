import Lean

namespace EvoNOMOS.R92

/-- A list of n joint actions on n independent modules can be defeated by
    assigning the i-th module's forbidden action to the i-th codeword's i-th
    coordinate. This is the diagonal lower bound, not the upper bound. -/
theorem diagonalObstruction {n q : Nat}
    (code : Fin n → Fin n → Fin q) :
    ∃ world : Fin n → Fin q,
      ∀ m : Fin n, ¬ (∀ i : Fin n, world i ≠ code m i) := by
  refine ⟨fun i => code i i, ?_⟩
  intro m h
  exact h m rfl

/-- If a symbol absent from the forbidden coordinates has been supplied,
    a constant joint action is admissible. The counting argument giving
    such a symbol when q>n is left to a later compiler-verified module. -/
theorem diagonalWitness {n q : Nat}
    (world : Fin n → Fin q) (j : Fin q)
    (h : ∀ i : Fin n, world i ≠ j) :
    ∃ action : Fin n → Fin q, ∀ i, world i ≠ action i :=
  ⟨fun _ => j, h⟩

#print axioms diagonalObstruction
#print axioms diagonalWitness
end EvoNOMOS.R92
