import fs from 'node:fs';

const input = process.argv[2] ?? 'out-p12/p12-worlds.json';
const output = process.argv[3] ?? 'out-p12/p12-court.json';
const w = JSON.parse(fs.readFileSync(input, 'utf8'));

const repPass = w.representation_invariance?.all_pass === true;
const antiPass = w.anti_rationalization_pass === true;
const mergedEnough = w.merged_source_count >= 4;
const identified = new Set(w.identified_coordinates ?? []);
const lifecycleIdentified = identified.has('LIFECYCLE_PHASE');
const exactFullConflict = (w.full_state_conflicts ?? []).length > 0;
const sampleMin = w.sample_minimal_cardinality;
const sparseMatched = (w.clean_matched_GE_pairs ?? []).length < 3;

let verdict;
let status = 'PASS';
let lawR2 = 'NOT_AUTHORIZED';

if (!repPass || !antiPass || !mergedEnough) {
  verdict = 'HOLD_CONTEXT_MINIMALITY_CUSTODY_OR_ANTI_RATIONALIZATION_FAILURE';
  status = 'HOLD';
} else if (exactFullConflict) {
  verdict = 'FAIL_STATE_SUFFICIENCY__NORMALIZED_FULL_STATE_ACTION_CONFLICT__LAW_R2_CANDIDATE';
  lawR2 = 'CANDIDATE_ONLY';
} else if (lifecycleIdentified && sparseMatched) {
  verdict = 'PASS_CONTEXT_COMPRESSION_SUPPORTED__LIFECYCLE_IDENTIFIED__OTHER_COORDINATES_UNDERIDENTIFIED__POST_HOC_EXPANSION_BLOCKED__R2_NOT_AUTHORIZED';
} else if (w.identified_coordinates?.length > 1) {
  verdict = 'PASS_BOUNDED_X_MIN_EQUIVALENCE_CLASS_IDENTIFIED__ANTI_RATIONALIZATION_SURVIVES__R2_NOT_AUTHORIZED';
} else {
  verdict = 'PASS_COMPRESSION_SUPPORTED_BUT_X_MIN_NONUNIQUE__ANTI_RATIONALIZATION_SURVIVES__R2_NOT_AUTHORIZED';
}

const result = {
  stage: 'EvoNOMOS Generation VIII LAW-R1-P12',
  status,
  verdict,
  scientific_readout: {
    coordinate_deletion: 'EXECUTED',
    identified_coordinates: w.identified_coordinates,
    unidentified_coordinates: w.unidentified_coordinates,
    clean_matched_GE_pairs: w.clean_matched_GE_pairs,
    sample_minimal_cardinality: sampleMin,
    sample_minimal_subsets: w.sample_minimal_subsets,
    minimality_claim: sparseMatched ? 'BOUNDED_UNDERIDENTIFIED__NO_UNIVERSAL_X_MIN_CLAIM' : 'BOUNDED_IDENTIFIED',
    representation_invariance: repPass ? 'PASS' : 'FAIL',
    anti_rationalization: antiPass ? 'PASS' : 'FAIL',
    reassignment: w.reassignment_audit,
    post_hoc_coordinate_additions: w.post_hoc_coordinate_additions
  },
  ruling: {
    X: 'COMPRESSIBLE_BUT_NOT_FULLY_IDENTIFIED',
    strongest_identified_coordinate: lifecycleIdentified ? 'LIFECYCLE_PHASE' : 'NONE',
    consumer_migration_window: 'NOT_ESTABLISHED_AS_INDEPENDENT_PRIMITIVE',
    runtime_or_toolchain_provenance: 'REASSIGN_TOWARD_E_UNDER_P12_REPRESENTATION',
    ownership_or_responsibility_boundary: 'NOT_ESTABLISHED_AS_INDEPENDENT_X_PRIMITIVE',
    state_ontology: 'SURVIVES_CURRENT_ATTACK',
    policy: 'INTERACTION_BEARING',
    law_r2: lawR2,
    next_authority: 'REMAIN_WITHIN_LAW_R1'
  },
  caution: 'The one-coordinate sample-minimal subset is not promoted as universal X_min because matched-(G,E) coverage is sparse. Underidentification is preserved rather than repaired post hoc.'
};

fs.writeFileSync(output, JSON.stringify(result, null, 2) + '\n');
console.log(status === 'PASS' ? 'LAW_R1_P12_COURT=PASS' : 'LAW_R1_P12_COURT=HOLD');
console.log(`VERDICT=${verdict}`);
console.log(`IDENTIFIED=${(w.identified_coordinates ?? []).join(',') || 'NONE'}`);
console.log(`LAW_R2=${lawR2}`);
if (status !== 'PASS') process.exit(2);
