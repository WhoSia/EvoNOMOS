import Init

/- EvoNOMOS P42 R11-P10-P12
   MATHEMATICS ONLY: partial source/net edits and a separate
   coenabledness square. B1 (forward) and B2 (backward) are HYPOTHESES,
   not claims already verified for all Go source programs.
   The mathematical court was sealed at Git commit d01c1300.
   Do not infer actual source rights, client/cost equivalence or new law.
-/

namespace P12SourceDiamond

def Hblocked (w : List Bool) : Prop := w.length ≤ 1

def Hfull (w : List Bool) : Prop :=
  w = [] ∨ w = [false] ∨ w = [true] ∨
  w = [false, true] ∨ w = [true, false]

instance (w : List Bool) : Decidable (Hblocked w) := by
  unfold Hblocked
  infer_instance

instance (w : List Bool) : Decidable (Hfull w) := by
  unfold Hfull
  infer_instance

theorem blocked_empty : Hblocked [] := by decide
theorem blocked_a : Hblocked [false] := by decide
theorem blocked_b : Hblocked [true] := by decide
theorem blocked_no_ab : ¬ Hblocked [false, true] := by decide
theorem blocked_no_ba : ¬ Hblocked [true, false] := by decide

theorem full_empty : Hfull [] := by decide
theorem full_a : Hfull [false] := by decide
theorem full_b : Hfull [true] := by decide
theorem full_ab : Hfull [false, true] := by decide
theorem full_ba : Hfull [true, false] := by decide

/- Hblocked is closed under ANY length-preserving permutation,
   stronger than adjacent a/b trace swaps, yet fails to fill the square.
   This is a demonstration that trace saturation does NOT entail
   concurrent joint admission of two independently initially enabled edits.
-/
theorem blocked_saturated_by_length
    (u v : List Bool) (h : Hblocked u)
    (hl : u.length = v.length) : Hblocked v := by
  unfold Hblocked at *
  simpa [hl] using h

theorem saturation_does_not_imply_diamond :
    Hblocked [false] ∧ Hblocked [true] ∧
    ¬ Hblocked [false, true] ∧ ¬ Hblocked [true, false] := by decide

/- Typed source/net relation: two-sided witness plus a true independent
   square in a net forces BOTH concrete source edit orders.
   Endpoint equality is proved only under abstraction alpha, not as
   equal original source bytes.
-/
theorem reflect_concurrent_square
    {S N E : Type}
    (alpha : S → N)
    (src : S → E → Option S)
    (net : N → E → Option N)
    (forward : ∀ s e s', src s e = some s' →
                  net (alpha s) e = some (alpha s'))
    (backward : ∀ s e n', net (alpha s) e = some n' →
                   ∃ s', src s e = some s' ∧ alpha s' = n')
    (start : S) (a b : E) (sa sb : S)
    (ha : src start a = some sa)
    (hb : src start b = some sb)
    (netSquare :
       ∀ n na nb, net n a = some na → net n b = some nb →
         ∃ nab, net na b = some nab ∧ net nb a = some nab) :
    ∃ sab sba,
      src sa b = some sab ∧ src sb a = some sba ∧ alpha sab = alpha sba := by
  have hna := forward start a sa ha
  have hnb := forward start b sb hb
  obtain ⟨nab, hnab1, hnab2⟩ :=
    netSquare (alpha start) (alpha sa) (alpha sb) hna hnb
  obtain ⟨sab, hsab, heqAB⟩ := backward sa b nab hnab1
  obtain ⟨sba, hsba, heqBA⟩ := backward sb a nab hnab2
  exact ⟨sab, sba, hsab, hsba, heqAB.trans heqBA.symm⟩

/- General nonfactorization necessity: cannot infer an actual edit
   acceptance predicate from a boundary projection with a split fibre.
   Already classically proved in P40 Lean; recorded again only as
   an application, not a new priority.
-/
theorem admission_requires_boundary_information
    {S B : Type}
    (beta : S → B) (admitted : S → Bool)
    (x y : S) (same : beta x = beta y)
    (different : admitted x ≠ admitted y) :
    ¬ ∃ guard : B → Bool, ∀ s, admitted s = guard (beta s) := by
  intro h
  obtain ⟨guard, hg⟩ := h
  apply different
  calc
    admitted x = guard (beta x) := hg x
    _ = guard (beta y) := by rw [same]
    _ = admitted y := (hg y).symm

end P12SourceDiamond
