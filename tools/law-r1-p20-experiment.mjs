import fs from 'node:fs';

const tsv = fs.readFileSync(process.argv[2] ?? 'active/g8-law-r1-p20/P20_RUBY_SEPARATOR.tsv','utf8')
  .trim().split(/\r?\n/);
const hdr = tsv[0].split('\t');
const rows = tsv.slice(1).map(line => {
  const p=line.split('\t');
  return Object.fromEntries(hdr.map((h,i)=>[h, ['X','G_binary','preservation'].includes(h)?Number(p[i]):p[i]]));
});
const ruby = JSON.parse(fs.readFileSync(process.argv[3] ?? 'out-p20/p20-ruby.json','utf8'));
const custody = JSON.parse(fs.readFileSync('active/g8-law-r1-p20/P20_REPRESENTATION_SEPARATOR_CUSTODY.json','utf8'));

for (const row of rows) {
  const observed = ruby.cases?.[row.case]?.preservation;
  if (observed !== row.preservation) {
    console.error('RUBY_TSV_MISMATCH', row.case, observed, row.preservation);
    process.exit(2);
  }
}

const genericPredict = r => (r.X===1 && r.G_binary===1) ? 1 : 0;
const maximPredict = r => r.X===1 ? 1 : 0;
const genericErrors = rows.filter(r=>genericPredict(r)!==r.preservation);
const maximErrors = rows.filter(r=>maximPredict(r)!==r.preservation);

const triggerPositive = rows.filter(r=>r.X===1 && r.G_binary===1);
const distinctWithinCoarseTrigger = new Set(triggerPositive.map(r=>r.preservation)).size > 1;
const presealedStates = new Set(triggerPositive.map(r=>r.G_state));
const typedBoundarySurvives = distinctWithinCoarseTrigger &&
  presealedStates.has('IMPLICIT_DIRECT') &&
  presealedStates.has('WRAPPER_MEDIATED_GAP');

const explicit = rows.find(r=>r.case==='EXPLICIT_KWARGS');
const direct = rows.find(r=>r.case==='MARKED_IMPLICIT_DIRECT');
const wrapper = rows.find(r=>r.case==='MARKED_WRAPPER_GAP');
const control = rows.find(r=>r.case==='UNMARKED_IMPLICIT_CONTROL');

const leaveOneOut = {
  held_out: 'RUBY_KEYWORD_FORWARDING_COMPATIBILITY',
  generic_binary_conjunction: genericErrors.length>0 ? 'FAIL' : 'PASS',
  generic_error_cases: genericErrors.map(r=>r.case),
  typed_geometry_partition: typedBoundarySurvives ? 'SURVIVES_BOUNDARY_CLASSIFICATION' : 'FAIL',
  typed_exact_sign_prediction: 'UNDERIDENTIFIED_NOT_PRECOMMITTED',
  named_maxim: maximErrors.length>0 ? 'FAIL' : 'PASS',
  named_maxim_error_cases: maximErrors.map(r=>r.case),
  untyped_lookup: 'NO_TRANSPORT_PREDICTION'
};

const status = ruby.status==='PASS' &&
  genericErrors.length>0 &&
  typedBoundarySurvives &&
  maximErrors.some(r=>r.case==='MARKED_WRAPPER_GAP') &&
  custody.post_hoc_X_additions.length===0 &&
  custody.post_hoc_G_additions.length===0 &&
  custody.trigger_rebinning===false
  ? 'PASS' : 'HOLD';

const verdict = status==='PASS'
 ? 'PASS_REPRESENTATION_SEPARATION__SECOND_EXACT_NONMIGRATION_FAMILY__TYPED_BOUNDARY_TRANSPORTS__GENERIC_CONJUNCTION_FAILS__MACRO_LAW_NOT_YET_AUTHORIZED'
 : 'HOLD_SECOND_EXACT_FAMILY_NOT_FOUND__REPRESENTATION_SEPARATOR_UNDERPOWERED';

const result = {
  stage:'EvoNOMOS Generation VIII LAW-R1-P20',
  suffix:'Experiment',
  status,
  verdict,
  ruby_reproduction:ruby.status,
  second_exact_nonmigration_family:'RUBY_KEYWORD_FORWARDING_COMPATIBILITY',
  representation_separator:{
    generic_binary_conjunction:{
      errors:genericErrors.length,
      error_cases:genericErrors.map(r=>r.case),
      status:genericErrors.length>0?'FALSIFIED':'SURVIVES'
    },
    typed_geometry:{
      status:typedBoundarySurvives?'SURVIVES_STRUCTURALLY':'FAIL',
      exact_sign_prediction:'NOT_PRECOMMITTED',
      unique_representation:'NO'
    },
    named_compatibility_maxim:{
      errors:maximErrors.length,
      error_cases:maximErrors.map(r=>r.case),
      status:maximErrors.length>0?'FAILS_FROZEN_MAPPING':'SURVIVES',
      posthoc_unless:'FORBIDDEN_RESCUE'
    }
  },
  key_cells:{
    control:control.preservation,
    marked_direct:direct.preservation,
    marked_wrapper_gap:wrapper.preservation,
    explicit_kwargs:explicit.preservation
  },
  leave_one_mechanism_out:leaveOneOut,
  policy_surface_equivalence:{
    binary_conjunction_member:'ELIMINATED_BY_RUBY_TRANSPORT',
    typed_semantic_partition:'SURVIVES',
    richer_low_complexity_rivals:'OPEN',
    class_identity:'NARROWED_NOT_UNIQUE'
  },
  macro_law:{
    exact_nonmigration_family_count:2,
    strong_macro_law:'NOT_AUTHORIZED',
    reason:'Binary conjunction is eliminated, but typed sign prediction was not prospectively specified and richer low-complexity rivals remain open.'
  },
  solid_special_case:'NOT_DERIVED',
  law_r2:'NOT_AUTHORIZED',
  anti_rationalization:{
    new_X:0,
    new_G:0,
    trigger_rebinning:false
  }
};

fs.mkdirSync('out-p20',{recursive:true});
fs.writeFileSync(process.argv[4] ?? 'out-p20/p20-experiment.json',JSON.stringify(result,null,2)+'\n');
console.log('LAW_R1_P20_EXPERIMENT='+status);
console.log('VERDICT='+verdict);
console.log('GENERIC_CONJUNCTION_ERRORS='+genericErrors.length);
console.log('GENERIC_ERROR_CASES='+genericErrors.map(r=>r.case).join(','));
console.log('TYPED_BOUNDARY='+result.representation_separator.typed_geometry.status);
console.log('TYPED_SIGN_PREDICTION=NOT_PRECOMMITTED');
console.log('MAXIM='+result.representation_separator.named_compatibility_maxim.status);
console.log('EXACT_NONMIGRATION_FAMILIES=2');
console.log('MACRO_LAW=NOT_AUTHORIZED');
console.log('LAW_R2=NOT_AUTHORIZED');
if(status!=='PASS') process.exit(3);
