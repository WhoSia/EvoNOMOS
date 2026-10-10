import Init

/- EvoNOMOS Generation VIII LAW-R1-P42-P0.
   Three-valued evidentiary judgement and declared client observation vector.
   This is a finite mathematical CONTRACT, NOT semantics of Echo/httprouter or
   proof that platform operations imply institutional change authorization.
   Proofs carry no axioms, sorry or admits. -/
namespace P42

inductive RightsEvidence where
  | unknown
  | platformOperationObserved
  | versionedPolicyVerified
  deriving Repr, DecidableEq

def permissionEligible : RightsEvidence → Bool
  | .unknown => false
  | .platformOperationObserved => false
  | .versionedPolicyVerified => true

structure ClientObservation where
  status : Nat
  body : Nat
  header : Nat
  selectedHandler : Nat
  handlerEffects : Nat
  deriving Repr, DecidableEq

def responseProjection (o : ClientObservation) : Nat × Nat :=
  (o.status, o.body)

def controlObservation : ClientObservation :=
  {status := 200, body := 1, header := 2, selectedHandler := 3,
   handlerEffects := 1}
def hiddenChangedObservation : ClientObservation :=
  {status := 200, body := 1, header := 4, selectedHandler := 5,
   handlerEffects := 0}

theorem response_projection_cannot_certify_full_contract :
    responseProjection controlObservation =
      responseProjection hiddenChangedObservation ∧
    controlObservation ≠ hiddenChangedObservation := by decide

structure ProposedEdit where
  sourceAdmitted : Bool
  before : ClientObservation
  after : ClientObservation
  rights : RightsEvidence
  providerCapabilityEvidenced : Bool
  deriving Repr

inductive Evaluation where
  | sourceRejected
  | clientContractViolated
  | dependencyUnverified
  | authorityUnverified
  | boundedEligible
  deriving Repr, DecidableEq

/- Priority ordering is a declared policy for the SELECTED test harness:
   Source admission, old observation, provider evidence, then authority.
   A boundedEligible classification is NOT a legal permission claim. -/
def evaluate (w : ProposedEdit) : Evaluation :=
  if !w.sourceAdmitted then .sourceRejected
  else if w.before != w.after then .clientContractViolated
  else if !w.providerCapabilityEvidenced then .dependencyUnverified
  else if !permissionEligible w.rights then .authorityUnverified
  else .boundedEligible

def admittedButBreaking : ProposedEdit :=
  {sourceAdmitted := true,
   before := controlObservation,
   after := hiddenChangedObservation,
   rights := .versionedPolicyVerified,
   providerCapabilityEvidenced := true}

def preservedButHistoricallyUnknown : ProposedEdit :=
  {sourceAdmitted := true,
   before := controlObservation,
   after := controlObservation,
   rights := .platformOperationObserved,
   providerCapabilityEvidenced := true}

def preservedWithFixtureCertificate : ProposedEdit :=
  {sourceAdmitted := true,
   before := controlObservation,
   after := controlObservation,
   rights := .versionedPolicyVerified,
   providerCapabilityEvidenced := true}

theorem admission_alone_does_not_entail_client_preservation :
    admittedButBreaking.sourceAdmitted = true ∧
    admittedButBreaking.before ≠ admittedButBreaking.after := by decide

theorem admitted_but_breaking_rejected_by_client_guard :
    evaluate admittedButBreaking = .clientContractViolated := by decide

theorem observed_platform_operation_not_historical_policy :
    permissionEligible RightsEvidence.platformOperationObserved = false := by rfl

theorem no_certification_for_missing_history :
    evaluate preservedButHistoricallyUnknown = .authorityUnverified := by decide

theorem certificate_is_only_conditional_to_declared_fixture :
    evaluate preservedWithFixtureCertificate = .boundedEligible := by decide

theorem bounded_eligible_needs_explicit_guards
    (w : ProposedEdit)
    (h : evaluate w = .boundedEligible) :
    w.sourceAdmitted = true ∧ w.before = w.after ∧
    w.providerCapabilityEvidenced = true ∧
    permissionEligible w.rights = true := by
  unfold evaluate at h
  split at h
  · contradiction
  · split at h
    · contradiction
    · split at h
      · contradiction
      · split at h
        · contradiction
        · rename_i admission hv provider rights
          -- All if guards evaluated to false along the eligible path.
          simp_all

/- The lemma above is about the declared evaluate definition, not an
   external new law. Operational original-Go and GitHub provenance needed. -/
end P42
