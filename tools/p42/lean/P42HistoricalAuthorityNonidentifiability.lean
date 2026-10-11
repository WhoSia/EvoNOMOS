import P42EvidenceJudgement

/- P42-P1: open-world, time-indexed platform governance evidence.
   The propositions are MATHEMATICAL: they are not a Go semantics model,
   an authenticated historical policy reconstruction or a legal mandate.
   Independent source replay must separately validate public metadata. -/
namespace P42P1

inductive Verdict where
  | permitted
  | contradicted
  | unknown
  deriving Repr, DecidableEq

structure PublicSnapshot where
  mergeObserved : Bool
  visibleCurrentRuleset : Bool
  currentRequiredApprovalsZero : Bool
  rulesetCreationOrder : Nat
  rulesetLastUpdateOrder : Nat
  mergeEventOrder : Nat
  observedCommentReviews : Nat
  deriving Repr, DecidableEq

def echoObserved : PublicSnapshot :=
  { mergeObserved := true
    visibleCurrentRuleset := true
    currentRequiredApprovalsZero := true
    rulesetCreationOrder := 1
    rulesetLastUpdateOrder := 2
    mergeEventOrder := 3
    observedCommentReviews := 2 }

def temporallyCompatible (s : PublicSnapshot) : Prop :=
  s.rulesetCreationOrder ≤ s.rulesetLastUpdateOrder ∧
  s.rulesetLastUpdateOrder ≤ s.mergeEventOrder

theorem echo_public_metadata_temporal_order :
    temporallyCompatible echoObserved := by decide

/- These are separate evidence sources; a CURRENT ruleset's numeric review
   minimum does NOT attest all historical legacy/organization layers. -/
structure HistoryEvidence where
  publicView : PublicSnapshot
  ruleVersionAtMerge : Option Bool
  legacyProtectionAtMerge : Option Bool
  organizationPolicyAtMerge : Option Bool
  actorEligibleAtMerge : Option Bool
  institutionalMandate : Option Bool
  deriving Repr, DecidableEq

def evidenceVerdict (w : HistoryEvidence) : Verdict :=
  match w.ruleVersionAtMerge, w.legacyProtectionAtMerge,
        w.organizationPolicyAtMerge, w.actorEligibleAtMerge,
        w.institutionalMandate with
  | some r, some l, some o, some a, some m =>
      if r && l && o && a && m then .permitted else .contradicted
  | _, _, _, _, _ => .unknown

def sourceOnly : HistoryEvidence :=
  { publicView := echoObserved
    ruleVersionAtMerge := none
    legacyProtectionAtMerge := none
    organizationPolicyAtMerge := none
    actorEligibleAtMerge := none
    institutionalMandate := none }

theorem public_merge_and_ruleset_do_not_certify_permission :
    sourceOnly.publicView.mergeObserved = true ∧
    sourceOnly.publicView.currentRequiredApprovalsZero = true ∧
    evidenceVerdict sourceOnly = .unknown := by decide

def hypothesizedAllEligible : HistoryEvidence :=
  { publicView := echoObserved
    ruleVersionAtMerge := some true
    legacyProtectionAtMerge := some true
    organizationPolicyAtMerge := some true
    actorEligibleAtMerge := some true
    institutionalMandate := some true }

def hypothesizedHiddenRestriction : HistoryEvidence :=
  { publicView := echoObserved
    ruleVersionAtMerge := some true
    legacyProtectionAtMerge := some false
    organizationPolicyAtMerge := some true
    actorEligibleAtMerge := some true
    institutionalMandate := some true }

theorem public_view_cannot_disambiguate_hidden_branch_protection :
    hypothesizedAllEligible.publicView =
      hypothesizedHiddenRestriction.publicView ∧
    evidenceVerdict hypothesizedAllEligible = .permitted ∧
    evidenceVerdict hypothesizedHiddenRestriction = .contradicted := by decide

theorem no_public_snapshot_total_authority_classifier :
    ¬ ∃ f : PublicSnapshot → Verdict, ∀ w : HistoryEvidence,
      evidenceVerdict w = f w.publicView := by
  rintro ⟨f, h⟩
  have a := h hypothesizedAllEligible
  have b := h hypothesizedHiddenRestriction
  have same : hypothesizedAllEligible.publicView =
      hypothesizedHiddenRestriction.publicView := by decide
  have diff : evidenceVerdict hypothesizedAllEligible ≠
      evidenceVerdict hypothesizedHiddenRestriction := by decide
  apply diff
  calc
    evidenceVerdict hypothesizedAllEligible =
      f hypothesizedAllEligible.publicView := a
    _ = f hypothesizedHiddenRestriction.publicView := congrArg f same
    _ = evidenceVerdict hypothesizedHiddenRestriction := b.symm

/- The actual historical "no policy" is not the same as "policy unobserved".
   Both concrete witness worlds are hypothetical; no allegation about
   labstack/echo or any named actor follows from this existence proof. -/
theorem absent_past_policy_data_stays_unknown :
    evidenceVerdict sourceOnly = .unknown := by decide

theorem successful_platform_merge_not_sufficient_to_classify :
    echoObserved.mergeObserved = true ∧
    evidenceVerdict sourceOnly ≠ .permitted := by decide

/- A complete declared record is enough to evaluate *this definition*.
   Such a record has NOT been obtained for the observed Echo PR. -/
theorem model_complete_record_positive :
    evidenceVerdict hypothesizedAllEligible = .permitted := by decide

end P42P1
