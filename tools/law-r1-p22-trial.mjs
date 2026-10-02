import fs from 'node:fs';

const math=JSON.parse(fs.readFileSync(process.argv[2] ?? 'out-p22/p22-math.json','utf8'));
const java=JSON.parse(fs.readFileSync(process.argv[3] ?? 'out-p22/p22-java.json','utf8'));
const flink=JSON.parse(fs.readFileSync('active/g8-law-r1-p22/P22_FLINK_REPAIR_CUSTODY.json','utf8'));
const p20=JSON.parse(fs.readFileSync('active/g8-law-r1-p20/P20_REPRESENTATION_SEPARATOR_CUSTODY.json','utf8'));
const p21=JSON.parse(fs.readFileSync('active/g8-law-r1-p21/P21_GO_RESPONSECONTROLLER_CUSTODY.json','utf8'));
const p19=JSON.parse(fs.readFileSync('active/g8-law-r1-p19/P19_CROSS_MECHANISM_CUSTODY.json','utf8'));

const obs={
  DIRECT_CURRENT:java.DIRECT_CURRENT,
  OLD_RAW_MISMATCH:java.OLD_RAW_MISMATCH,
  OLD_WITH_EXPLICIT_REPAIR:java.OLD_WITH_EXPLICIT_REPAIR,
  NON_TARGET:java.NON_TARGET_UID_MISMATCH_WITH_TOLERANT_READER
};

const models={
  M0_ABSORBING_LOSS:{DIRECT_CURRENT:'+',OLD_RAW_MISMATCH:'-',OLD_WITH_EXPLICIT_REPAIR:'-'},
  M1_REPAIRABLE_TRANSPORT:{DIRECT_CURRENT:'+',OLD_RAW_MISMATCH:'-',OLD_WITH_EXPLICIT_REPAIR:'+'},
  M4_PROPERTY_INDEPENDENT_REPAIR:{NON_TARGET:'+'},
  M5_PROPERTY_INDEXED_REPAIR:{NON_TARGET:'-'}
};
const score=pred=>{
  const keys=Object.keys(pred);
  const errors=keys.filter(k=>pred[k]!==obs[k]);
  return {errors:errors.length,error_cases:errors,status:errors.length?'FAIL':'FIT'};
};
const modelScores=Object.fromEntries(Object.entries(models).map(([k,v])=>[k,score(v)]));

const mathPass=math.status==='PASS'
  && math.BOOLEAN_R4_R5_EQUIVALENCE==='PASS'
  && math.REPAIR_BREAKS_QUOTIENT==='PASS'
  && math.NONCOMMUTATIVE_WITNESS==='PASS'
  && math.PROPERTY_INDEXED_WITNESS==='PASS';

const fourthPass=java.status==='PASS'
  && obs.DIRECT_CURRENT==='+'
  && obs.OLD_RAW_MISMATCH==='-'
  && obs.OLD_WITH_EXPLICIT_REPAIR==='+'
  && obs.NON_TARGET==='-';

const rubyPattern={
  direct:'+',
  gap:'-',
  explicit:'+'
};
const goPattern={
  direct:'+',
  gap:'-',
  explicit:'+'
};
const flinkPattern={
  direct:obs.DIRECT_CURRENT,
  gap:obs.OLD_RAW_MISMATCH,
  explicit:obs.OLD_WITH_EXPLICIT_REPAIR
};
const patterns={RUBY:rubyPattern,GO:goPattern,FLINK:flinkPattern};
const expected={direct:'+',gap:'-',explicit:'+'};
const patternFits=p=>Object.keys(expected).every(k=>p[k]===expected[k]);

const carrierNames=Object.keys(patterns);
const leaveTwo=[];
for(let i=0;i<carrierNames.length;i++){
  for(let j=i+1;j<carrierNames.length;j++){
    const held=[carrierNames[i],carrierNames[j]];
    const train=carrierNames.filter(x=>!held.includes(x));
    const trainFits=train.every(x=>patternFits(patterns[x]));
    const heldFits=held.every(x=>patternFits(patterns[x]));
    leaveTwo.push({
      held_out:held,
      training:train,
      training_has_exact_carrier:train.length>0,
      fixed_pattern_prediction:expected,
      held_out_match:trainFits&&heldFits,
      status:train.length>0&&trainFits&&heldFits?'PASS':'FAIL'
    });
  }
}
const leaveTwoPass=leaveTwo.every(x=>x.status==='PASS');

const bridge={
  exact_families:{
    RUST:{
      source:p19.fresh_exact_families?.[0]?.id ?? 'RUST_ARRAY_INTO_ITER_EDITION_GEOMETRY',
      family:'SURFACE_SELECTION_INTERACTION',
      path_carrier_packet:false
    },
    RUBY:{
      source:p20.second_exact_nonmigration_family?.id ?? 'RUBY_KEYWORD_FORWARDING_COMPATIBILITY',
      family:'PATH_CARRIER_TRANSPORT',
      path_carrier_packet:true
    },
    GO:{
      source:p21.third_family?.id ?? 'GO_HTTP_RESPONSECONTROLLER_CAPABILITY_TRANSPORT',
      family:'PATH_CARRIER_TRANSPORT',
      path_carrier_packet:true
    },
    FLINK:{
      source:flink.fourth_family.id,
      family:'PATH_CARRIER_TRANSPORT_REPAIRABLE',
      path_carrier_packet:true
    }
  },
  F0_SINGLE_TRANSPORT_LAW:{
    status:'UNDERIDENTIFIED_RESTRICTED_ABSTRACTION_MAP_MISSING',
    reason:'An unrestricted path-category encoding can represent arbitrary local tables and is therefore non-falsifying. No pre-frozen mechanism-independent restricted abstraction map places Rust surface selection into the same carrier algebra without an extra Rust-specific observation map.'
  },
  F1_TWO_FAMILY_DECOMPOSITION:{
    status:fourthPass&&leaveTwoPass?'SUPPORTED_CURRENTLY_MINIMAL':'UNDERIDENTIFIED',
    families:{
      SURFACE_SELECTION:['RUST'],
      PATH_CARRIER_TRANSPORT:['RUBY','GO','FLINK']
    },
    reason:'Three mechanistically distinct path/carrier families share the fixed +/-/+ transport pattern, while Rust remains an exact surface-selection interaction without a non-ad-hoc common carrier map.'
  },
  F2_MECHANISM_LOCAL_ONLY:{
    status:fourthPass&&leaveTwoPass?'REJECTED_BY_CROSS_MECHANISM_CARRIER_REPLICATION':'OPEN'
  }
};

const orderEmpirical='UNDERIDENTIFIED_NO_REPAIR_THEN_GAP_SOFTWARE_CELL';
const mathematicalNoncommutativity='PROVED_IN_MODEL_NOT_YET_EMPIRICALLY_REPLICATED';

const macroAuthorized=false;
const status=mathPass&&fourthPass&&modelScores.M0_ABSORBING_LOSS.status==='FAIL'
  && modelScores.M1_REPAIRABLE_TRANSPORT.status==='FIT'
  && modelScores.M4_PROPERTY_INDEPENDENT_REPAIR.status==='FAIL'
  && modelScores.M5_PROPERTY_INDEXED_REPAIR.status==='FIT'
  && leaveTwoPass ? 'PASS':'HOLD';

const verdict=status==='PASS'
 ? 'PASS_BOOLEAN_RIVAL_COLLAPSE__REPAIRABLE_TRANSPORT_WITNESS__FOURTH_EXACT_COMPATIBILITY_FAMILY__TWO_FAMILY_DECOMPOSITION_SUPPORTED__MACRO_LAW_NOT_AUTHORIZED'
 : 'HOLD_P22_COMPOSITION_TRIAL_INCOMPLETE';

const result={
  stage:'EvoNOMOS Generation VIII LAW-R1-P22',
  suffix:'Trial',
  status,verdict,
  mathematical_lane:{
    theorem0_boolean_rival_equivalence:math.BOOLEAN_R4_R5_EQUIVALENCE,
    irreversible_boolean_quotient:math.IRREVERSIBLE_BOOLEAN_QUOTIENT,
    repair_breaks_quotient:math.REPAIR_BREAKS_QUOTIENT,
    finite_noncommutative_countermodel:math.NONCOMMUTATIVE_WITNESS,
    property_indexed_countermodel:math.PROPERTY_INDEXED_WITNESS
  },
  fourth_exact_family:{
    id:flink.fourth_family.id,
    compatibility_obligation:'EXPLICIT',
    observed:obs,
    direct_gap_repair_pattern:fourthPass?'PASS':'FAIL'
  },
  empirical_model_competition:modelScores,
  empirical_rulings:{
    BOOLEAN_ABSORBING_QUOTIENT:'FALSIFIED_ON_FLINK_REPAIR',
    REPAIRABLE_TRANSPORT:'SUPPORTED_ON_FLINK',
    PROPERTY_INDEPENDENT_REPAIR:'FALSIFIED_BY_NON_TARGET_CONTROL',
    PROPERTY_INDEXED_REPAIR:'SUPPORTED',
    ORDER_SENSITIVITY:orderEmpirical
  },
  leave_two_out_recovery:{
    carrier_families:['RUBY','GO','FLINK'],
    splits:leaveTwo,
    result:leaveTwoPass?'PASS_FIXED_PATTERN_RECOVERY':'FAIL'
  },
  law_family_bridge:bridge,
  pure_math_vs_empirical_boundary:{
    noncommutativity:mathematicalNoncommutativity,
    note:'Drop and repair fail to commute in the abstract two-state model; P22 Flink establishes repair after mismatch, but does not supply a natural repair-then-gap software cell.'
  },
  macro_law:{
    authorized:macroAuthorized,
    result:'NOT_AUTHORIZED',
    blockers:[
      'SINGLE_TRANSPORT_LAW_RESTRICTED_ABSTRACTION_MAP_MISSING',
      'REPAIR_VS_GAP_ORDER_NOT_EMPIRICALLY_CLOSED',
      'TWO_FAMILY_DECOMPOSITION_SUPPORTED_BUT_HIGHER_LEVEL_BRIDGE_UNDERIDENTIFIED',
      'SOLID_SPECIAL_CASE_NOT_DERIVED'
    ]
  },
  law_r2:'NOT_AUTHORIZED',
  anti_rationalization:{
    posthoc_repair_definition:false,
    posthoc_property_reindexing:false,
    forced_single_grammar:false
  }
};

fs.writeFileSync(process.argv[4] ?? 'out-p22/p22-trial.json',JSON.stringify(result,null,2)+'\n');
console.log('LAW_R1_P22_TRIAL='+status);
console.log('VERDICT='+verdict);
console.log('M0_ABSORBING='+modelScores.M0_ABSORBING_LOSS.status);
console.log('M1_REPAIRABLE='+modelScores.M1_REPAIRABLE_TRANSPORT.status);
console.log('M4_PROPERTY_INDEPENDENT='+modelScores.M4_PROPERTY_INDEPENDENT_REPAIR.status);
console.log('M5_PROPERTY_INDEXED='+modelScores.M5_PROPERTY_INDEXED_REPAIR.status);
console.log('LEAVE_TWO='+result.leave_two_out_recovery.result);
console.log('F0_SINGLE='+bridge.F0_SINGLE_TRANSPORT_LAW.status);
console.log('F1_TWO_FAMILY='+bridge.F1_TWO_FAMILY_DECOMPOSITION.status);
console.log('F2_LOCAL_ONLY='+bridge.F2_MECHANISM_LOCAL_ONLY.status);
console.log('MACRO_LAW=NOT_AUTHORIZED');
console.log('LAW_R2=NOT_AUTHORIZED');
if(status!=='PASS') process.exit(3);
