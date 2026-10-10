import Init

/- P40 Math-B-P2: conditional structural-guard independence and classical
   future-continuation kernel inclusion.
   This proves mathematical statements about the declared finite/typed models,
   NOT axioms describing all Go programs. No axiom/sorry/admit. -/

namespace P40MathB

structure World where
  typed : Bool
  observedOld : Nat
  expectedOld : Nat
  ownerAllows : Bool
  frozenCore : Nat
  currentCore : Nat
  occupiedKey : Nat
  newKey : Nat
  parentTree : Nat
  childTree : Nat
  routeAlreadySealed : Bool
  registerGlobalMiddleware : Bool
  dependencyTarget : Nat
  stablePort : Nat
  deriving Repr, DecidableEq

def LocalOK (w : World) : Prop :=
  w.typed = true ∧
  w.observedOld = w.expectedOld ∧
  w.ownerAllows = true ∧
  w.frozenCore = w.currentCore ∧
  w.dependencyTarget = w.stablePort

def NamespaceFree (w : World) : Prop := w.occupiedKey ≠ w.newKey
def NoTreeAlias (w : World) : Prop := w.parentTree ≠ w.childTree
def OrderSafe (w : World) : Prop :=
  ¬ (w.routeAlreadySealed = true ∧ w.registerGlobalMiddleware = true)

def AllGuards (w : World) : Prop :=
  LocalOK w ∧ NamespaceFree w ∧ NoTreeAlias w ∧ OrderSafe w

instance (w : World) : Decidable (LocalOK w) := by
  unfold LocalOK
  infer_instance

instance (w : World) : Decidable (NamespaceFree w) := by
  unfold NamespaceFree
  infer_instance

instance (w : World) : Decidable (NoTreeAlias w) := by
  unfold NoTreeAlias
  infer_instance

instance (w : World) : Decidable (OrderSafe w) := by
  unfold OrderSafe
  infer_instance

instance (w : World) : Decidable (AllGuards w) := by
  unfold AllGuards
  infer_instance

def base : World :=
  { typed := true, observedOld := 7, expectedOld := 7,
    ownerAllows := true, frozenCore := 17, currentCore := 17,
    occupiedKey := 1, newKey := 2,
    parentTree := 0, childTree := 1,
    routeAlreadySealed := false, registerGlobalMiddleware := true,
    dependencyTarget := 3, stablePort := 3 }

def badNamespace : World := { base with newKey := 1 }
def badAlias : World := { base with childTree := 0 }
def badOrder : World := { base with routeAlreadySealed := true }

theorem all_guards_base : AllGuards base := by decide
theorem namespace_obligation_independent :
    LocalOK badNamespace ∧ NoTreeAlias badNamespace ∧
    OrderSafe badNamespace ∧ ¬ NamespaceFree badNamespace := by decide
theorem alias_obligation_independent :
    LocalOK badAlias ∧ NamespaceFree badAlias ∧
    OrderSafe badAlias ∧ ¬ NoTreeAlias badAlias := by decide
theorem order_obligation_independent :
    LocalOK badOrder ∧ NamespaceFree badOrder ∧
    NoTreeAlias badOrder ∧ ¬ OrderSafe badOrder := by decide

theorem no_factorization {X Q : Type} (view : X → Q) (outcome : X → Bool)
    (x y : X) (hview : view x = view y) (hneq : outcome x ≠ outcome y) :
    ¬ ∃ predict : Q → Bool, ∀ z, outcome z = predict (view z) := by
  intro h
  rcases h with ⟨predict, hp⟩
  apply hneq
  calc
    outcome x = predict (view x) := hp x
    _ = predict (view y) := by rw [hview]
    _ = outcome y := (hp y).symm

def surfaceView (w : World) : Nat × Nat × Bool × Nat :=
  (w.occupiedKey, w.newKey, w.typed, w.observedOld)

def legal (w : World) : Bool := decide (AllGuards w)

theorem same_surface_different_alias :
    surfaceView base = surfaceView badAlias ∧ legal base ≠ legal badAlias := by decide

theorem surface_does_not_decide_gluing :
    ¬ ∃ f : (Nat × Nat × Bool × Nat) → Bool,
        ∀ w, legal w = f (surfaceView w) := by
  exact no_factorization surfaceView legal base badAlias
    (by decide) (by decide)

/- Deterministic edit automata: the next statements do not require finiteness. -/

def run {S E : Type} (step : S → E → S) (s : S) : List E → S
  | [] => s
  | e :: w => run step (step s e) w

def FutureEq {S E O : Type} (step : S → E → S) (obs : S → O)
    (s t : S) : Prop :=
  ∀ w : List E, obs (run step s w) = obs (run step t w)

theorem futureEq_step {S E O : Type} (step : S → E → S)
    (obs : S → O) {s t : S} (h : FutureEq step obs s t) (e : E) :
    FutureEq step obs (step s e) (step t e) := by
  intro w
  exact h (e :: w)

theorem run_map {S Q E : Type}
    (step : S → E → S) (abstractStep : Q → E → Q)
    (q : S → Q)
    (hStep : ∀ s e, q (step s e) = abstractStep (q s) e)
    (s : S) (word : List E) :
    q (run step s word) = run abstractStep (q s) word := by
  induction word generalizing s with
  | nil => rfl
  | cons e es ih =>
      calc
        q (run step s (e :: es)) = q (run step (step s e) es) := rfl
        _ = run abstractStep (q (step s e)) es := ih (step s e)
        _ = run abstractStep (abstractStep (q s) e) es := by rw [hStep s e]
        _ = run abstractStep (q s) (e :: es) := rfl

theorem exact_abstraction_kernel_subset_futureEq {S Q E O : Type}
    (step : S → E → S) (abstractStep : Q → E → Q)
    (obs : S → O) (abstractObs : Q → O) (q : S → Q)
    (hStep : ∀ s e, q (step s e) = abstractStep (q s) e)
    (hObs : ∀ s, obs s = abstractObs (q s))
    {s t : S} (hq : q s = q t) :
    FutureEq step obs s t := by
  intro w
  calc
    obs (run step s w) = abstractObs (q (run step s w)) := hObs _
    _ = abstractObs (run abstractStep (q s) w) := by
      rw [run_map step abstractStep q hStep s w]
    _ = abstractObs (run abstractStep (q t) w) := by rw [hq]
    _ = abstractObs (q (run step t w)) := by
      rw [run_map step abstractStep q hStep t w]
    _ = obs (run step t w) := (hObs _).symm


/- P3: source-specific admission predicate motivated by independent per-method
   radix trees (a model, NOT a formal verification of the original Go code). -/

structure MethodScopedPair where
  localA : Bool
  localB : Bool
  disjointRequestLanguages : Bool
  sameMethodTree : Bool
  wildcardStaticConflict : Bool
  deriving Repr, DecidableEq

def extensionalSignature (p : MethodScopedPair) : Bool × Bool × Bool :=
  (p.localA, p.localB, p.disjointRequestLanguages)

def scopedSourceAdmitted (p : MethodScopedPair) : Bool :=
  p.localA && p.localB && !(p.sameMethodTree && p.wildcardStaticConflict)

def sameTreeDisjoint : MethodScopedPair :=
  { localA := true, localB := true, disjointRequestLanguages := true,
    sameMethodTree := true, wildcardStaticConflict := true }

def distinctMethodDisjoint : MethodScopedPair :=
  { sameTreeDisjoint with sameMethodTree := false }

theorem p3_extensional_indistinguishable :
    extensionalSignature sameTreeDisjoint =
      extensionalSignature distinctMethodDisjoint := by decide

theorem p3_source_admission_diverges :
    scopedSourceAdmitted sameTreeDisjoint ≠
      scopedSourceAdmitted distinctMethodDisjoint := by decide

theorem p3_no_request_disjointness_only_classifier :
    ¬ ∃ f : (Bool × Bool × Bool) → Bool,
        ∀ x, scopedSourceAdmitted x = f (extensionalSignature x) := by
  exact no_factorization extensionalSignature scopedSourceAdmitted
    sameTreeDisjoint distinctMethodDisjoint
    p3_extensional_indistinguishable p3_source_admission_diverges

theorem p3_method_partition_frame (x : MethodScopedPair)
    (ha : x.localA = true) (hb : x.localB = true)
    (hDistinct : x.sameMethodTree = false) :
    scopedSourceAdmitted x = true := by
  simp [scopedSourceAdmitted, ha, hb, hDistinct]


end P40MathB
