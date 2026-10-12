import Init

/- P42-P2-R5: restricted capability-obligation incidence and repair-site
   model. Each case corresponds to independently compiled, source-generated
   ORIGINAL Go language fixtures, but NO compiler-checked source-to-Lean
   simulation or historical maintainer evidence is asserted.
   TCS result is classical typed-interface satisfaction and shortest repair. -/
namespace P42R5

inductive Architecture where
  | bundleDirect
  | bundlePort
  | segregateDirect
  | segregatePort
  deriving Repr, DecidableEq

inductive FutureDemand where
  | readPartial
  | exportPartial
  | independentPartialPair
  | coordinatedFullProvider
  deriving Repr, DecidableEq

inductive Capability where
  | read
  | export
  deriving Repr, DecidableEq

def selectedCapRequired (a : Architecture) (selected required : Capability) : Bool :=
  match a with
  | .bundlePort => true
  | .segregatePort => selected == required
  | .bundleDirect => selected == required
  | .segregateDirect => selected == required

def readOnlyProvides (cap : Capability) : Bool := cap == .read
def exportOnlyProvides (cap : Capability) : Bool := cap == .export
def fullProvides (_ : Capability) : Bool := true

/- A selected Read provider type-checks at a port only if all methods required
   by that interface are present; finite Go method set analogue. -/
def interfaceConforms (a : Architecture) (selected : Capability)
    (provider : Capability → Bool) : Bool :=
  ((!selectedCapRequired a selected .read) || provider .read) &&
  ((!selectedCapRequired a selected .export) || provider .export)

theorem read_only_fails_bundle_port :
    interfaceConforms .bundlePort .read readOnlyProvides = false := by decide

theorem read_only_fits_segregated_port :
    interfaceConforms .segregatePort .read readOnlyProvides = true := by decide

theorem export_only_fails_bundle_port :
    interfaceConforms .bundlePort .export exportOnlyProvides = false := by decide

theorem full_provider_fits_both_ports :
    interfaceConforms .bundlePort .read fullProvides = true ∧
    interfaceConforms .segregatePort .read fullProvides = true ∧
    interfaceConforms .bundlePort .export fullProvides = true ∧
    interfaceConforms .segregatePort .export fullProvides = true := by decide

def affectedClients : FutureDemand → Nat
  | .readPartial => 1
  | .exportPartial => 1
  | .independentPartialPair => 2
  | .coordinatedFullProvider => 2

def isPort : Architecture → Bool
  | .bundlePort => true
  | .segregatePort => true
  | _ => false

/- Actual Go source-site obligations declared before the separate compiler
   run. Not calibrated engineering-hours. -/
def forcedIrrelevantMethods (a : Architecture) (d : FutureDemand) : Nat :=
  match a, d with
  | .bundlePort, .readPartial => 1
  | .bundlePort, .exportPartial => 1
  | .bundlePort, .independentPartialPair => 2
  | _, _ => 0

def consumerSignatureEdits (a : Architecture) (d : FutureDemand) : Nat :=
  if isPort a then 0 else affectedClients d

def wiringEdits (_ : Architecture) (d : FutureDemand) : Nat :=
  affectedClients d

def sourceSiteEdits (a : Architecture) (d : FutureDemand) : Nat :=
  forcedIrrelevantMethods a d +
  consumerSignatureEdits a d +
  wiringEdits a d

theorem sixteen_finite_site_forecasts :
    sourceSiteEdits .bundleDirect .readPartial = 2 ∧
    sourceSiteEdits .bundlePort .readPartial = 2 ∧
    sourceSiteEdits .segregateDirect .readPartial = 2 ∧
    sourceSiteEdits .segregatePort .readPartial = 1 ∧
    sourceSiteEdits .bundleDirect .independentPartialPair = 4 ∧
    sourceSiteEdits .bundlePort .independentPartialPair = 4 ∧
    sourceSiteEdits .segregateDirect .independentPartialPair = 4 ∧
    sourceSiteEdits .segregatePort .independentPartialPair = 2 ∧
    sourceSiteEdits .bundleDirect .coordinatedFullProvider = 4 ∧
    sourceSiteEdits .bundlePort .coordinatedFullProvider = 2 ∧
    sourceSiteEdits .segregateDirect .coordinatedFullProvider = 4 ∧
    sourceSiteEdits .segregatePort .coordinatedFullProvider = 2 := by decide

theorem correlation_changes_bundle_obligation_geometry :
    forcedIrrelevantMethods .bundlePort .independentPartialPair = 2 ∧
    forcedIrrelevantMethods .bundlePort .coordinatedFullProvider = 0 ∧
    forcedIrrelevantMethods .segregatePort .independentPartialPair = 0 ∧
    forcedIrrelevantMethods .segregatePort .coordinatedFullProvider = 0 := by decide

theorem unused_interface_shape_has_no_direct_client_impact
    (d : FutureDemand) :
    sourceSiteEdits .bundleDirect d = sourceSiteEdits .segregateDirect d := by
  cases d <;> decide

/- Current outputs share a single observational class before demands. There
   is no classifier of FUTURE method obligations that factors through it. -/
def currentObservation (_ : Architecture) : Bool := true

theorem present_behavior_insufficient_for_future_obligations :
    ¬ ∃ classifier : Bool → FutureDemand → Nat,
      ∀ a : Architecture,
        classifier (currentObservation a) .readPartial =
          forcedIrrelevantMethods a .readPartial := by
  rintro ⟨classifier, h⟩
  have a := h .bundlePort
  have b := h .segregatePort
  have ha : classifier true .readPartial = 1 := by
    simpa [currentObservation, forcedIrrelevantMethods] using a
  have hb : classifier true .readPartial = 0 := by
    simpa [currentObservation, forcedIrrelevantMethods] using b
  have contradiction : (1 : Nat) = 0 := ha.symm.trans hb
  exact Nat.one_ne_zero contradiction

/- These are algebraic sensitivity thresholds. The 'p' below is an
   INTEGER count of partial arrivals, not an estimated probability.
   External demand probability and developer-time weights are NOT measured. -/
def bundleSurface (partialArrivals lateWeight : Nat) : Nat :=
  1 + partialArrivals * lateWeight
def segregatedSurface (_partialArrivals _lateWeight : Nat) : Nat := 2

theorem birth_surface_prefers_bundle (w : Nat) :
    bundleSurface 0 w < segregatedSurface 0 w := by
  simp [bundleSurface, segregatedSurface]

theorem repeated_partial_demand_prefers_segregation :
    segregatedSurface 2 2 < bundleSurface 2 2 := by decide

theorem threshold_when_partial_cost_exceeds_one
    (arrivals weight : Nat) (h : 1 < arrivals * weight) :
    segregatedSurface arrivals weight <
      bundleSurface arrivals weight := by
  exact Nat.succ_lt_succ h

/- Explicit non-novelty: this is a bounded incidence-constraint model, not a
   discovery of a universal new OO/SOLID axiom or any historical actual cost. -/
end P42R5
