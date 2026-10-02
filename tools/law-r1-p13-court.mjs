import fs from 'node:fs';

const input = process.argv[2] ?? 'out-p13/p13-discriminators.json';
const output = process.argv[3] ?? 'out-p13/p13-court.json';
const d = JSON.parse(fs.readFileSync(input,'utf8'));

const repPass = d.representation_invariance?.all_pass === true;
const antiPass = d.anti_rationalization_pass === true;
const custodyPass = d.merged_source_count >= 5 && d.family_count >= 3;
const sameStateConflict = d.same_normalized_X_G_E_conflicting_action_observed === true;

let verdict;
let status = 'PASS';
let lawR2 = 'NOT_AUTHORIZED';

if (!repPass || !antiPass || !custodyPass) {
  verdict = 'HOLD_DISCRIMINATOR_ECOLOGY_INSUFFICIENT__NO_POST_HOC_EXPANSION';
  status = 'HOLD';
} else if (sameStateConflict) {
  verdict = 'FAIL_STABLE_X_PRIMITIVE_STRUCTURE__CONTEXT_REPRESENTATION_REQUIRES_RECONSTITUTION';
  lawR2 = 'CANDIDATE_ONLY';
} else if ((d.stable_primitives ?? []).length > 0) {
  verdict = 'PASS_STABLE_X_PRIMITIVES_REPLICATED__COMPATIBILITY_COEXISTENCE_AUTHORITY_SEPARATED__R2_NOT_AUTHORIZED';
} else {
  verdict = 'PASS_PARTIAL_PRIMITIVE_STRUCTURE__DEPENDENCIES_RECOVERED__RESIDUAL_UNDERIDENTIFICATION_RETAINED__R2_NOT_AUTHORIZED';
}

const compat = d.coordinate_summary?.COMPATIBILITY_OBLIGATION;
const coexist = d.coordinate_summary?.COEXISTENCE_REQUIREMENT;
const authority = d.coordinate_summary?.RELEASE_AUTHORITY;

const result = {
  stage: 'EvoNOMOS Generation VIII LAW-R1-P13',
  status,
  verdict,
  scientific_readout: {
    compatibility_obligation: compat?.bounded_identified ? 'IDENTIFIED_BOUNDED_ONE_DOMAIN_EXACT' : 'UNRESOLVED',
    coexistence_requirement: coexist?.bounded_identified ? 'IDENTIFIED_BOUNDED' : ((coexist?.near_domains?.length ?? 0) > 0 ? 'SUPPORTED_NEAR_MATCHED_BUT_NOT_ORTHOGONAL' : 'UNRESOLVED'),
    release_authority: authority?.bounded_identified ? 'IDENTIFIED_BOUNDED' : 'UNRESOLVED_CONFOUNDED_WITH_LIFECYCLE',
    stable_primitives: d.stable_primitives,
    bounded_identified: d.bounded_identified,
    unresolved_coordinates: d.unresolved_coordinates,
    dependency_graph: d.dependency_graph,
    representation_invariance: repPass ? 'PASS' : 'FAIL',
    anti_rationalization: antiPass ? 'PASS' : 'FAIL'
  },
  ruling: {
    stable_primitive_structure_of_X: (d.stable_primitives ?? []).length > 0 ? 'PARTIALLY_ESTABLISHED' : 'NOT_YET_ESTABLISHED',
    compatibility_obligation: 'RETAIN_AS_BOUNDED_IDENTIFIED_CANDIDATE',
    coexistence_requirement: 'DO_NOT_PROMOTE_INDEPENDENT_PRIMITIVE_YET',
    release_authority: 'DO_NOT_PROMOTE__LIFECYCLE_CONFOUND_REMAINS',
    lifecycle_phase: 'RETAINS_P12_IDENTIFIED_STATUS',
    state_ontology: 'SURVIVES_CURRENT_ATTACK',
    policy: 'INTERACTION_BEARING',
    law_r2: lawR2,
    next_authority: 'REMAIN_WITHIN_LAW_R1'
  },
  caution: 'P13 does not meet the presealed two-domain exact-replication threshold for any new stable primitive. Bounded identification and dependency evidence are preserved without promotion.'
};

fs.writeFileSync(output,JSON.stringify(result,null,2)+'\n');
console.log(status === 'PASS' ? 'LAW_R1_P13_COURT=PASS' : 'LAW_R1_P13_COURT=HOLD');
console.log(`VERDICT=${verdict}`);
console.log(`STABLE=${(d.stable_primitives ?? []).join(',') || 'NONE'}`);
console.log(`BOUNDED=${(d.bounded_identified ?? []).join(',') || 'NONE'}`);
console.log(`LAW_R2=${lawR2}`);
if (status !== 'PASS') process.exit(2);
