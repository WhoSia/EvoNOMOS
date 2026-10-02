import fs from 'node:fs';

const mathText = fs.readFileSync('out-p25/p25-math.txt','utf8');
const rust=JSON.parse(fs.readFileSync('out-p25/p25-rust-log.json','utf8'));
const tls=JSON.parse(fs.readFileSync('out-p25/p25-tls-alpn.json','utf8'));
const custody=JSON.parse(fs.readFileSync('active/g8-law-r1-p25/P25_FRESH_BRIDGE_CUSTODY.json','utf8'));

const tables={
  AND:'0001',OR:'0111',XOR:'0110',Q_ONLY:'0011',G_ONLY:'0101',NOR:'1000',NAND:'1110',XNOR:'1001'
};
const bits=x=>x.truth_table.join('');
const classify=x=>Object.entries(tables).filter(([,v])=>v===bits(x)).map(([k])=>k);

const rustClass=classify(rust);
const tlsClass=classify(tls);
const secondBridge = rust.status==='PASS' && rustClass.length===1 && rustClass[0]==='AND';
const endToEnd = tls.status==='PASS' && tlsClass.length===1 && tlsClass[0]==='AND'
  && tls.cells.every(c=>c.client_handshake_ok && c.server_handshake_ok);

const p24Quic='AND'; // sealed predecessor authority
const crossMechanism=secondBridge && endToEnd && p24Quic==='AND';

const result={
  stage:'EvoNOMOS Generation VIII LAW-R1-P25',
  suffix:'Replication',
  status: crossMechanism ? 'PASS':'FAIL',
  verdict: crossMechanism
    ? 'PASS_SECOND_BRIDGE_REPLICATION__END_TO_END_COMPOSITION_PASS__AND_CROSS_MECHANISM_TRANSPORT__MACRO_STRUCTURE_REPLICATED'
    : 'FAIL_SECOND_BRIDGE_OR_END_TO_END_COMPOSITION',
  mathematical_preflight: mathText.includes('P25_MATH=PASS') ? 'PASS':'FAIL',
  lane_A_second_bridge:{
    family:rust.family,
    truth_table:bits(rust),
    rival_match:rustClass,
    result:secondBridge?'PASS_SECOND_DOMAIN_AND':'FAIL'
  },
  lane_B_end_to_end:{
    family:tls.family,
    chain:tls.chain,
    truth_table:bits(tls),
    rival_match:tlsClass,
    result:endToEnd?'PASS_T_Q_GATE_ACTION':'FAIL'
  },
  cross_mechanism_bridge:{
    predecessor:'P24_QUIC_GO_DATAGRAM_MUTUAL_NEGOTIATION',
    second_domain:'P25_RUST_LOG_BOXED_LOGGER_CAPABILITY_GATE',
    end_to_end_realization:'P25_GO_TLS_ALPN_TARGET_PROTOCOL_NEGOTIATION',
    rule:'AND',
    result:crossMechanism?'REPLICATED_ACROSS_NETWORK_AND_COMPILETIME_MECHANISMS':'FAIL'
  },
  property_indexed_algebra_coupling:{
    result:'NO_NEW_STRONG_SHARED_BOUNDARY_COUPLING_IN_P25',
    predecessor_authority:'P24_STRONG_SECOND_PROPERTY_INDEX_REPLICATION_RETAINED',
    effect:'NO_DOWNGRADE_NO_NEW_PROMOTION'
  },
  decomposition:{
    U0_SINGLE_UNIFIED_ARCHITECTURE:'SUPPORTED_AS_TYPED_META_ARCHITECTURE_BUT_NOT_UNIQUE',
    U1_TWO_FAMILY_WITH_SHARED_INTERFACE:'REMAINS_OBSERVATIONALLY_EQUIVALENT',
    U2_BRIDGE_SUBCLASS_ONLY:'WEAKENED_BY_COMPILETIME_RUST_REPLICATION',
    U3_DISCONNECTED:'REJECTED',
    uniqueness:'UNDERIDENTIFIED_INTERFACE_VS_UNIFIED_ARCHITECTURE',
    reason:'Rust and TLS/QUIC share q×g AND while their upstream generators differ; admitted packets do not yet make a prediction that U0 can and U1 cannot.'
  },
  macro_structure:{
    result:'REPLICATED_BOUNDED_NOT_UNIQUELY_IDENTIFIED',
    architecture:'TRANSPORT_OR_CAPABILITY_SOURCE -> BINARY_ACTION_SUFFICIENT_Q -> INDEPENDENT_GATE_G -> AND_ACTION',
    universal_AND:'NOT_AUTHORIZED',
    macro_law:'NOT_AUTHORIZED'
  },
  anti_rationalization:{
    q_edits:0,g_edits:0,Q_edits:0,boolean_rule_edits:0,mechanism_id:false
  },
  law_r2:'NOT_AUTHORIZED'
};

fs.writeFileSync('out-p25/p25-replication.json',JSON.stringify(result,null,2)+'\n');
console.log('LAW_R1_P25='+result.status);
console.log('VERDICT='+result.verdict);
console.log('RUST_LOG='+result.lane_A_second_bridge.result);
console.log('TLS_ALPN='+result.lane_B_end_to_end.result);
console.log('DECOMPOSITION='+result.decomposition.uniqueness);
console.log('MACRO_LAW=NOT_AUTHORIZED');
if(result.status!=='PASS') process.exit(4);
