import fs from 'node:fs';

const input = process.argv[2] ?? 'out-p15/p15-basis.json';
const output = process.argv[3] ?? 'out-p15/p15-court.json';
const d = JSON.parse(fs.readFileSync(input, 'utf8'));

const repPass = d.representation_invariance?.all_pass === true;
const antiPass = d.anti_rationalization_pass === true;
const coexistPass = d.second_domain_replication?.COEXISTENCE_REQUIREMENT === 'PASS';
const authorityPass = d.second_domain_replication?.RELEASE_AUTHORITY === 'PASS';
const minimalBasis = d.minimal_reproducible_basis === 'PASS';
const sameState = d.same_normalized_X_G_E_conflicting_action_observed === true;

let status = 'PASS';
let lawR2 = 'NOT_AUTHORIZED';
let verdict;

if (!repPass || !antiPass) {
  status = 'HOLD';
  verdict = 'HOLD_SECOND_DOMAIN_REPLICATION_INSUFFICIENT__BASIS_COMPLETION_NOT_AUTHORIZED';
} else if (sameState) {
  verdict = 'FAIL_CONTEXT_BASIS_STABILITY__MERGE_OR_DELETION_ATTACK_DEFEATS_CURRENT_X';
  lawR2 = 'CANDIDATE_ONLY';
} else if (minimalBasis) {
  verdict = 'PASS_REPRODUCIBLE_MINIMAL_CONTEXT_BASIS__COEXISTENCE_AND_AUTHORITY_STABLE__MERGE_SPLIT_ATTACKS_SURVIVE__R2_NOT_AUTHORIZED';
} else if (coexistPass && authorityPass) {
  verdict = 'PASS_PARTIAL_CONTEXT_BASIS__SECOND_DOMAIN_COEXISTENCE_AND_AUTHORITY_REPLICATIONS_EARNED__LIFECYCLE_TRANSPORT_GAP_RETAINED__R2_NOT_AUTHORIZED';
} else if (coexistPass || authorityPass) {
  verdict = 'PASS_PARTIAL_CONTEXT_BASIS__ONE_SECOND_DOMAIN_REPLICATION_EARNED__RESIDUAL_BOUNDEDNESS_RETAINED__R2_NOT_AUTHORIZED';
} else {
  status = 'HOLD';
  verdict = 'HOLD_SECOND_DOMAIN_REPLICATION_INSUFFICIENT__BASIS_COMPLETION_NOT_AUTHORIZED';
}

const result = {
  stage: 'EvoNOMOS Generation VIII LAW-R1-P15',
  status,
  verdict,
  scientific_readout: {
    stable_primitives: d.stable_primitives,
    identified_single_domain: d.identified_single_domain,
    coexistence_second_domain: d.second_domain_replication.COEXISTENCE_REQUIREMENT,
    authority_second_domain: d.second_domain_replication.RELEASE_AUTHORITY,
    minimal_reproducible_basis: d.minimal_reproducible_basis,
    minimal_basis_blocker: d.minimal_basis_blocker,
    deletion_attacks: d.basis_attacks.deletion,
    merge_attacks: d.basis_attacks.pairwise_merge,
    split_attacks: d.basis_attacks.split,
    representation_invariance: repPass ? 'PASS' : 'FAIL',
    anti_rationalization: antiPass ? 'PASS' : 'FAIL'
  },
  custody_readout: d.literature_custody,
  ruling: {
    compatibility_obligation: 'STABLE_PRIMITIVE_RETAINED',
    coexistence_requirement: coexistPass ? 'STABLE_PRIMITIVE_TWO_DOMAIN_EXACT' : 'BOUNDED',
    release_authority: authorityPass ? 'STABLE_PRIMITIVE_TWO_DOMAIN_EXACT' : 'BOUNDED',
    lifecycle_phase: 'IDENTIFIED_SINGLE_DOMAIN__SECOND_DOMAIN_REQUIRED',
    context_basis: minimalBasis ? 'REPRODUCIBLE_MINIMAL_BASIS_ESTABLISHED' : 'PARTIAL_REPRODUCIBLE_BASIS_ONLY',
    state_ontology: 'SURVIVES_CURRENT_ATTACK',
    policy: 'INTERACTION_BEARING',
    law_r2: lawR2,
    next_authority: 'REMAIN_WITHIN_LAW_R1'
  },
  caution: 'P15 may promote coexistence and authority, but it does not promote the full X basis while lifecycle remains single-domain. No manuscript narrative can override that ceiling.'
};

fs.writeFileSync(output, JSON.stringify(result, null, 2) + '\n');
console.log(status === 'PASS' ? 'LAW_R1_P15_COURT=PASS' : 'LAW_R1_P15_COURT=HOLD');
console.log(`VERDICT=${verdict}`);
console.log(`STABLE=${d.stable_primitives.join(',')}`);
console.log(`MINIMAL_BASIS=${d.minimal_reproducible_basis}`);
console.log(`LAW_R2=${lawR2}`);
if (status !== 'PASS') process.exit(2);
