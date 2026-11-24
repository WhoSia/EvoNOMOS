import Lean

/-!
R92 candidate formalization. Compiler verification is pending.
A path potential is a lower-bound certificate, not a claim of novelty.
Only natural-number edge costs are modeled here.
-/
namespace EvoNOMOS.R92

inductive Walk {V : Type} (E : V → V → Nat → Prop) :
    V → V → Nat → Prop where
  | refl (v : V) : Walk E v v 0
  | step {u v t : V} {w k : Nat} :
      E u v w → Walk E v t k → Walk E u t (w + k)

theorem pathPotentialLowerBound {V : Type} {E : V → V → Nat → Prop}
    (p : V → Nat)
    (h : ∀ u v w, E u v w → p u ≤ w + p v)
    {s t : V} {k : Nat} (walk : Walk E s t k) :
    p s ≤ k + p t := by
  induction walk with
  | refl v => simp
  | @step u v t w k edge tail ih =>
      have he := h u v w edge
      omega

theorem exactCostCertificate {V : Type} {E : V → V → Nat → Prop}
    (p : V → Nat) (s t : V) (k : Nat)
    (h : ∀ u v w, E u v w → p u ≤ w + p v)
    (hp : p s = k + p t)
    (witness : Walk E s t k) :
    Walk E s t k ∧ ∀ j, Walk E s t j → k ≤ j := by
  refine ⟨witness, ?_⟩
  intro j path
  have hb := pathPotentialLowerBound p h path
  omega

theorem summedPotential {V : Type} {E : V → V → Nat → Prop}
    (p q : V → Nat)
    (h : ∀ u v w, E u v w →
      ∃ a b : Nat, a + b ≤ w ∧ p u ≤ a + p v ∧ q u ≤ b + q v) :
    ∀ u v w, E u v w → p u + q u ≤ w + (p v + q v) := by
  intro u v w edge
  obtain ⟨a,b,hab,hp,hq⟩ := h u v w edge
  omega

#print axioms pathPotentialLowerBound
#print axioms exactCostCertificate
#print axioms summedPotential
end EvoNOMOS.R92
