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
        v.payload_heterogeneity,
        v.authentication_heterogeneity,
        v.configuration_heterogeneity
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
        assert_eq!(out.mechanism_channels.membership_propagation_opportunity, "PRESENT");
        assert_eq!(out.mechanism_channels.shared_mechanism_opportunity, "PRESENT");
        assert_eq!(out.mechanism_channels.boundary_redundancy_pressure, "ABSENT");
        assert_eq!(out.mechanism_channels.decision_authority, "ABSTAIN_PRE_OUTCOME");
    }
}
