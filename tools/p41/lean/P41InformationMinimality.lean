import P41SemanticP0

/- P41-P2 — first *negative* irredundancy court.
   Theorems target information sufficiency, not historical SOLID. Original
   external Echo provider/route evidence is tested separately by pinned Go.
   These records are elementary abstract counterparts, not a Go simulator.
   No sorry/axiom/admit. -/

namespace P41P2
open P41

structure ProviderWorld where
  echoesRouterShape : Bool
  sourceAccepts : Bool
  actualProviderOutput : Nat
  requiredOutput : Nat
  deriving Repr, DecidableEq

def typeOnlyView (w : ProviderWorld) : Bool × Bool :=
  (w.echoesRouterShape, w.sourceAccepts)
def providerMeetsGoal (w : ProviderWorld) : Bool :=
  decide (w.actualProviderOutput = w.requiredOutput)

def nativeCompatibleProvider : ProviderWorld :=
  { echoesRouterShape := true, sourceAccepts := true,
    actualProviderOutput := 1, requiredOutput := 1 }
def nativeDivertingProvider : ProviderWorld :=
  { echoesRouterShape := true, sourceAccepts := true,
    actualProviderOutput := 2, requiredOutput := 1 }

theorem provider_type_shapes_equal_but_goals_differ :
    typeOnlyView nativeCompatibleProvider =
      typeOnlyView nativeDivertingProvider ∧
    providerMeetsGoal nativeCompatibleProvider ≠
      providerMeetsGoal nativeDivertingProvider := by decide

theorem no_type_and_source_only_provider_goal_classifier :
    ¬ ∃ f : (Bool × Bool) → Bool,
       ∀ w, providerMeetsGoal w = f (typeOnlyView w) := by
  exact nonfactorization typeOnlyView providerMeetsGoal
    nativeCompatibleProvider nativeDivertingProvider
    (by decide) (by decide)

/- Present GitHub platform permission does not logically determine previous
   revision-indexed permission. This is a toy temporal countermodel; current
   platform role observation is REAL but historic authorization is unknown. -/
structure RightsHistory where
  observedCurrentAdmin : Bool
  permissionAtEditRevision : Bool
  deriving Repr, DecidableEq

def currentPermissionView (h : RightsHistory) : Bool :=
  h.observedCurrentAdmin
def historicalAuthorized (h : RightsHistory) : Bool :=
  h.permissionAtEditRevision

def historicalYes : RightsHistory :=
  { observedCurrentAdmin := true, permissionAtEditRevision := true }
def historicalNo : RightsHistory :=
  { observedCurrentAdmin := true, permissionAtEditRevision := false }

theorem no_current_role_only_historical_authority_classifier :
    ¬ ∃ f : Bool → Bool,
      ∀ h, historicalAuthorized h = f (currentPermissionView h) := by
  exact nonfactorization currentPermissionView historicalAuthorized
    historicalYes historicalNo (by decide) (by decide)

/- Formal minimality adversary: adding a duplicate guard creates a *nonminimal*
   premise list even if all listed guards sound plausible. No universal axiom
   independence can follow merely from the number of named conjuncts. -/
def redundantCompilerGuard (w : EditWorld) : Prop := A_Typed w

theorem duplicate_premise_is_eliminable (w : EditWorld) :
    (candidateAdequacy w ∧ redundantCompilerGuard w) ↔
      candidateAdequacy w := by
  constructor
  · exact And.left
  · intro h
    exact ⟨h, h.1⟩

/- Three DISTINCT claims:
   1. free product omission witnesses: syntactic independence, P0
   2. observational information necessity: selected-source countermodels, P1/P2
   3. noncircular safe-evolution axiom basis: still entirely OPEN.
   No proof below asserts (3). -/

end P41P2
