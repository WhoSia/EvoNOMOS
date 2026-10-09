import Init

/-!
  P35-MATH-0 kernel-checked *foundational control*, not a new software law.
  Two implementations agree at the initial world and separate after an update.
  The only theorem about context ordering is basic logical antitonicity.
-/
namespace EvoNOMOS.Math0

inductive Design where
  | live
  | snapshot
  deriving DecidableEq, Repr

structure World where
  atConstruction : Bool
  current : Bool
  deriving DecidableEq, Repr

def aligned (b : Bool) : World :=
  { atConstruction := b, current := b }

def updated (w : World) : World :=
  { w with current := !w.current }

def observe (d : Design) (w : World) : Bool :=
  match d with
  | .live => w.current
  | .snapshot => w.atConstruction

def obsEq (contexts : List World) (a b : Design) : Prop :=
  ∀ w, w ∈ contexts → observe a w = observe b w

-- A context set that is larger admits fewer observational equivalences.
theorem obsEq_antitone
    (small large : List World) (a b : Design)
    (hsub : ∀ w, w ∈ small → w ∈ large)
    (h : obsEq large a b) : obsEq small a b := by
  intro w hw
  exact h w (hsub w hw)

theorem agree_initially (b : Bool) :
    observe .live (aligned b) = observe .snapshot (aligned b) := by
  cases b <;> rfl

theorem separate_after_update (b : Bool) :
    observe .live (updated (aligned b)) ≠
      observe .snapshot (updated (aligned b)) := by
  cases b <;> decide

theorem initial_context_equivalent (b : Bool) :
    obsEq [aligned b] .live .snapshot := by
  intro w hw
  simp only [List.mem_singleton] at hw
  subst w
  exact agree_initially b

theorem updated_context_distinguishes (b : Bool) :
    ¬ obsEq [updated (aligned b)] .live .snapshot := by
  intro h
  have contra := h (updated (aligned b)) (by simp)
  exact separate_after_update b contra

-- Any scoring function of the *initial observation alone* cannot
-- distinguish these two implementations, even if its codomain is arbitrary.
theorem initial_only_score_indistinguishable
    {Score : Type} (score : Bool → Score) (b : Bool) :
    score (observe .live (aligned b)) =
      score (observe .snapshot (aligned b)) := by
  rw [agree_initially]

end EvoNOMOS.Math0
