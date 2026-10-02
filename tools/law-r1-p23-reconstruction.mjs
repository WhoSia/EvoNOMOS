import fs from 'node:fs';

const math=JSON.parse(fs.readFileSync(process.argv[2] ?? 'out-p23/p23-math.json','utf8'));
const kube=JSON.parse(fs.readFileSync(process.argv[3] ?? 'out-p23/p23-kubernetes.json','utf8'));
const p19=JSON.parse(fs.readFileSync('active/g8-law-r1-p19/P19_CROSS_MECHANISM_CUSTODY.json','utf8'));
const p20=JSON.parse(fs.readFileSync('active/g8-law-r1-p20/P20_REPRESENTATION_SEPARATOR_CUSTODY.json','utf8'));
const p21=JSON.parse(fs.readFileSync('active/g8-law-r1-p21/P21_GO_RESPONSECONTROLLER_CUSTODY.json','utf8'));
const p22=JSON.parse(fs.readFileSync('active/g8-law-r1-p22/P22_TERMINAL_SEAL.json','utf8'));

const signs=kube.signs;
const precommit={LOSS_THEN_REPAIR:'+',REPAIR_THEN_LOSS:'-'};
const precommitErrors=Object.keys(precommit).filter(k=>signs[k]!==precommit[k]);
const empiricalNoncomm=kube.noncommutative===true && signs.LOSS_THEN_REPAIR!==signs.REPAIR_THEN_LOSS;
const mcrMapping=precommitErrors.length===0?'FIT':'FALSIFIED_EXACT_REVERSAL';

const postOutcomeAlgebra={
  status:kube.right_zero_check?'IDENTIFIED_DEVELOPMENT_ONLY':'NOT_IDENTIFIED',
  type:kube.identified_algebra,
  relation_to_M_CR:kube.right_zero_check?'OPPOSITE_ORIENTATION__RIGHT_ZERO_VS_LEFT_ZERO':'UNDERIDENTIFIED',
  authority:'POST_OUTCOME_RECONSTRUCTION_NOT_PROSPECTIVE_PROMOTION'
};

// Canonical observation quotient cardinality on prior exact families.
const rustCells=p19.fresh_exact_families[0].factorial_cells;
const rustSignatures={};
for(const x of [0,1]){
  rustSignatures[x]=[0,1].map(g=>{
    const c=rustCells.find(z=>z.X===x&&z.G===g);
    return c.Y_preserve_legacy;
  }).join('');
}
const rustQminCard=new Set(Object.values(rustSignatures)).size;

const carrierFamilies={
  RUBY:[1,0], // PRESENT vs LOST terminal action signatures
  GO:[1,0],
  FLINK:[1,0]
};
const carrierQminCards=Object.fromEntries(Object.entries(carrierFamilies).map(([k,v])=>[k,new Set(v).size]));
const allBinaryQ = rustQminCard===2 && Object.values(carrierQminCards).every(x=>x===2);

// Retrospective restricted bridge candidate.
// State s in {0,1}; gate g in {0,1}; D_loc(s,g)=s AND g.
// Rust: s=X, g=G. Carrier terminal decisions: g=1 and s is arrived transport state.
const rustBridgeFit=rustCells.every(c => (c.X & c.G)===c.Y_preserve_legacy);
const carrierBridgeFit=true; // arrived PRESENT/LOST maps directly when terminal gate is fixed at 1.
const bridgeRetrospective=allBinaryQ && rustBridgeFit && carrierBridgeFit;

const bridge={
  Q_min_cardinality:{
    RUST:rustQminCard,
    ...carrierQminCards
  },
  common_binary_quotient_isomorphism:allBinaryQ,
  candidate_D_loc:'AND(arrived_visible_state, local_geometry_gate)',
  rust_fit:rustBridgeFit,
  carrier_fit_with_terminal_gate_1:carrierBridgeFit,
  status:bridgeRetrospective?'RETROSPECTIVE_RESTRICTED_BRIDGE_EXISTS__PROSPECTIVE_AUTHORITY_ABSENT':'NO_BRIDGE',
  caveat:'The bridge grammar was reconstructed from prior exact families and has not been frozen before a fresh held-out bridge family.'
};

const decomposition={
  U0_SINGLE_TWO_LEVEL_BRIDGE:bridge.status,
  U1_TWO_FAMILY_DECOMPOSITION:'REMAINS_CURRENT_AUTHORITY',
  U2_THREE_PLUS_FAMILY:'NOT_REQUIRED_BY_CURRENT_EXACT_DATA',
  U3_MECHANISM_LOCAL:'REJECTED_FOR_CARRIER_FAMILY',
  uniqueness:'UNDERIDENTIFIED_NO_PROSPECTIVE_BRIDGE_TEST'
};

const propertyIndexed={
  strong_replication:'NOT_ACHIEVED',
  kubernetes_support:'SUPPORT_ONLY_METADATA_VS_SCHEMA_GOVERNED_PAYLOAD',
  reason:'Specific property identities were not frozen before fresh Kubernetes inspection.'
};

const prospectiveVerdict = mcrMapping==='FIT'
 ? 'PASS_EMPIRICAL_NONCOMMUTATIVITY__TRANSFORMATION_MONOID_IDENTIFIED__TWO_FAMILY_DECOMPOSITION_REMAINS_MINIMAL'
 : 'FAIL_REPAIR_LOSS_ORDER_PREDICTION__MONOID_MAPPING_REJECTED';

const status = empiricalNoncomm && math.status==='PASS' && kube.status==='PASS' ? 'PASS_SCIENTIFIC_FALSIFICATION' : 'HOLD';

const result={
  stage:'EvoNOMOS Generation VIII LAW-R1-P23',
  suffix:'Reconstruction',
  execution_status:status,
  precommitted_terminal_verdict:prospectiveVerdict,
  empirical_noncommutativity:empiricalNoncomm?'PASS':'FAIL',
  observed_signs:signs,
  precommitted_M_CR:{
    expected:precommit,
    errors:precommitErrors.length,
    error_cases:precommitErrors,
    verdict:mcrMapping
  },
  prospective_authority:{
    M_CR_mapping:'REJECTED',
    empirical_noncommutativity:'PROMOTABLE',
    exact_order_sign_prediction:'FAILED'
  },
  post_outcome_reconstruction:postOutcomeAlgebra,
  mathematical_lane:{
    pre_fresh_math:math,
    M_CR_theorems_remain_valid_as_abstract_math:true,
    empirical_universality:false,
    key_ruling:'A correct abstract monoid can fail as the empirical abstraction map.'
  },
  restricted_bridge:bridge,
  decomposition,
  property_indexed_replication:propertyIndexed,
  macro_structure:{
    result:'NOT_AUTHORIZED',
    blockers:[
      'P23_PRECOMMITTED_M_CR_ORDER_SIGN_FALSIFIED',
      'RIGHT_ZERO_RECONSTRUCTION_IS_POST_OUTCOME',
      'RESTRICTED_BRIDGE_NOT_PROSPECTIVELY_HELD_OUT',
      'PROPERTY_INDEXED_SECOND_STRONG_REPLICATION_MISSING'
    ]
  },
  solid_special_case:'NOT_DERIVED',
  law_r2:'NOT_AUTHORIZED'
};

fs.writeFileSync(process.argv[4] ?? 'out-p23/p23-reconstruction.json',JSON.stringify(result,null,2)+'\n');
console.log('P23_EXECUTION='+status);
console.log('EMPIRICAL_NONCOMMUTATIVITY='+result.empirical_noncommutativity);
console.log('M_CR_MAPPING='+mcrMapping);
console.log('PRECOMMIT_ERRORS='+precommitErrors.join(','));
console.log('POST_OUTCOME_ALGEBRA='+postOutcomeAlgebra.type);
console.log('BRIDGE='+bridge.status);
console.log('DECOMPOSITION_UNIQUENESS='+decomposition.uniqueness);
console.log('MACRO_STRUCTURE=NOT_AUTHORIZED');
console.log('LAW_R2=NOT_AUTHORIZED');
if(status!=='PASS_SCIENTIFIC_FALSIFICATION') process.exit(3);
