import fs from 'node:fs';

const input = process.argv[2] ?? 'out-p11/p11-worlds.json';
const output = process.argv[3] ?? 'out-p11/p11-court.json';
const w = JSON.parse(fs.readFileSync(input, 'utf8'));

const repPass = w.representation_invariance?.all_pass === true;
const mergedAuthority = w.merged_authority_count >= 3;
const aliasFatal = w.same_material_state_conflicting_action_observed === true;

const aliasDissolution = (w.alias_candidates ?? []).every(a =>
  a.material_equivalence === 'FAILS' &&
  a.same_material_fingerprint === false &&
  ['X','G','E'].includes(a.dissolves_in)
);

const matchedGeometry = w.matched_geometry?.observed === 'ACTION_DISCRIMINATION';
const matchedContext = w.matched_context?.observed === 'DISTINCT_INTERVENTION_FAMILY';

let verdict;
let lawR2;
if (!repPass || !mergedAuthority) {
  verdict = 'HOLD_P11_CUSTODY_OR_INVARIANCE_FAILURE';
  lawR2 = 'NOT_AUTHORIZED';
} else if (aliasFatal) {
  verdict = 'FAIL_STATE_SUFFICIENCY__FRESH_SAME_STATE_ACTION_DIVERGENCE__LAW_R2_AUTHORIZED';
  lawR2 = 'AUTHORIZED';
} else if (aliasDissolution && matchedGeometry && matchedContext) {
  verdict = 'PASS_BOUNDED_TRANSPORT__ALIAS_CANDIDATES_DISSOLVED_UNDER_RECONSTITUTION__R2_NOT_AUTHORIZED';
  lawR2 = 'NOT_AUTHORIZED';
} else {
  verdict = 'HOLD_STATE_ALIASING_CANDIDATE__MATERIAL_EQUIVALENCE_NOT_ESTABLISHED';
  lawR2 = 'NOT_AUTHORIZED';
}

const result = {
  stage: 'EvoNOMOS Generation VIII LAW-R1-P11',
  verdict,
  scientific_readout: {
    cross_ecosystem_transport: matchedGeometry && matchedContext ? 'SUPPORTED_BOUNDED' : 'UNRESOLVED',
    matched_geometry_context_effect: matchedGeometry ? 'SUPPORTED_BOUNDED' : 'UNRESOLVED',
    matched_context_geometry_discrimination: matchedContext ? 'SUPPORTED_BOUNDED' : 'UNRESOLVED',
    representation_invariance: repPass ? 'PASS' : 'FAIL',
    alias_candidates: aliasDissolution ? 'DISSOLVED_UNDER_EXISTING_X_G_E' : 'UNRESOLVED',
    same_material_X_G_E_conflicting_action: aliasFatal ? 'OBSERVED' : 'NOT_OBSERVED',
    hidden_coordinate_reconstruction: aliasDissolution ? 'EXISTING_X_REFINEMENT_SUFFICIENT_FOR_TESTED_ALIASES' : 'UNRESOLVED'
  },
  ruling: {
    state_ontology: aliasFatal ? 'INSUFFICIENT_CANDIDATE' : 'SURVIVES_CURRENT_ATTACK',
    policy: 'INTERACTION_BEARING',
    law_r2: lawR2,
    next_authority: lawR2 === 'AUTHORIZED' ? 'R2_REOPENING_PERMITTED_AFTER_TERMINAL_SEAL' : 'REMAIN_WITHIN_LAW_R1'
  },
  custody: {
    world_count: w.world_count,
    merged_authority_count: w.merged_authority_count,
    representation_cases: Object.keys(w.representation_invariance?.cases ?? {}).length
  }
};

fs.writeFileSync(output, JSON.stringify(result, null, 2) + '\n');
if (verdict.startsWith('HOLD')) {
  console.log('LAW_R1_P11_COURT=HOLD');
  console.log(`VERDICT=${verdict}`);
  process.exit(2);
}
console.log('LAW_R1_P11_COURT=PASS');
console.log(`VERDICT=${verdict}`);
console.log(`LAW_R2=${lawR2}`);
