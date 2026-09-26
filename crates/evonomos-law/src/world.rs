use serde::{Deserialize, Serialize};

const GATES: [&str; 7] = [
    "exact_source_locked",
    "independent_real_initial_demand",
    "independent_real_followup_demand",
    "pair_frozen_before_treatment",
    "discriminates_prior_world",
    "outcome_surface_frozen",
    "observability_firewall_frozen",
];

#[derive(Debug, Deserialize)]
pub struct WorldEnvelope {
    pub protocol_version: String,
    pub world_id: String,
    pub moderators: WorldModerators,
    pub admission_gates: WorldAdmissionGates,
}

#[derive(Debug, Deserialize)]
pub struct WorldModerators {
    pub membership_surface_fanout: u64,
    pub existing_runtime_interface: bool,
    pub existing_interface_capabilities: Vec<String>,
    pub initial_demand_capabilities: Vec<String>,
    pub followup_demand_capabilities: Vec<String>,
    pub capability_bundle_mismatch: bool,
}

#[derive(Debug, Deserialize)]
pub struct WorldAdmissionGates {
    pub exact_source_locked: bool,
    pub independent_real_initial_demand: bool,
    pub independent_real_followup_demand: bool,
    pub pair_frozen_before_treatment: bool,
    pub discriminates_prior_world: bool,
    pub outcome_surface_frozen: bool,
    pub observability_firewall_frozen: bool,
}

impl WorldAdmissionGates {
    fn all_pass(&self) -> bool {
        self.exact_source_locked
            && self.independent_real_initial_demand
            && self.independent_real_followup_demand
            && self.pair_frozen_before_treatment
            && self.discriminates_prior_world
            && self.outcome_surface_frozen
            && self.observability_firewall_frozen
    }

    fn pairs(&self) -> [(&'static str, bool); 7] {
        [
            (GATES[0], self.exact_source_locked),
            (GATES[1], self.independent_real_initial_demand),
            (GATES[2], self.independent_real_followup_demand),
            (GATES[3], self.pair_frozen_before_treatment),
            (GATES[4], self.discriminates_prior_world),
            (GATES[5], self.outcome_surface_frozen),
            (GATES[6], self.observability_firewall_frozen),
        ]
    }
}

#[derive(Debug, Serialize)]
pub struct WorldAdmission {
    pub protocol_version: &'static str,
    pub world_id: String,
    pub admission: &'static str,
    pub gates: std::collections::BTreeMap<&'static str, &'static str>,
    pub law_pressures: LawPressures,
    pub authorized_next: &'static str,
    pub decision_authority: &'static str,
    pub winner: Option<String>,
}

#[derive(Debug, Serialize)]
pub struct LawPressures {
    #[serde(rename = "CIL-C1")]
    pub cil_c1: CilC1WorldPressure,
    #[serde(rename = "CBL-C1")]
    pub cbl_c1: CblC1WorldPressure,
}

#[derive(Debug, Serialize)]
pub struct CilC1WorldPressure {
    pub membership_propagation_opportunity: &'static str,
    pub preexisting_boundary_pressure: &'static str,
}

#[derive(Debug, Serialize)]
pub struct CblC1WorldPressure {
    pub capability_bundle_mismatch: &'static str,
    pub interface_capabilities: Vec<String>,
    pub initial_demand_capabilities: Vec<String>,
    pub followup_demand_capabilities: Vec<String>,
}

pub fn admit_world(world: WorldEnvelope) -> WorldAdmission {
    let pass = world.admission_gates.all_pass();
    let gates = world
        .admission_gates
        .pairs()
        .into_iter()
        .map(|(name, ok)| (name, if ok { "PASS" } else { "FAIL" }))
        .collect();

    WorldAdmission {
        protocol_version: "0.3",
        world_id: world.world_id,
        admission: if pass { "ADMIT" } else { "HOLD" },
        gates,
        law_pressures: LawPressures {
            cil_c1: CilC1WorldPressure {
                membership_propagation_opportunity: if world.moderators.membership_surface_fanout
                    > 1
                {
                    "PRESENT"
                } else {
                    "LIMITED"
                },
                preexisting_boundary_pressure: if world.moderators.existing_runtime_interface {
                    "PRESENT"
                } else {
                    "ABSENT"
                },
            },
            cbl_c1: CblC1WorldPressure {
                capability_bundle_mismatch: if world.moderators.capability_bundle_mismatch {
                    "PRESENT"
                } else {
                    "ABSENT"
                },
                interface_capabilities: world.moderators.existing_interface_capabilities,
                initial_demand_capabilities: world.moderators.initial_demand_capabilities,
                followup_demand_capabilities: world.moderators.followup_demand_capabilities,
            },
        },
        authorized_next: if pass {
            "PRETREATMENT_RIVAL_CONSTITUTION"
        } else {
            "NONE"
        },
        decision_authority: "NO_DESIGN_RECOMMENDATION",
        winner: None,
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn sample() -> WorldEnvelope {
        WorldEnvelope {
            protocol_version: "0.3".into(),
            world_id: "WORLD".into(),
            moderators: WorldModerators {
                membership_surface_fanout: 9,
                existing_runtime_interface: true,
                existing_interface_capabilities: vec!["search".into(), "fetch".into()],
                initial_demand_capabilities: vec!["search".into()],
                followup_demand_capabilities: vec!["search".into()],
                capability_bundle_mismatch: true,
            },
            admission_gates: WorldAdmissionGates {
                exact_source_locked: true,
                independent_real_initial_demand: true,
                independent_real_followup_demand: true,
                pair_frozen_before_treatment: true,
                discriminates_prior_world: true,
                outcome_surface_frozen: true,
                observability_firewall_frozen: true,
            },
        }
    }

    #[test]
    fn admits_only_when_all_gates_pass() {
        let out = admit_world(sample());
        assert_eq!(out.admission, "ADMIT");
        assert_eq!(out.authorized_next, "PRETREATMENT_RIVAL_CONSTITUTION");
        assert_eq!(out.decision_authority, "NO_DESIGN_RECOMMENDATION");
        assert_eq!(
            out.law_pressures.cbl_c1.capability_bundle_mismatch,
            "PRESENT"
        );
    }

    #[test]
    fn holds_when_one_gate_fails() {
        let mut world = sample();
        world.admission_gates.outcome_surface_frozen = false;
        let out = admit_world(world);
        assert_eq!(out.admission, "HOLD");
        assert_eq!(out.authorized_next, "NONE");
    }
}
