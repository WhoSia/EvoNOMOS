import Lean

/-!
R92 candidate formalization; compiler verification pending.
good w a means a meets the fixed feasibility and regret threshold in world w.
This does not assert that software contracts are already represented correctly.
-/
namespace EvoNOMOS.R92

theorem fiberCompatibility {W A M : Type}
    (good : W → A → Prop) (encode : W → M) :
    (∃ decode : M → A, ∀ w, good w (decode (encode w))) ↔
    (∀ m, ∃ a : A, ∀ w, encode w = m → good w a) := by
  constructor
  · intro h
    obtain ⟨decode, hd⟩ := h
    intro m
    refine ⟨decode m, ?_⟩
    intro w hw
    rw [← hw]
    exact hd w
  · intro h
    classical
    let decode : M → A := fun m => Classical.choose (h m)
    refine ⟨decode, ?_⟩
    intro w
    exact Classical.choose_spec (h (encode w)) w rfl

theorem messageCodeIffActionCover {W A : Type}
    (good : W → A → Prop) (k : Nat) :
    (∃ encode : W → Fin k, ∃ decode : Fin k → A,
      ∀ w, good w (decode (encode w))) ↔
    (∃ decode : Fin k → A, ∀ w, ∃ m : Fin k, good w (decode m)) := by
  constructor
  · intro h
    obtain ⟨encode, decode, hd⟩ := h
    exact ⟨decode, fun w => ⟨encode w, hd w⟩⟩
  · intro h
    obtain ⟨decode, hd⟩ := h
    classical
    let encode : W → Fin k := fun w => Classical.choose (hd w)
    exact ⟨encode, decode, fun w => Classical.choose_spec (hd w)⟩

theorem refinementPreservesFeasibility {W A M N : Type}
    (good : W → A → Prop) (fine : W → N) (coarse : W → M)
    (project : N → M) (h : ∀ w, coarse w = project (fine w))
    (old : M → A) (valid : ∀ w, good w (old (coarse w))) :
    ∃ new : N → A, ∀ w, good w (new (fine w)) := by
  refine ⟨fun n => old (project n), ?_⟩
  intro w
  rw [← h w]
  exact valid w

#print axioms fiberCompatibility
#print axioms messageCodeIffActionCover
#print axioms refinementPreservesFeasibility
end EvoNOMOS.R92
