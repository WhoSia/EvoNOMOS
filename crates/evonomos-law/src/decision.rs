use anyhow::{anyhow, Result};
use serde::{Deserialize, Serialize};
use std::collections::BTreeSet;

#[derive(Debug, Deserialize)]
pub struct LawSurfaceEnvelope {
    pub protocol_version: String,
    pub evidence: Vec<EvidenceWorld>,
    pub prospective_context: ProspectiveContext,
}

#[derive(Debug, Deserialize)]
pub struct EvidenceWorld {
    pub world_id: String,
    pub evidence_class: String,
    pub observed: ObservedEvidence,
}

#[derive(Debug, Deserialize)]
pub struct ObservedEvidence {
    pub outcomes_opened: bool,
    pub surface_reversal: Option<bool>,
    pub surface_discrimination: Option<bool>,
    pub churn_reversal: Option<bool>,
    pub capability_burden_reduction: Option<bool>,
}

#[derive(Debug, Deserialize)]
pub struct ProspectiveContext {
    pub context_id: String,
    pub existing_boundary: String,
    pub membership_fanout: u64,
    pub shared_mechanism_fraction: String,
    pub boundary_capabilities: Vec<String>,
    pub demanded_capabilities: Vec<String>,
    pub future_same_family_demand: String,
    pub heterogeneity: String,
}

#[derive(Debug, Serialize)]
pub struct LawSurfaceProjection {
    pub protocol_version: &'static str,
    pub authority: &'static str,
    pub cil_c1_evidence: &'static str,
    pub cbl_c1_evidence: &'static str,
    pub coordinate_noncollapse: bool,
    pub p12_full_corequirement_cell: &'static str,
    pub context_id: String,
    pub membership_propagation_pressure: &'static str,
    pub capability_bundle_mismatch: &'static str,
    pub mismatch_width: usize,
    pub uncovered_demand_capabilities: Vec<String>,
    pub candidate_tests: Vec<&'static str>,
    pub abstention_reasons: Vec<&'static str>,
    pub decision_authority: &'static str,
    pub scalarization: bool,
    pub winner: Option<String>,
    pub cil_c1_falsifiers: Vec<&'static str>,
    pub cbl_c1_falsifiers: Vec<&'static str>,
    pub prohibited_inference: Vec<&'static str>,
}

fn fraction(s: &str) -> Result<(u64, u64)> {
    let (n, d) = s
        .split_once('/')
        .ok_or_else(|| anyhow!("shared_mechanism_fraction must be N/D"))?;
    let n: u64 = n.trim().parse()?;
    let d: u64 = d.trim().parse()?;
    if d == 0 || n > d {
        return Err(anyhow!("invalid shared_mechanism_fraction"));
    }
    Ok((n, d))
}

fn world<'a>(env: &'a LawSurfaceEnvelope, id: &str) -> Result<&'a EvidenceWorld> {
    env.evidence
        .iter()
        .find(|w| w.world_id == id)
        .ok_or_else(|| anyhow!("missing evidence world {id}"))
}

fn validate_evidence(env: &LawSurfaceEnvelope) -> Result<()> {
    let p10 = world(env, "P10_MIKROTIK")?;
    if p10.evidence_class != "EXPLORATORY_ONLY"
        || !p10.observed.outcomes_opened
        || p10.observed.surface_reversal != Some(true)
        || p10.observed.churn_reversal != Some(false)
    {
        return Err(anyhow!("P10 evidence contract mismatch"));
    }

    let p11 = world(env, "P11_TRUEFORGE")?;
    if p11.evidence_class != "REAL_TWO_DEMAND"
        || !p11.observed.outcomes_opened
        || p11.observed.surface_discrimination != Some(false)
        || p11.observed.churn_reversal != Some(true)
        || p11.observed.capability_burden_reduction != Some(true)
    {
        return Err(anyhow!("P11 evidence contract mismatch"));
    }

    let p12 = world(env, "P12_RESTIC")?;
    if p12.evidence_class != "TERMINAL_NONRESULT" || p12.observed.outcomes_opened {
        return Err(anyhow!(
            "P12 must remain terminal non-result with outcomes closed"
        ));
    }
    Ok(())
}

pub fn project_law_surface(env: LawSurfaceEnvelope) -> Result<LawSurfaceProjection> {
    if env.protocol_version != "0.6" {
        return Err(anyhow!("protocol_version must be 0.6"));
    }
    validate_evidence(&env)?;

    let c = env.prospective_context;
    let (shared_n, shared_d) = fraction(&c.shared_mechanism_fraction)?;
    let boundary: BTreeSet<String> = c.boundary_capabilities.iter().cloned().collect();
    let demand: BTreeSet<String> = c.demanded_capabilities.iter().cloned().collect();
    let extraneous: Vec<String> = boundary.difference(&demand).cloned().collect();
    let missing: Vec<String> = demand.difference(&boundary).cloned().collect();

    let membership_pressure = if c.existing_boundary == "ABSENT"
        && c.membership_fanout > 1
        && shared_n > 0
        && shared_d > 1
    {
        "PRESENT"
    } else if c.existing_boundary != "ABSENT" {
        "BOUNDED_BY_EXISTING_BOUNDARY"
    } else {
        "LIMITED"
    };

    let bundle_mismatch = if !extraneous.is_empty() {
        "PRESENT"
    } else if !boundary.is_empty() && missing.is_empty() && boundary == demand {
        "ABSENT_FULL_COREQUIREMENT"
    } else {
        "ABSENT_OR_NOT_APPLICABLE"
    };

    let mut candidate_tests = Vec::new();
    if membership_pressure == "PRESENT" {
        candidate_tests.push("TEST_MEMBERSHIP_CENTRALIZATION_VS_DIRECT");
    }
    if bundle_mismatch == "PRESENT" {
        candidate_tests.push("TEST_CAPABILITY_SEGREGATION_VS_BUNDLE_REUSE");
    }

    let mut abstention_reasons =
        vec!["NO_ARCHITECTURE_RECOMMENDATION_WITHOUT_PAIRED_LIFECYCLE_EVIDENCE"];
    if c.existing_boundary != "ABSENT" {
        abstention_reasons.push("CIL_C1_MEMBERSHIP_SAVING_NOT_INFERRED_WITH_EXISTING_BOUNDARY");
    }
    if bundle_mismatch == "ABSENT_FULL_COREQUIREMENT" {
        abstention_reasons.push("CBL_C1_FULL_COREQUIREMENT_CELL_UNRESOLVED");
    }
    if c.future_same_family_demand == "UNKNOWN" {
        abstention_reasons.push("FUTURE_SAME_FAMILY_DEMAND_UNKNOWN");
    }
    if !missing.is_empty() {
        abstention_reasons.push("CURRENT_BOUNDARY_DOES_NOT_COVER_FROZEN_DEMAND");
    }

    let decision_authority = if !missing.is_empty() {
        "ABSTAIN_INVALID_CAPABILITY_COVERAGE"
    } else if candidate_tests.is_empty() {
        "ABSTAIN_NO_MATCHED_MECHANISM"
    } else {
        "SELECT_PROSPECTIVE_RIVAL_TESTS_ONLY"
    };

    Ok(LawSurfaceProjection {
        protocol_version: "0.6",
        authority: "LAW_R1_P0_CONSTITUTION_ONLY",
        cil_c1_evidence: "EXPLORATORY_MECHANISM_PLUS_BOUNDARY_EVIDENCE__NO_GENERAL_RECOMMENDATION",
        cbl_c1_evidence: "NARROW_MECHANISM_SUPPORT__FULL_COREQUIREMENT_FALSIFIER_UNRESOLVED",
        coordinate_noncollapse: true,
        p12_full_corequirement_cell: "UNRESOLVED_TERMINAL_NONRESULT",
        context_id: c.context_id,
        membership_propagation_pressure: membership_pressure,
        capability_bundle_mismatch: bundle_mismatch,
        mismatch_width: extraneous.len(),
        uncovered_demand_capabilities: missing,
        candidate_tests,
        abstention_reasons,
        decision_authority,
        scalarization: false,
        winner: None,
        cil_c1_falsifiers: vec![
            "PREEXISTING_BOUNDARY_COLLAPSES_MEMBERSHIP_SURFACE_DIFFERENCE",
            "LOW_OR_LOCAL_MEMBERSHIP_FANOUT",
            "NO_REPEATED_SAME_FAMILY_MEMBERSHIP_CHANGE",
        ],
        cbl_c1_falsifiers: vec![
            "DEMAND_COREQUIRES_FULL_BOUNDARY_BUNDLE",
            "SEGREGATION_BIRTH_TAX_DOMINATES_LIFECYCLE",
            "NO_TRUTHFUL_DEMAND_EXTRANEOUS_CONFORMANCE_OBLIGATION",
        ],
        prohibited_inference: vec![
            "SOLID_IS_VALIDATED",
            "DIP_IS_UNIVERSALLY_BETTER",
            "ISP_IS_UNIVERSALLY_BETTER",
            "ONE_MAINTAINABILITY_SCALAR_SUBSTITUTES_FOR_S_L_C_A",
            "P12_NONRESULT_COUNTS_AS_CBL_C1_FALSIFICATION",
        ],
    })
}

#[cfg(test)]
mod tests {
    use super::*;

    fn evidence() -> Vec<EvidenceWorld> {
        vec![
            EvidenceWorld {
                world_id: "P10_MIKROTIK".into(),
                evidence_class: "EXPLORATORY_ONLY".into(),
                observed: ObservedEvidence {
                    outcomes_opened: true,
                    surface_reversal: Some(true),
                    surface_discrimination: Some(true),
                    churn_reversal: Some(false),
                    capability_burden_reduction: None,
                },
            },
            EvidenceWorld {
                world_id: "P11_TRUEFORGE".into(),
                evidence_class: "REAL_TWO_DEMAND".into(),
                observed: ObservedEvidence {
                    outcomes_opened: true,
                    surface_reversal: Some(false),
                    surface_discrimination: Some(false),
                    churn_reversal: Some(true),
                    capability_burden_reduction: Some(true),
                },
            },
            EvidenceWorld {
                world_id: "P12_RESTIC".into(),
                evidence_class: "TERMINAL_NONRESULT".into(),
                observed: ObservedEvidence {
                    outcomes_opened: false,
                    surface_reversal: None,
                    surface_discrimination: None,
                    churn_reversal: None,
                    capability_burden_reduction: None,
                },
            },
        ]
    }

    #[test]
    fn mismatch_selects_test_not_winner() {
        let out = project_law_surface(LawSurfaceEnvelope {
            protocol_version: "0.6".into(),
            evidence: evidence(),
            prospective_context: ProspectiveContext {
                context_id: "X".into(),
                existing_boundary: "STRONG".into(),
                membership_fanout: 8,
                shared_mechanism_fraction: "3/4".into(),
                boundary_capabilities: vec!["search".into(), "fetch".into()],
                demanded_capabilities: vec!["search".into()],
                future_same_family_demand: "OBSERVED_OR_PLAUSIBLE".into(),
                heterogeneity: "HIGH".into(),
            },
        })
        .unwrap();
        assert_eq!(
            out.candidate_tests,
            vec!["TEST_CAPABILITY_SEGREGATION_VS_BUNDLE_REUSE"]
        );
        assert_eq!(
            out.decision_authority,
            "SELECT_PROSPECTIVE_RIVAL_TESTS_ONLY"
        );
        assert!(!out.scalarization);
        assert!(out.winner.is_none());
    }
}
