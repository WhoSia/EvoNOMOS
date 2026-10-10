import Init

/- EvoNOMOS G8 LAW-R1-P41-P0.
   A *typed, deliberately free* candidate signature, not a semantic model of
   every object-oriented language. Each named predicate inspects distinct
   source/behavior/authority/goal/dependency evidence coordinates.
   Independent satisfiability here is ONLY model-theoretic independence for
   the free product; actual Go realization is a separate empirical obligation.
   No additional axioms, sorry or admit. -/

namespace P41

structure EditWorld where
  compilerAccepts : Bool
  sourceRegisters : Bool
  oldObservationBefore : Nat
  oldObservationAfter : Nat
  editActor : Nat
  legitimateOwner : Nat
  targetRoute : Nat
  resolvedRoute : Nat
  demandedOutput : Nat
  producedOutput : Nat
  requestedPort : Nat
  actualPort : Nat
  deriving Repr, DecidableEq

def A_Typed (s : EditWorld) : Prop :=
  s.compilerAccepts = true

def B_OldObservationFrame (s : EditWorld) : Prop :=
  s.oldObservationAfter = s.oldObservationBefore

def C_Authorized (s : EditWorld) : Prop :=
  s.editActor = s.legitimateOwner

def D_RouteAndGoal (s : EditWorld) : Prop :=
  s.targetRoute = s.resolvedRoute ∧
    s.demandedOutput = s.producedOutput

def E_SourceRegistered (s : EditWorld) : Prop :=
  s.sourceRegisters = true

def F_DependencyAligned (s : EditWorld) : Prop :=
  s.requestedPort = s.actualPort

def candidateAdequacy (s : EditWorld) : Prop :=
  A_Typed s ∧ B_OldObservationFrame s ∧ C_Authorized s ∧
  D_RouteAndGoal s ∧ E_SourceRegistered s ∧ F_DependencyAligned s

def control : EditWorld :=
  { compilerAccepts := true
    sourceRegisters := true
    oldObservationBefore := 10
    oldObservationAfter := 10
    editActor := 1
    legitimateOwner := 1
    targetRoute := 20
    resolvedRoute := 20
    demandedOutput := 30
    producedOutput := 30
    requestedPort := 40
    actualPort := 40 }

def rejectA := { control with compilerAccepts := false }
def rejectB := { control with oldObservationAfter := 11 }
def rejectC := { control with legitimateOwner := 2 }
def rejectD := { control with resolvedRoute := 21 }
def rejectE := { control with sourceRegisters := false }
def rejectF := { control with actualPort := 41 }

theorem control_satisfies_candidates : candidateAdequacy control := by decide

theorem independence_A_in_free_signature :
    ¬ A_Typed rejectA ∧ B_OldObservationFrame rejectA ∧
    C_Authorized rejectA ∧ D_RouteAndGoal rejectA ∧
    E_SourceRegistered rejectA ∧ F_DependencyAligned rejectA := by decide

theorem independence_B_in_free_signature :
    A_Typed rejectB ∧ ¬ B_OldObservationFrame rejectB ∧
    C_Authorized rejectB ∧ D_RouteAndGoal rejectB ∧
    E_SourceRegistered rejectB ∧ F_DependencyAligned rejectB := by decide

theorem independence_C_in_free_signature :
    A_Typed rejectC ∧ B_OldObservationFrame rejectC ∧
    ¬ C_Authorized rejectC ∧ D_RouteAndGoal rejectC ∧
    E_SourceRegistered rejectC ∧ F_DependencyAligned rejectC := by decide

theorem independence_D_in_free_signature :
    A_Typed rejectD ∧ B_OldObservationFrame rejectD ∧
    C_Authorized rejectD ∧ ¬ D_RouteAndGoal rejectD ∧
    E_SourceRegistered rejectD ∧ F_DependencyAligned rejectD := by decide

theorem independence_E_in_free_signature :
    A_Typed rejectE ∧ B_OldObservationFrame rejectE ∧
    C_Authorized rejectE ∧ D_RouteAndGoal rejectE ∧
    ¬ E_SourceRegistered rejectE ∧ F_DependencyAligned rejectE := by decide

theorem independence_F_in_free_signature :
    A_Typed rejectF ∧ B_OldObservationFrame rejectF ∧
    C_Authorized rejectF ∧ D_RouteAndGoal rejectF ∧
    E_SourceRegistered rejectF ∧ ¬ F_DependencyAligned rejectF := by decide

/- This view retains compiler/source admission and chosen old/new behavior,
   *not* the principal/owner entitlement evidence. -/
def sourceBehaviorView (s : EditWorld) :
    Bool × Bool × Nat × Nat × Nat × Nat × Nat :=
  (s.compilerAccepts, s.sourceRegisters, s.oldObservationBefore,
   s.oldObservationAfter, s.resolvedRoute, s.producedOutput, s.actualPort)

def authorityDecision (s : EditWorld) : Bool :=
  decide (s.editActor = s.legitimateOwner)

theorem same_source_and_behavior_but_different_rights :
    sourceBehaviorView control = sourceBehaviorView rejectC ∧
    authorityDecision control ≠ authorityDecision rejectC := by decide

theorem nonfactorization {α β : Type}
    (view : α → β) (decision : α → Bool) (x y : α)
    (eqv : view x = view y) (distinct : decision x ≠ decision y) :
    ¬ ∃ f : β → Bool, ∀ z : α, decision z = f (view z) := by
  intro h
  rcases h with ⟨f, hf⟩
  apply distinct
  calc
    decision x = f (view x) := hf x
    _ = f (view y) := congrArg f eqv
    _ = decision y := (hf y).symm

theorem no_source_behavior_only_authority_classifier :
    ¬ ∃ f : (Bool × Bool × Nat × Nat × Nat × Nat × Nat) → Bool,
        ∀ s, authorityDecision s = f (sourceBehaviorView s) := by
  exact nonfactorization sourceBehaviorView authorityDecision control rejectC
    (by decide) (by decide)

/- The route identity is a separate observation, not reconstructible merely
   from unchanged old client output and the new output's scalar value. -/
def responseOnlyView (s : EditWorld) : Nat × Nat × Bool :=
  (s.oldObservationAfter, s.producedOutput, s.sourceRegisters)

def routeIdentityDecision (s : EditWorld) : Bool :=
  decide (s.resolvedRoute = s.targetRoute)

theorem no_response_only_route_identity_classifier :
    ¬ ∃ f : (Nat × Nat × Bool) → Bool,
        ∀ s, routeIdentityDecision s = f (responseOnlyView s) := by
  exact nonfactorization responseOnlyView routeIdentityDecision control rejectD
    (by decide) (by decide)

/- Evidence status and proof source are not the same as data sort.
   The provenance type tracks whether a premise has a source realization. -/
inductive EvidenceOrigin where
  | originalNativeGo
  | originalAST
  | authorityRecord
  | dependencyAudit
  | syntheticCountermodel
  deriving Repr, DecidableEq

structure PremiseEvidence where
  origin : EvidenceOrigin
  sourceRevision : String
  contractName : String
  isSourceRealization : Bool
  deriving Repr

def syntheticIndependenceReceipt (name : String) : PremiseEvidence :=
  { origin := .syntheticCountermodel, sourceRevision := "NONE",
    contractName := name, isSourceRealization := false }

theorem synthetic_does_not_imply_native_realization (name : String) :
    (syntheticIndependenceReceipt name).isSourceRealization = false := by rfl

end P41
