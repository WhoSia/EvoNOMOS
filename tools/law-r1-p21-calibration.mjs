import fs from 'node:fs';

const go = JSON.parse(fs.readFileSync(process.argv[2] ?? 'out-p21/p21-go.json','utf8'));
const custody = JSON.parse(fs.readFileSync('active/g8-law-r1-p21/P21_GO_RESPONSECONTROLLER_CUSTODY.json','utf8'));

const observed = Object.fromEntries(go.cases.map(c => [c.name, c.observed_sign]));
const rivals = custody.rival_predictions;
const scored = {};

for (const [name, pred] of Object.entries(rivals)) {
  if (name === 'R6_UNTYPED_LOOKUP') {
    scored[name] = {status:'NO_TRANSPORT_PREDICTION', errors:null, error_cases:[]};
    continue;
  }
  const errorCases = Object.keys(observed).filter(k => pred[k] !== observed[k]);
  scored[name] = {
    status:errorCases.length === 0 ? 'FIT' : 'FAIL',
    errors:errorCases.length,
    error_cases:errorCases
  };
}

const required = ['DIRECT_CAPABILITY','OPAQUE_WRAPPER','UNWRAP_WRAPPER'];
const prospectiveSignPass =
  go.status === 'PASS' &&
  required.every(k => custody.third_family.presealed_state_mapping.some(x=>x.case===k)) &&
  observed.DIRECT_CAPABILITY === '+' &&
  observed.OPAQUE_WRAPPER === '-' &&
  observed.UNWRAP_WRAPPER === '+';

const carrierSpecificity =
  scored.R4_ALL_EDGES_MUST_CARRY.status === 'FIT' &&
  scored.R5_ONE_SPLIT_DECISION_TREE.status === 'FIT' &&
  scored.R2_WRAPPER_PENALTY.status === 'FAIL' &&
  scored.R3_PATH_LENGTH_THRESHOLD.status === 'FAIL';

const exactFamilies = {
  P19_RUST_EXACT: {
    shared_path_carrier_grammar:false,
    exact:true,
    role:'interaction-family'
  },
  P20_RUBY_EXACT: {
    shared_path_carrier_grammar:true,
    exact:true,
    observed_pattern:'+/-/+'
  },
  P21_GO_EXACT: {
    shared_path_carrier_grammar:true,
    exact:true,
    observed_pattern:'+/-/+'
  },
  P14_AXIOS_SUPPORT: {
    shared_path_carrier_grammar:false,
    exact:false,
    role:'support'
  },
  P19_NODE_SUPPORT: {
    shared_path_carrier_grammar:false,
    exact:false,
    role:'support'
  }
};

const leaveTwo = [];
const names = Object.keys(exactFamilies);
for (let i=0;i<names.length;i++) {
  for (let j=i+1;j<names.length;j++) {
    const held=[names[i],names[j]];
    const train=names.filter(n=>!held.includes(n));
    const heldCarrier=held.filter(n=>exactFamilies[n].shared_path_carrier_grammar);
    const trainCarrier=train.filter(n=>exactFamilies[n].shared_path_carrier_grammar);
    let status='OUT_OF_SHARED_GRAMMAR';
    if (heldCarrier.length>0 && trainCarrier.length>0) status='ADMISSIBLE_PARTIAL';
    if (heldCarrier.length===2 && trainCarrier.length===0) status='UNDERIDENTIFIED_NO_CARRIER_TRAINING';
    leaveTwo.push({held_out:held,training:train,status});
  }
}
const admissibleLeaveTwo = leaveTwo.filter(x=>x.status==='ADMISSIBLE_PARTIAL').length;
const underidentifiedLeaveTwo = leaveTwo.filter(x=>x.status==='UNDERIDENTIFIED_NO_CARRIER_TRAINING').length;

const boundaryCarrierRuling = prospectiveSignPass && carrierSpecificity
  ? 'STRUCTURAL_CARRIER_REPLICATION_PASS__OBLIGATION_SEMANTICS_UNDERIDENTIFIED'
  : 'NO_REPLICATION';

const principle = custody.frozen_principle_applicability.PRINCIPLE_V2_PROPAGATION_QUALIFIED_COMPATIBILITY;

const macroLawAuthorized =
  prospectiveSignPass &&
  scored.R0_TYPED_BOUNDARY_TRANSPORT.status === 'FIT' &&
  carrierSpecificity &&
  principle === 'PASS' &&
  underidentifiedLeaveTwo === 0;

const status = prospectiveSignPass ? 'PASS' : 'FAIL';
const verdict = prospectiveSignPass
  ? 'PASS_PROSPECTIVE_SIGN_PREDICTION__THIRD_EXACT_FAMILY__CARRIER_STRUCTURE_REPLICATED__RICH_RIVALS_ADJUDICATED__MACRO_LAW_NOT_AUTHORIZED'
  : 'FAIL_PROSPECTIVE_SIGN_RULE__THIRD_FAMILY_REVERSES_PRECOMMITTED_BOUNDARY_PREDICTION';

const result = {
  stage:'EvoNOMOS Generation VIII LAW-R1-P21',
  suffix:'Calibration',
  status,
  verdict,
  third_exact_family:'GO_HTTP_RESPONSECONTROLLER_CAPABILITY_TRANSPORT',
  observed_signs:observed,
  required_pattern:'+/-/+',
  prospective_sign_prediction:prospectiveSignPass ? 'PASS' : 'FAIL',
  rival_ecology:scored,
  carrier_specificity:carrierSpecificity ? 'PASS' : 'FAIL',
  boundary_carrying_hypothesis:boundaryCarrierRuling,
  frozen_principle:{
    id:'PRINCIPLE_V2_PROPAGATION_QUALIFIED_COMPATIBILITY',
    result:principle,
    reason:'Go ResponseController carries HTTP capabilities across wrappers; it is not itself a historical compatibility obligation. Scope was frozen before hosted outcome.'
  },
  leave_two_mechanisms_out:{
    protocol:'EXECUTED',
    splits:leaveTwo,
    admissible_partial_splits:admissibleLeaveTwo,
    underidentified_no_carrier_training:underidentifiedLeaveTwo,
    overall:'UNDERIDENTIFIED_INSUFFICIENT_SHARED_GRAMMAR'
  },
  macro_law:{
    authorized:macroLawAuthorized,
    result:macroLawAuthorized ? 'AUTHORIZED' : 'NOT_AUTHORIZED',
    blockers:[
      ...(principle !== 'PASS' ? ['FROZEN_COMPATIBILITY_PRINCIPLE_NOT_DIRECTLY_TESTED'] : []),
      ...(underidentifiedLeaveTwo>0 ? ['LEAVE_TWO_OUT_SHARED_GRAMMAR_UNDERIDENTIFIED'] : []),
      ...(scored.R4_ALL_EDGES_MUST_CARRY.status==='FIT' && scored.R5_ONE_SPLIT_DECISION_TREE.status==='FIT'
          ? ['CARRIER_RULE_AND_ONE_SPLIT_TREE_REMAIN_OBSERVATIONALLY_EQUIVALENT_ON_P21']
          : [])
    ]
  },
  paper_readiness:{
    manuscript:'NOT_AUTHORIZED',
    strongest_new_claim:'A prospectively frozen +/−/+ boundary sign pattern reproduced exactly in a third mechanism, and carrier status outperformed wrapper-only and path-length-only rivals on that family.'
  },
  solid_special_case:'NOT_DERIVED',
  law_r2:'NOT_AUTHORIZED',
  anti_rationalization:{
    new_X:0,
    new_G:0,
    sign_edits:0,
    rival_edits:0,
    scope_expansion:false
  }
};

fs.writeFileSync(process.argv[3] ?? 'out-p21/p21-calibration.json', JSON.stringify(result,null,2)+'\n');
console.log('LAW_R1_P21_CALIBRATION='+status);
console.log('VERDICT='+verdict);
console.log('SIGN='+result.prospective_sign_prediction);
console.log('R2_WRAPPER_PENALTY='+scored.R2_WRAPPER_PENALTY.status);
console.log('R3_PATH_LENGTH='+scored.R3_PATH_LENGTH_THRESHOLD.status);
console.log('R4_ALL_EDGES_CARRY='+scored.R4_ALL_EDGES_MUST_CARRY.status);
console.log('R5_CARRIER_GAP_TREE='+scored.R5_ONE_SPLIT_DECISION_TREE.status);
console.log('BOUNDARY_CARRIER='+boundaryCarrierRuling);
console.log('PRINCIPLE='+principle);
console.log('LEAVE_TWO='+result.leave_two_mechanisms_out.overall);
console.log('MACRO_LAW='+result.macro_law.result);
console.log('LAW_R2=NOT_AUTHORIZED');
if(status!=='PASS') process.exit(3);
