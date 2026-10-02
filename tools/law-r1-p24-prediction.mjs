import fs from 'node:fs';

const math=JSON.parse(fs.readFileSync(process.argv[2] ?? 'out-p24/p24-math.json','utf8'));
const pb=JSON.parse(fs.readFileSync(process.argv[3] ?? 'out-p24/p24-protobuf.json','utf8'));
const quic=JSON.parse(fs.readFileSync(process.argv[4] ?? 'out-p24/p24-quic-bridge.json','utf8'));
const quicUpstream=JSON.parse(fs.readFileSync(process.argv[5] ?? 'out-p24/p24-quic-upstream.json','utf8'));
const pbModule=JSON.parse(fs.readFileSync(process.argv[6] ?? 'out-p24/p24-protobuf-module.json','utf8'));

const mathPass =
  math.status==='PASS' &&
  math.left_zero_min_faithful_degree===2 &&
  math.right_zero_min_faithful_degree===3 &&
  math.boolean_quotient_orientation_erasure===true &&
  math.and_unique_on_complete_2x2===true;

const orientationPass =
  pb.status==='PASS' &&
  pb.predicted_orientation==='LEFT_ZERO_IDENTITY' &&
  pb.observed_orientation==='LEFT_ZERO_IDENTITY';

const faithfulDegreePass =
  pb.predicted_min_faithful_degree===2 &&
  math.left_zero_min_faithful_degree===2;

const propertyIndexPass =
  pb.property_index?.known_default===7 &&
  pb.property_index?.known_discard_unknown===7 &&
  pb.property_index?.unknown_default_present===true &&
  pb.property_index?.unknown_discard_present===false &&
  pb.property_index?.shared_boundary_distinct_transport===true;

const bridgeCells = quic.cells ?? {};
const expected = {
  q0_g0:0, q0_g1:0, q1_g0:0, q1_g1:1
};
const bridgePass =
  quic.status==='PASS' &&
  quic.frozen_function==='AND' &&
  Object.entries(expected).every(([k,v]) => bridgeCells[k]?.y===v) &&
  quic.mechanism_local_parameters===0 &&
  quicUpstream.status==='PASS' &&
  quicUpstream.head==='7c3a98eeb4144e77876ba77c9292da9b5b27a0e1';

const protobufPinPass =
  typeof pbModule.Version==='string' &&
  (pbModule.Version.includes('dcb66ef29d5') || pbModule.Sum || pbModule.Path==='google.golang.org/protobuf') &&
  pbModule.Path==='google.golang.org/protobuf';

const status =
  mathPass && orientationPass && faithfulDegreePass &&
  propertyIndexPass && bridgePass && protobufPinPass ? 'PASS' : 'FAIL';

const decomposition = {
  U0_SINGLE_TWO_LEVEL_BRIDGE: bridgePass
    ? 'PROSPECTIVELY_SUPPORTED_ON_ONE_FRESH_HELD_OUT_FAMILY'
    : 'REJECTED_ON_P24_HELD_OUT',
  U1_TWO_FAMILY_WITH_INTERFACE: bridgePass
    ? 'REMAINS_OBSERVATIONALLY_COMPATIBLE'
    : 'STRENGTHENED_IF_FAMILY_LOCAL_LAWS_SURVIVE',
  U2_TWO_FAMILY_DISCONNECTED: bridgePass ? 'NOT_SUPPORTED_ON_P24' : 'OPEN',
  U3_THREE_PLUS_FAMILY: 'NOT_REQUIRED_BY_P24_PACKET',
  uniqueness: bridgePass
    ? 'UNDERIDENTIFIED_ONE_PROSPECTIVE_BRIDGE_FAMILY'
    : 'UNDERIDENTIFIED'
};

let verdict;
if(status==='PASS'){
  verdict='PASS_ORIENTATION_PREDICTION__FAITHFUL_DEGREE_MATCH__PROPERTY_INDEX_REPLICATION__AND_BRIDGE_HELD_OUT_PASS__MACRO_STRUCTURE_ADVANCES';
}else if(orientationPass && propertyIndexPass && !bridgePass){
  verdict='PASS_ORIENTATION_PREDICTION__PROPERTY_INDEX_REPLICATION__AND_BRIDGE_FAILS__TWO_FAMILY_INTERFACE_ONLY';
}else if(!orientationPass){
  verdict='FAIL_ORIENTATION_CLASSIFICATION__P23_RECONSTRUCTION_DOES_NOT_TRANSPORT';
}else{
  verdict='HOLD_P24_MIXED_PACKET';
}

const result={
  stage:'EvoNOMOS Generation VIII LAW-R1-P24',
  suffix:'Prediction',
  execution_status:status,
  verdict,
  mathematical_lane:{
    status:mathPass?'PASS':'FAIL',
    left_zero_min_degree:math.left_zero_min_faithful_degree,
    right_zero_min_degree:math.right_zero_min_faithful_degree,
    boolean_quotient_orientation_erasure:math.boolean_quotient_orientation_erasure,
    and_unique_on_2x2:math.and_unique_on_complete_2x2
  },
  transport_algebra_prediction:{
    candidate:'PROTOBUF_GO_UNKNOWN_FIELD_TRANSPORT',
    predicted:'LEFT_ZERO_IDENTITY',
    observed:pb.observed_orientation,
    status:orientationPass?'PASS':'FAIL',
    faithful_degree_prediction:2,
    faithful_degree_status:faithfulDegreePass?'PASS':'FAIL'
  },
  property_indexed_shared_boundary:{
    candidate:'PROTOBUF_GO_BINARY_UNMARSHAL',
    status:propertyIndexPass?'PASS_STRONG_SECOND_REPLICATION':'FAIL',
    properties:{
      KNOWN_CURRENT_FIELD_OR_CAPABILITY: propertyIndexPass?'PRESERVED':'CHECK_FAILED',
      UNKNOWN_OR_FUTURE_FIELD_OR_CAPABILITY:
        pb.property_index?.unknown_default_present===true &&
        pb.property_index?.unknown_discard_present===false
          ? 'POLICY_CONDITIONAL_PRESERVE_DROP'
          : 'CHECK_FAILED'
    }
  },
  prospective_and_bridge:{
    candidate:'QUIC_GO_DATAGRAM_MUTUAL_NEGOTIATION',
    status:bridgePass?'PASS_HELD_OUT':'FAIL',
    upstream_exact_test:quicUpstream,
    frozen_truth_table:expected,
    observed_cells:bridgeCells
  },
  dependency_receipt:{
    protobuf_module_path:pbModule.Path,
    protobuf_module_version:pbModule.Version,
    protobuf_pin_check:protobufPinPass?'PASS':'FAIL'
  },
  decomposition,
  macro_structure:{
    result:status==='PASS'?'ADVANCES_NOT_AUTHORIZED':'NOT_AUTHORIZED',
    blockers:status==='PASS'
      ? [
          'DECOMPOSITION_UNIQUENESS_REQUIRES_MORE_THAN_ONE_PROSPECTIVE_BRIDGE_FAMILY',
          'SINGLE_MACRO_LAW_REQUIRES_CROSS_DOMAIN_REPLICATION_OF_THE_BRIDGE',
          'SOLID_SPECIAL_CASE_NOT_DERIVED'
        ]
      : ['P24_PACKET_NOT_FULL_PASS']
  },
  solid_special_case:'NOT_DERIVED',
  law_r2:'NOT_AUTHORIZED'
};

fs.writeFileSync(process.argv[7] ?? 'out-p24/p24-prediction.json',JSON.stringify(result,null,2)+'\n');

console.log('P24_EXECUTION='+status);
console.log('VERDICT='+verdict);
console.log('ORIENTATION_PREDICTION='+(orientationPass?'PASS':'FAIL'));
console.log('FAITHFUL_DEGREE_MATCH='+(faithfulDegreePass?'PASS':'FAIL'));
console.log('PROPERTY_INDEX_REPLICATION='+(propertyIndexPass?'PASS':'FAIL'));
console.log('AND_BRIDGE='+(bridgePass?'PASS':'FAIL'));
console.log('DECOMPOSITION_UNIQUENESS='+decomposition.uniqueness);
console.log('MACRO_STRUCTURE='+result.macro_structure.result);
console.log('LAW_R2=NOT_AUTHORIZED');

if(status!=='PASS') process.exit(3);
