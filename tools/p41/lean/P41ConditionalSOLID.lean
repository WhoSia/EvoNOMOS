import P41InformationMinimality

/- P41-P3: five conditional SOLID-shaped claims, each reduced to ordinary
   classical frame, guarded extension, contextual equivalence, interface
   projection, or provider contextual refinement. These are tiny declared
   functional semantics: NOT axiomatizations of historical SOLID.
   No sorry, axiom or admit; Go source realizations are separate tests. -/
namespace P41P3
open P41
open P41P2

/- SRP-shaped: a change at one owned responsibility coordinate cannot alter
   a distinct observer coordinate. This is the classical frame principle. -/
def writeAt (state : Nat → Nat) (owned value : Nat) : Nat → Nat :=
  fun key => if key = owned then value else state key

theorem srp_classical_frame
    (state : Nat → Nat) (owned observed newValue : Nat)
    (separate : observed ≠ owned) :
    writeAt state owned newValue observed = state observed := by
  simp [writeAt, separate]

theorem srp_without_separation_can_break_observation :
    writeAt (fun _ : Nat => 0) 3 1 3 ≠ (fun _ : Nat => 0) 3 := by
  decide

/- OCP-shaped: an extension adding a route without modifying existing routes
   preserves all explicitly enumerated old-client requests if its key is
   disjoint from them. This is guarded update / classical data refinement. -/
def extension (baseline : Nat → Nat) (newRoute newHandler : Nat) :=
  writeAt baseline newRoute newHandler

theorem ocp_conditional_old_client_preservation
    (baseline : Nat → Nat) (oldRequests : List Nat)
    (newRoute newHandler : Nat)
    (disjoint : ∀ req, req ∈ oldRequests → req ≠ newRoute) :
    ∀ req, req ∈ oldRequests →
      extension baseline newRoute newHandler req = baseline req := by
  intro req h
  exact srp_classical_frame baseline newRoute req newHandler (disjoint req h)

theorem ocp_unrestricted_existing_route_overwrite_fails :
    extension (fun _ : Nat => 1) 7 2 7 ≠ (fun _ : Nat => 1) 7 := by
  decide

/- LSP-shaped: a provider replacement is substitutable for a declared
   observer family precisely when those observers yield identical results.
   Reproduces a standard contextual observational refinement definition. -/
def contextualAgreement (original replacement : Nat → Nat)
    (contexts : List Nat) : Prop :=
  ∀ c, c ∈ contexts → replacement c = original c

theorem lsp_contextual_replacement
    (oldImpl candidate : Nat → Nat) (contexts : List Nat)
    (refinement : contextualAgreement oldImpl candidate contexts) :
    ∀ c, c ∈ contexts → candidate c = oldImpl c := by
  exact refinement

def coarseOutput (_ : Nat) : Nat := 200
def selectedRoute (provider : Nat) : Nat :=
  if provider = 0 then 17 else 18

theorem lsp_same_coarse_output_different_routing :
    coarseOutput 0 = coarseOutput 1 ∧
    selectedRoute 0 ≠ selectedRoute 1 := by
  decide

/- ISP-shaped: clients need a projection to the operations they actually
   require. A provider implementing a larger interface may be consumed
   through a narrow projection; adding unrelated methods is unnecessary.
   This is classical logical weakening/projection. -/
def meetsPortSet (provider : Nat → Bool) (ports : List Nat) : Prop :=
  ∀ p, p ∈ ports → provider p = true

theorem isp_narrowing
    (provider : Nat → Bool) (large small : List Nat)
    (subset : ∀ p, p ∈ small → p ∈ large)
    (hasLarge : meetsPortSet provider large) :
    meetsPortSet provider small := by
  intro p hp
  exact hasLarge p (subset p hp)

theorem isp_context_projection
    (providerA providerB : Nat → Bool) (required : List Nat)
    (agree : ∀ port, port ∈ required →
      providerA port = providerB port) :
    meetsPortSet providerA required ↔
      meetsPortSet providerB required := by
  constructor
  · intro h port hp
    rw [← agree port hp]
    exact h port hp
  · intro h port hp
    rw [agree port hp]
    exact h port hp

/- DIP-shaped: the original Echo.Router type boundary does not imply
   clients accept all runtime implementations. Reuses already verified
   classical factorization obstruction from P41-P2. -/
theorem dip_shape_not_behavior :
    ¬ ∃ classifier : Bool × Bool → Bool, ∀ provider,
      providerMeetsGoal provider =
        classifier (typeOnlyView provider) :=
  no_type_and_source_only_provider_goal_classifier

theorem dip_semantically_qualified_replacement
    (expected actual : Nat → Nat) (required : List Nat)
    (behavioralEvidence : contextualAgreement expected actual required) :
    ∀ request, request ∈ required →
      actual request = expected request := by
  exact behavioralEvidence

/- Explicit orthogonality of actual source/behavior and edit rights: no
   SOLID-shaped structural theorem licenses a historical modification. -/
theorem source_and_behavior_not_authority :
    ¬ ∃ authorityFromCode :
      (Bool × Bool × Nat × Nat × Nat × Nat × Nat) → Bool,
      ∀ w : EditWorld,
       authorityDecision w = authorityFromCode (sourceBehaviorView w) :=
  no_source_behavior_only_authority_classifier

/- Classical comparator: the five guarded conclusions are each a direct
   specialization of existing frame/context/refinement/projection/factorization
   reasoning. These are REDUCTIONS, not new universal SOLID axioms. -/

end P41P3
