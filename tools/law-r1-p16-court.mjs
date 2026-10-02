import fs from 'node:fs';

const input = process.argv[2] ?? 'out-p16/p16-basis.json';
const output = process.argv[3] ?? 'out-p16/p16-court.json';
const d = JSON.parse(fs.readFileSync(input, 'utf8'));

const lifecyclePass = d.lifecycle_second_domain === 'PASS';
const deletionPass = d.deletion_completeness === 'PASS';
const pairwisePass = d.pairwise_quotient_exhaustion?.status === 'PASS';
const triplePass = d.higher_order_quotient_exhaustion?.triple_status === 'PASS';
const fullPass = d.higher_order_quotient_exhaustion?.full_collapse_status === 'PASS';
const repPass = d.representation_invariance === 'PASS';
const antiPass = d.anti_rationalization === 'PASS';
const basisPass = d.operational_minimal_basis === 'PASS';
const custodyPass = d.literature_custody?.status === 'PASS';
const sameState = d.same_normalized_X_G_E_conflicting_action_observed === true;

let status = 'PASS';
let lawR2 = 'NOT_AUTHORIZED';
let verdict;

if (!repPass || !antiPass || !custodyPass) {
  status = 'HOLD';
  verdict = 'HOLD_LIFECYCLE_SECOND_DOMAIN_REPLICATION_INSUFFICIENT__FULL_BASIS_CLOSURE_NOT_AUTHORIZED';
} else if (sameState) {
  verdict = 'FAIL_CURRENT_CONTEXT_BASIS__QUOTIENT_OR_DELETION_ATTACK_DEFEATS_PRIMITIVE_STRUCTURE';
  lawR2 = 'CANDIDATE_ONLY';
} else if (!lifecyclePass) {
  status = 'HOLD';
  verdict = 'HOLD_LIFECYCLE_SECOND_DOMAIN_REPLICATION_INSUFFICIENT__FULL_BASIS_CLOSURE_NOT_AUTHORIZED';
} else if (basisPass && deletionPass && pairwisePass && triplePass && fullPass) {
  verdict = 'PASS_REPRODUCIBLE_MINIMAL_CONTEXT_BASIS__FOUR_PRIMITIVES_TWO_DOMAIN_REPLICATED__DELETION_AND_QUOTIENT_EXHAUSTION_SURVIVE__R2_NOT_AUTHORIZED';
} else {
  verdict = 'PASS_LIFECYCLE_SECOND_DOMAIN_REPLICATION__FULL_MINIMALITY_NOT_EARNED__R2_NOT_AUTHORIZED';
}

const result = {
  stage: 'EvoNOMOS Generation VIII LAW-R1-P16',
  status,
  verdict,
  scientific_readout: {
    lifecycle_second_domain: d.lifecycle_second_domain,
    two_domain_transport: d.transport,
    orthogonal_single_coordinate_interventions: d.orthogonal_single_coordinate_interventions,
    deletion_completeness: d.deletion_completeness,
    pairwise_quotient_exhaustion: d.pairwise_quotient_exhaustion,
    higher_order_quotient_exhaustion: d.higher_order_quotient_exhaustion,
    prospective_split_attack: d.prospective_split_attack,
    representation_invariance: d.representation_invariance,
    anti_rationalization: d.anti_rationalization,
    operational_minimal_basis: d.operational_minimal_basis
  },
  scope_ruling: {
    authorized_claim: 'REPRODUCIBLE_OPERATIONAL_MINIMAL_PRIMITIVE_BASIS_UNDER_FROZEN_COORDINATE_GRAMMAR',
    universal_coordinate_cardinality: 'NOT_CLAIMED',
    unique_latent_factorization: 'NOT_CLAIMED',
    arbitrary_bijective_tuple_packing: 'REPRESENTATION_CHANGE_NOT_PRIMITIVE_REDUCTION'
  },
  literature_data_custody: d.literature_custody,
  ruling: {
    compatibility_obligation: 'STABLE_PRIMITIVE_TWO_DOMAIN',
    coexistence_requirement: 'STABLE_PRIMITIVE_TWO_DOMAIN',
    release_authority: 'STABLE_PRIMITIVE_TWO_DOMAIN',
    lifecycle_phase: lifecyclePass ? 'STABLE_PRIMITIVE_TWO_DOMAIN' : 'SINGLE_DOMAIN_IDENTIFIED',
    context_basis: basisPass ? 'REPRODUCIBLE_OPERATIONAL_MINIMAL_BASIS_ESTABLISHED' : 'NOT_FULLY_CLOSED',
    state_ontology: 'SURVIVES_CURRENT_ATTACK',
    policy: 'INTERACTION_BEARING',
    paper_story_override: 'FORBIDDEN_AND_NOT_USED',
    law_r2: lawR2,
    next_authority: 'REMAIN_WITHIN_LAW_R1'
  },
  caution: 'P16 closes a grammar-relative operational primitive basis, not a representation-invariant minimum coordinate count. Arbitrary reversible recoding can pack the tuple without reducing its primitive intervention content.'
};

fs.writeFileSync(output, JSON.stringify(result, null, 2) + '\n');
console.log(status === 'PASS' ? 'LAW_R1_P16_COURT=PASS' : 'LAW_R1_P16_COURT=HOLD');
console.log(`VERDICT=${verdict}`);
console.log(`LIFECYCLE_SECOND_DOMAIN=${d.lifecycle_second_domain}`);
console.log(`OPERATIONAL_MINIMAL_BASIS=${d.operational_minimal_basis}`);
console.log('UNIVERSAL_CARDINALITY=NOT_CLAIMED');
console.log(`LAW_R2=${lawR2}`);
if (status !== 'PASS') process.exit(2);
