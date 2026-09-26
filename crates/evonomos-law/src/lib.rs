mod world;
pub use world::*;

use anyhow::{anyhow, Result};
use serde::{Deserialize, Serialize};

#[derive(Debug, Deserialize)]
pub struct ModeratorEnvelope {
    pub vector: ModeratorVector,
}

#[derive(Debug, Deserialize)]
pub struct ModeratorVector {
    pub existing_provider_family_cardinality: u64,
    pub canonical_provider_membership_surface_fanout: u64,
    pub shared_transport_fraction: FractionField,
    pub payload_heterogeneity: String,
    pub authentication_heterogeneity: String,
    pub configuration_heterogeneity: String,
    pub existing_polymorphic_provider_boundary: bool,
}

#[derive(Debug, Deserialize)]
pub struct FractionField {
    pub value: String,
}

#[derive(Debug, Serialize)]
pub struct LawInspection {
    pub law_candidate: &'static str,
    pub authority: &'static str,
    pub observations: ObservationVector,
    pub mechanism_channels: MechanismChannels,
    pub prohibited_inference: Vec<&'static str>,
}

#[derive(Debug, Serialize)]
pub struct ObservationVector {
    pub provider_family_cardinality: u64,
    pub membership_surface_fanout: u64,
    pub shared_transport_fraction: String,
    pub payload_heterogeneity: String,
    pub authentication_heterogeneity: String,
    pub configuration_heterogeneity: String,
    pub existing_polymorphic_boundary: bool,
}

#[derive(Debug, Serialize)]
pub struct MechanismChannels {
    pub membership_propagation_opportunity: &'static str,
    pub shared_mechanism_opportunity: &'static str,
    pub heterogeneity_resistance: String,
    pub boundary_redundancy_pressure: &'static str,
    pub future_same_family_demand: &'static str,
    pub decision_authority: &'static str,
}

#[derive(Debug, Deserialize)]
pub struct LifecycleExposure {
    pub vectors: LifecycleVectors,
}

#[derive(Debug, Deserialize)]
pub struct LifecycleVectors {
    #[serde(rename = "DIRECT_DEDICATED")]
    pub direct: LifecycleVector,
    #[serde(rename = "INVERT_CHANNEL_ADAPTER")]
    pub invert: LifecycleVector,
}

#[derive(Debug, Deserialize)]
#[allow(non_snake_case)]
pub struct LifecycleVector {
    pub S0: i64,
    pub L0: i64,
    pub Q0: i64,
    pub S1: i64,
    pub L1: i64,
    pub Q1: i64,
}

#[derive(Debug, Deserialize)]
pub struct AuthorityFirewall {
    pub lawkit_required_authority: String,
    pub forbidden: Vec<String>,
}

#[derive(Debug, Serialize, PartialEq, Eq)]
pub struct PhasePair {
    pub phase0: String,
    pub phase1: String,
}

#[derive(Debug, Serialize, PartialEq, Eq)]
pub struct PhasewiseDirection {
    pub surface: PhasePair,
    pub churn: PhasePair,
}

#[derive(Debug, Serialize, PartialEq, Eq)]
pub struct ReversalState {
    pub surface: bool,
    pub churn: bool,
}

#[derive(Debug, Serialize, PartialEq, Eq)]
pub struct LifecyclePattern {
    pub surface: String,
    pub churn: String,
}

#[derive(Debug, Serialize)]
pub struct ModeratorContext {
    pub membership_surface_fanout: u64,
    pub shared_transport_fraction: String,
    pub payload_heterogeneity: String,
    pub authentication_heterogeneity: String,
    pub configuration_heterogeneity: String,
    pub existing_polymorphic_boundary: bool,
}

#[derive(Debug, Serialize)]
pub struct LawAdjudication {
    pub law_candidate: &'static str,
    pub authority: String,
    pub evidence_class: &'static str,
    pub phasewise_direction: PhasewiseDirection,
    pub reversal: ReversalState,
    pub lifecycle_pattern: LifecyclePattern,
    pub moderator_context: ModeratorContext,
    pub cil_c1_update: &'static str,
    pub decision_authority: &'static str,
    pub prohibited_inference: Vec<String>,
}

pub fn parse_fraction(s: &str) -> Result<(u64, u64)> {
    let (a, b) = s
        .split_once('/')
        .ok_or_else(|| anyhow!("fraction must be N/D, got {s}"))?;
    let n: u64 = a.trim().parse()?;
    let d: u64 = b.trim().parse()?;
    if d == 0 {
        return Err(anyhow!("fraction denominator must be non-zero"));
    }
    if n > d {
        return Err(anyhow!("fraction numerator cannot exceed denominator"));
    }
    Ok((n, d))
}

pub fn inspect(env: ModeratorEnvelope) -> Result<LawInspection> {
    let v = env.vector;
    let (shared_n, shared_d) = parse_fraction(&v.shared_transport_fraction.value)?;

    let fanout = if v.canonical_provider_membership_surface_fanout > 1 {
        "PRESENT"
    } else {
        "LIMITED"
    };
    let shared = if shared_n > 0 && shared_d > 1 {
        "PRESENT"
    } else {
        "LIMITED"
    };
    let redundancy = if v.existing_polymorphic_provider_boundary {
        "PRESENT"
    } else {
        "ABSENT"
    };

    let heterogeneity = format!(
        "payload={};auth={};config={}",
        v.payload_heterogeneity, v.authentication_heterogeneity, v.configuration_heterogeneity
    );

    Ok(LawInspection {
        law_candidate: "CIL-C1",
        authority: "HYPOTHESIS_ONLY_PRE_OUTCOME",
        observations: ObservationVector {
            provider_family_cardinality: v.existing_provider_family_cardinality,
            membership_surface_fanout: v.canonical_provider_membership_surface_fanout,
            shared_transport_fraction: v.shared_transport_fraction.value,
            payload_heterogeneity: v.payload_heterogeneity,
            authentication_heterogeneity: v.authentication_heterogeneity,
            configuration_heterogeneity: v.configuration_heterogeneity,
            existing_polymorphic_boundary: v.existing_polymorphic_provider_boundary,
        },
        mechanism_channels: MechanismChannels {
            membership_propagation_opportunity: fanout,
            shared_mechanism_opportunity: shared,
            heterogeneity_resistance: heterogeneity,
            boundary_redundancy_pressure: redundancy,
            future_same_family_demand: "UNOBSERVED",
            decision_authority: "ABSTAIN_PRE_OUTCOME",
        },
        prohibited_inference: vec![
            "SOLID_IS_TRUE",
            "DIP_IS_UNIVERSALLY_BETTER",
            "INVERT_IS_RECOMMENDED_WITHOUT_LIFECYCLE_EVIDENCE",
            "SAME_SIGN_REPLICATION_IS_SUFFICIENT_AUTHORITY",
        ],
    })
}

fn direction(direct: i64, invert: i64) -> String {
    if direct == invert {
        "EQUAL".to_string()
    } else if direct > invert {
        "DIRECT_HIGHER".to_string()
    } else {
        "INVERT_HIGHER".to_string()
    }
}

fn reversal(pair: &PhasePair) -> bool {
    pair.phase0 != "EQUAL" && pair.phase1 != "EQUAL" && pair.phase0 != pair.phase1
}

fn pattern(pair: &PhasePair) -> String {
    match (pair.phase0.as_str(), pair.phase1.as_str()) {
        ("INVERT_HIGHER", "DIRECT_HIGHER") => {
            "INITIAL_INVERSION_TAX_THEN_PROPAGATION_SAVING".to_string()
        }
        ("DIRECT_HIGHER", "INVERT_HIGHER") => {
            "INITIAL_DIRECT_TAX_THEN_INVERSION_FOLLOWUP_TAX".to_string()
        }
        (a, b) if a == b => "NO_SIGN_REVERSAL".to_string(),
        _ => "MIXED_OR_EQUAL".to_string(),
    }
}

pub fn adjudicate(
    env: ModeratorEnvelope,
    lifecycle: LifecycleExposure,
    firewall: AuthorityFirewall,
) -> Result<LawAdjudication> {
    let d = lifecycle.vectors.direct;
    let i = lifecycle.vectors.invert;
    if d.Q0 != 1 || d.Q1 != 1 || i.Q0 != 1 || i.Q1 != 1 {
        return Err(anyhow!("all lifecycle validity gates must equal 1"));
    }

    let surface = PhasePair {
        phase0: direction(d.S0, i.S0),
        phase1: direction(d.S1, i.S1),
    };
    let churn = PhasePair {
        phase0: direction(d.L0, i.L0),
        phase1: direction(d.L1, i.L1),
    };
    let reversals = ReversalState {
        surface: reversal(&surface),
        churn: reversal(&churn),
    };
    let patterns = LifecyclePattern {
        surface: pattern(&surface),
        churn: pattern(&churn),
    };
    let v = env.vector;

    Ok(LawAdjudication {
        law_candidate: "CIL-C1",
        authority: firewall.lawkit_required_authority,
        evidence_class: "EXPLORATORY_ONLY",
        phasewise_direction: PhasewiseDirection { surface, churn },
        reversal: reversals,
        lifecycle_pattern: patterns,
        moderator_context: ModeratorContext {
            membership_surface_fanout: v.canonical_provider_membership_surface_fanout,
            shared_transport_fraction: v.shared_transport_fraction.value,
            payload_heterogeneity: v.payload_heterogeneity,
            authentication_heterogeneity: v.authentication_heterogeneity,
            configuration_heterogeneity: v.configuration_heterogeneity,
            existing_polymorphic_boundary: v.existing_polymorphic_provider_boundary,
        },
        cil_c1_update: "FORBIDDEN_CONFIRMATORY_UPDATE",
        decision_authority: "ABSTAIN",
        prohibited_inference: firewall.forbidden,
    })
}

#[cfg(test)]
mod tests {
    use super::*;

    fn sample() -> ModeratorEnvelope {
        ModeratorEnvelope {
            vector: ModeratorVector {
                existing_provider_family_cardinality: 5,
                canonical_provider_membership_surface_fanout: 7,
                shared_transport_fraction: FractionField {
                    value: "4/5".to_string(),
                },
                payload_heterogeneity: "HIGH".to_string(),
                authentication_heterogeneity: "HIGH".to_string(),
                configuration_heterogeneity: "HIGH".to_string(),
                existing_polymorphic_provider_boundary: false,
            },
        }
    }

    #[test]
    fn parses_fraction() {
        assert_eq!(parse_fraction("4/5").unwrap(), (4, 5));
        assert!(parse_fraction("2/0").is_err());
        assert!(parse_fraction("6/5").is_err());
    }

    #[test]
    fn cil_c1_preoutcome_abstains() {
        let out = inspect(sample()).unwrap();
        assert_eq!(out.law_candidate, "CIL-C1");
        assert_eq!(
            out.mechanism_channels.membership_propagation_opportunity,
            "PRESENT"
        );
        assert_eq!(
            out.mechanism_channels.shared_mechanism_opportunity,
            "PRESENT"
        );
        assert_eq!(
            out.mechanism_channels.boundary_redundancy_pressure,
            "ABSENT"
        );
        assert_eq!(
            out.mechanism_channels.decision_authority,
            "ABSTAIN_PRE_OUTCOME"
        );
    }

    #[test]
    fn postoutcome_authority_ceiling_is_preserved() {
        let lifecycle = LifecycleExposure {
            vectors: LifecycleVectors {
                direct: LifecycleVector {
                    S0: 7,
                    L0: 20,
                    Q0: 1,
                    S1: 7,
                    L1: 14,
                    Q1: 1,
                },
                invert: LifecycleVector {
                    S0: 8,
                    L0: 30,
                    Q0: 1,
                    S1: 4,
                    L1: 8,
                    Q1: 1,
                },
            },
        };
        let firewall = AuthorityFirewall {
            lawkit_required_authority: "HOLD_SELECTION_BLINDNESS".to_string(),
            forbidden: vec!["overall winner".to_string()],
        };
        let out = adjudicate(sample(), lifecycle, firewall).unwrap();
        assert_eq!(out.authority, "HOLD_SELECTION_BLINDNESS");
        assert_eq!(out.decision_authority, "ABSTAIN");
        assert!(out.reversal.surface);
        assert!(out.reversal.churn);
    }
}
