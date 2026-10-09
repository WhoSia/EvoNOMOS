import Init

/-!
EvoNOMOS MATH-1: deterministic total state transition/observation,
finite-trace equivalence and a proof of independent-product congruence.
Classical foundational formalization, NOT a new software-design law.
-/

namespace EvoNOMOS.Math1

structure Machine (S I O : Type) where
  step : S → I → S
  out : S → O

def run {S I O : Type} (m : Machine S I O) : S → List I → S
  | s, [] => s
  | s, a :: rest => run m (m.step s a) rest

/-- Equality of terminal observations for every input word of length ≤ k. -/
def eqUpTo {S T I O : Type}
    (k : Nat) (m : Machine S I O) (s : S)
    (n : Machine T I O) (t : T) : Prop :=
  ∀ word : List I, word.length ≤ k →
    m.out (run m s word) = n.out (run n t word)

theorem depth_antitone {S T I O : Type}
    {m : Machine S I O} {s : S}
    {n : Machine T I O} {t : T}
    {j k : Nat} (hjk : j ≤ k)
    (h : eqUpTo k m s n t) : eqUpTo j m s n t := by
  intro word hlen
  exact h word (Nat.le_trans hlen hjk)

theorem eqUpTo_refl {S I O : Type}
    (k : Nat) (m : Machine S I O) (s : S) :
    eqUpTo k m s m s := by
  intro word _
  rfl

theorem eqUpTo_symm {S T I O : Type}
    {k : Nat} {m : Machine S I O} {s : S}
    {n : Machine T I O} {t : T}
    (h : eqUpTo k m s n t) : eqUpTo k n t m s := by
  intro word hlen
  exact (h word hlen).symm

/-- Independent synchronous product on the *same input*,
    with both outputs visible as an ordered pair. -/
def prodMachine {S T I O P : Type}
    (m : Machine S I O) (e : Machine T I P) :
    Machine (S × T) I (O × P) where
  step := fun q a => (m.step q.1 a, e.step q.2 a)
  out := fun q => (m.out q.1, e.out q.2)

/-- Genuine run factorization for independent synchronous composition. -/
theorem runProduct {S T I O P : Type}
    (m : Machine S I O) (e : Machine T I P)
    (s : S) (t : T) (word : List I) :
    run (prodMachine m e) (s,t) word =
      (run m s word, run e t word) := by
  induction word generalizing s t with
  | nil => rfl
  | cons a rest ih =>
      simpa [run, prodMachine] using
        (ih (s := m.step s a) (t := e.step t a))

/-- The real congruence premise is independence and factored observation.
    Arbitrary shared-state/probing context is NOT covered. -/
theorem independent_product_congruence
    {S T U I O P : Type}
    (m : Machine S I O) (n : Machine T I O)
    (e : Machine U I P) (s : S) (t : T) (u : U)
    (k : Nat) (h : eqUpTo k m s n t) :
    eqUpTo k (prodMachine m e) (s,u) (prodMachine n e) (t,u) := by
  intro word hlen
  rw [runProduct m e s u word, runProduct n e t u word]
  change (m.out (run m s word), e.out (run e u word)) =
    (n.out (run n t word), e.out (run e u word))
  exact congrArg (fun o => (o, e.out (run e u word))) (h word hlen)

/-- Initial output can be used as a score but cannot identify a structure
    if the two machines are equivalent at depth 0. -/
theorem observed_score_equal {S T I O Q : Type}
    (m : Machine S I O) (n : Machine T I O)
    (s : S) (t : T) (k : Nat)
    (h : eqUpTo k m s n t) (score : O → Q)
    (word : List I) (hw : word.length ≤ k) :
    score (m.out (run m s word)) =
      score (n.out (run n t word)) :=
  congrArg score (h word hw)

def toggle : Machine Bool Unit Bool where
  step := fun b _ => !b
  out := id

def stutter : Machine Bool Unit Bool where
  step := fun b _ => b
  out := id

theorem toggle_stutter_eq_zero :
    eqUpTo 0 toggle false stutter false := by
  intro word hw
  cases word with
  | nil => rfl
  | cons a rest => simp at hw

theorem toggle_stutter_separate_one :
    ¬ eqUpTo 1 toggle false stutter false := by
  intro h
  have contrad := h [()] (by decide)
  have hf : (true : Bool) = false := by
    simpa [run, toggle, stutter] using contrad
  cases hf

/-- Both states have identical *published* observations at all depths. -/
def silent : Machine Bool Unit Bool where
  step := fun b _ => b
  out := fun _ => false

theorem silent_hides_all_depths (k : Nat) :
    eqUpTo k silent false silent true := by
  intro word _
  rfl

/-- An illicit context that reads the hidden Bool *state*, rather than
    the declared output, separates even at the empty trace. -/
def leakedState (s : Bool) (word : List Unit) : Bool :=
  run silent s word

theorem private_state_probe_counterexample :
    leakedState false [] ≠ leakedState true [] := by
  decide

end EvoNOMOS.Math1
