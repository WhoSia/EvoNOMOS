import Init

/-!
MATH-2: classical relational may/must, composition, commuting squares and
a finite anti-uniqueness countermodel. No new architectural law is claimed.
-/
namespace EvoNOMOS.Math2

def May {A : Type} (r : A → A → Prop) (start : A) (p : A → Prop) : Prop :=
  ∃ next, r start next ∧ p next

def Must {A : Type} (r : A → A → Prop) (start : A) (p : A → Prop) : Prop :=
  (∃ next, r start next) ∧ ∀ next, r start next → p next

def TwoStep {A : Type} (r s : A → A → Prop) (start finish : A) : Prop :=
  ∃ mid, r start mid ∧ s mid finish

theorem must_implies_may {A : Type}
    (r : A → A → Prop) (start : A) (p : A → Prop)
    (h : Must r start p) : May r start p := by
  obtain ⟨next, hrepair⟩ := h.1
  exact ⟨next, hrepair, h.2 next hrepair⟩

theorem must_preserved_under_nonempty_restriction {A : Type}
    (original restricted : A → A → Prop) (start : A) (p : A → Prop)
    (hsub : ∀ x y, restricted x y → original x y)
    (hexists : ∃ next, restricted start next)
    (h : Must original start p) : Must restricted start p := by
  constructor
  · exact hexists
  · intro next hn
    exact h.2 next (hsub start next hn)

theorem path_inclusion_of_square {A : Type}
    (r s : A → A → Prop)
    (square : ∀ a b c, r a b → s b c → ∃ d, s a d ∧ r d c)
    (a c : A) (h : TwoStep r s a c) : TwoStep s r a c := by
  obtain ⟨b, hab, hbc⟩ := h
  exact square a b c hab hbc

theorem reachable_sets_equal_of_two_squares {A : Type}
    (r s : A → A → Prop)
    (forward : ∀ a b c, r a b → s b c → ∃ d, s a d ∧ r d c)
    (backward : ∀ a b c, s a b → r b c → ∃ d, r a d ∧ s d c)
    (a c : A) : TwoStep r s a c ↔ TwoStep s r a c := by
  constructor
  · exact path_inclusion_of_square r s forward a c
  · exact path_inclusion_of_square s r backward a c

theorem distinguished_symbolic_implies_distinguished_concrete
    {State Observation Signature : Type}
    (observe : State → Observation) (decode : Observation → Signature)
    (x y : State)
    (distinguished : decode (observe x) ≠ decode (observe y)) :
    observe x ≠ observe y := by
  intro heq
  exact distinguished (congrArg decode heq)

-- This finite relation has two different, admitted successors from a
-- single starting point; witnessing one does not imply all repairs share
-- a selected implementation property (e.g., introducing a helper).
def demoRepair (a b : Fin 3) : Prop :=
  a = 0 ∧ (b = 1 ∨ b = 2)

theorem demo_two_distinct_admissible_repairs :
    demoRepair 0 1 ∧ demoRepair 0 2 ∧ (1 : Fin 3) ≠ 2 := by
  simp [demoRepair]

theorem one_valid_patch_does_not_force_every_patch :
    May demoRepair 0 (fun b => b = 1) ∧
      ¬ Must demoRepair 0 (fun b => b = 1) := by
  constructor
  · exact ⟨1, by simp [demoRepair], rfl⟩
  · intro all
    have other : demoRepair 0 2 := by simp [demoRepair]
    have impos : (2 : Fin 3) = 1 := all.2 2 other
    cases impos

-- Two noncommuting illustrative demand relations. Noncommutation is
-- possible, but NOT asserted to occur in the tested Go D9/D10 patches.
def addA (x y : Fin 5) : Prop :=
  (x = 0 ∧ y = 1) ∨ (x = 2 ∧ y = 4)

def addB (x y : Fin 5) : Prop :=
  (x = 0 ∧ y = 2) ∨ (x = 1 ∧ y = 3)

theorem ab_can_reach_three : TwoStep addA addB 0 3 := by
  exact ⟨1, by simp [addA, addB], by simp [addA, addB]⟩

theorem ba_cannot_reach_three : ¬ TwoStep addB addA 0 3 := by
  intro h
  obtain ⟨mid, hb, ha⟩ := h
  have midIsTwo : mid = 2 := by
    change ((0 : Fin 5) = 0 ∧ mid = 2) ∨
      ((0 : Fin 5) = 1 ∧ mid = 3) at hb
    cases hb with
    | inl yes => exact yes.2
    | inr no => cases no.1
  subst mid
  have impossible : ¬ addA 2 3 := by simp [addA, addB]
  exact impossible ha

theorem ba_can_reach_four : TwoStep addB addA 0 4 := by
  exact ⟨2, by simp [addA, addB], by simp [addA, addB]⟩

theorem ab_cannot_reach_four : ¬ TwoStep addA addB 0 4 := by
  intro h
  obtain ⟨mid, ha, hb⟩ := h
  have midIsOne : mid = 1 := by
    change ((0 : Fin 5) = 0 ∧ mid = 1) ∨
      ((0 : Fin 5) = 2 ∧ mid = 4) at ha
    cases ha with
    | inl yes => exact yes.2
    | inr no => cases no.1
  subst mid
  have impossible : ¬ addB 1 4 := by simp [addA, addB]
  exact impossible hb

end EvoNOMOS.Math2
