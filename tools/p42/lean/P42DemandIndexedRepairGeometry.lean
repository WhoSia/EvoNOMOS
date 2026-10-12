import P42ContextualSeparation

/- EvoNOMOS P42-P2-R4. Finite two-source-architecture edit game.
   Real unchanged Echo v4 executions are separately verified by Go CI.
   This Lean file proves properties of a restricted demand/edit model only;
   it does not mechanically derive Go semantics from its source. -/
namespace P42R4

inductive Architecture where
  | single
  | split
  deriving Repr, DecidableEq

inductive Demand where
  | legacy
  | deny
  deriving Repr, DecidableEq

inductive SourceEdit where
  | noop
  | addFallback
  | removeFallback
  deriving Repr, DecidableEq

/- Present D0 client-observation vector is identical by construction.
   Its source-realization is checked separately in original Go source. -/
def presentObservation (_ : Architecture) : Nat × Nat := (200, 200)

def fallbackPresent : Architecture → Bool
  | .single => false
  | .split => true

def target : Demand → Architecture
  | .legacy => .split
  | .deny => .single

def requiredExtraEdits (a : Architecture) (d : Demand) : Nat :=
  if a == target d then 0 else 1

/- Exactly the source-authorized add/remove/no-op edit grammar. -/
def step : Architecture → SourceEdit → Option Architecture
  | .single, .noop => some .single
  | .single, .addFallback => some .split
  | .single, .removeFallback => none
  | .split, .noop => some .split
  | .split, .addFallback => none
  | .split, .removeFallback => some .single

def editCost : SourceEdit → Nat
  | .noop => 0
  | .addFallback => 1
  | .removeFallback => 1

def predictionFromStructuralBit (b : Bool) (d : Demand) : Nat :=
  match b,d with
  | false,.legacy => 1
  | false,.deny => 0
  | true,.legacy => 0
  | true,.deny => 1

theorem source_fallback_bit_suffices_for_both_future_costs
    (a : Architecture) (d : Demand) :
    predictionFromStructuralBit (fallbackPresent a) d =
      requiredExtraEdits a d := by
  cases a <;> cases d <;> decide

theorem equal_present_observations :
    presentObservation .single = presentObservation .split := by rfl

theorem opposite_future_edit_preferences :
    requiredExtraEdits .single .legacy = 1 ∧
    requiredExtraEdits .split .legacy = 0 ∧
    requiredExtraEdits .single .deny = 0 ∧
    requiredExtraEdits .split .deny = 1 := by decide

theorem repair_cost_cannot_factor_through_present_behavior :
    ¬ ∃ f : (Nat × Nat) → Demand → Nat,
        ∀ a d, requiredExtraEdits a d =
          f (presentObservation a) d := by
  rintro ⟨f, h⟩
  have a := h .single .legacy
  have b := h .split .legacy
  have mismatch :
    requiredExtraEdits .single .legacy ≠
      requiredExtraEdits .split .legacy := by decide
  apply mismatch
  calc
    requiredExtraEdits .single .legacy =
      f (presentObservation .single) .legacy := a
    _ = f (presentObservation .split) .legacy := rfl
    _ = requiredExtraEdits .split .legacy := b.symm

theorem source_edit_domain_also_not_present_behavior_determined :
    step .single .addFallback = some .split ∧
    step .split .addFallback = none ∧
    presentObservation .single = presentObservation .split := by decide

def applyDemand (a : Architecture) (d : Demand) : Architecture × Nat :=
  (target d, requiredExtraEdits a d)

def runDemands (a : Architecture) (ds : List Demand) : Architecture × Nat :=
  ds.foldl (fun current d =>
    let next := applyDemand current.1 d
    (next.1, current.2 + next.2)) (a, 0)

theorem order_dependent_source_path_lengths :
    (runDemands .single [.legacy, .deny]).2 = 2 ∧
    (runDemands .single [.deny, .legacy]).2 = 1 ∧
    (runDemands .split [.legacy, .deny]).2 = 1 ∧
    (runDemands .split [.deny, .legacy]).2 = 2 := by decide

theorem repeated_demand_does_not_reedit :
    (runDemands .single [.legacy, .legacy]).2 = 1 ∧
    (runDemands .split [.deny, .deny]).2 = 1 := by decide

/- Explicit mathematical scope: adding one structural Boolean recovers all
   predicted one-step cost labels for this two-state family, while the
   present-behavior quotient fails to recover them. This is a classical
   distinguishability/factorization argument, NOT a new theorem about OO. -/
theorem one_bit_is_sufficient_but_zero_behavioral_information_is_not :
    (∀ a d, predictionFromStructuralBit (fallbackPresent a) d =
      requiredExtraEdits a d) ∧
    ¬ (∃ f : (Nat × Nat) → Demand → Nat,
        ∀ a d, requiredExtraEdits a d = f (presentObservation a) d) := by
  exact ⟨source_fallback_bit_suffices_for_both_future_costs,
         repair_cost_cannot_factor_through_present_behavior⟩

end P42R4
