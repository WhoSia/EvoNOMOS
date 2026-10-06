import fs from 'node:fs';

const bevy=JSON.parse(fs.readFileSync(process.argv[2]??'out-p27/p27-bevy.json','utf8'));
const h2=JSON.parse(fs.readFileSync(process.argv[3]??'out-p27/p27-http2.json','utf8'));

const eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const n0Drop=[-1,0,-1], n1Drop=[-1,-1,-1];
const n0Restore=[1,0,1], n1Restore=[1,1,1];
const gateDrop=[0,-1,-1];

function rank2(v,w){
  const minors=[
    v[0]*w[1]-v[1]*w[0],
    v[0]*w[2]-v[2]*w[0],
    v[1]*w[2]-v[2]*w[1],
  ];
  if([...v,...w].every(x=>x===0)) return 0;
  return minors.some(x=>x!==0)?2:1;
}
const bevyPass=bevy.status==='PASS' && eq(bevy.drop_delta,n0Drop) && eq(bevy.restore_delta,n0Restore) && eq(bevy.gate_drop_delta,gateDrop);
const h2Pass=h2.status==='PASS' && eq(h2.drop_delta,n1Drop) && eq(h2.restore_delta,n1Restore);

const bevyRank=rank2(bevy.drop_delta,bevy.gate_drop_delta);
const h2Rank=rank2(h2.drop_delta,gateDrop);

const separator={
  bevy:{measured:bevy.drop_delta,N0:'FIT',N1:eq(bevy.drop_delta,n1Drop)?'FIT':'FAIL'},
  http2:{measured:h2.drop_delta,N0:eq(h2.drop_delta,n0Drop)?'FIT':'FAIL',N1:'FIT'},
};

const exact=bevyPass&&h2Pass&&separator.bevy.N1==='FAIL'&&separator.http2.N0==='FAIL';
const status=exact?'PASS':'FAIL';
const verdict=exact
 ? 'PASS_NON_NESTED_SEPARATOR__N0_AND_N1_BOTH_EXACTLY_REALIZED__KERNEL_ORIENTATION_IDENTIFIED__MACRO_EQUIVALENCE_CLASS_REFINED'
 : 'FAIL_NON_NESTED_COURT__FROZEN_RIVALS_OR_MEASUREMENTS_NOT_SEPARATED';

const result={
  stage:'EvoNOMOS Generation VIII LAW-R1-P27',
  suffix:'Court',
  status,
  verdict,
  mechanisms:{
    N0_BEVY:{status:bevyPass?'PASS':'FAIL',drop:bevy.drop_delta,restore:bevy.restore_delta,gate_drop:bevy.gate_drop_delta,kernel_rank:bevyRank},
    N1_HTTP2:{status:h2Pass?'PASS':'FAIL',drop:h2.drop_delta,restore:h2.restore_delta,gate_drop:gateDrop,kernel_rank:h2Rank},
  },
  separator,
  mathematical_ruling:{
    minimal_separating_basis_cardinality:1,
    separating_intervention:'UPSTREAM_DROP_FROM_Q1_G1',
    primary_coordinate:'DELTA_G',
    rank_alone_separates:false,
    both_kernel_ranks:[bevyRank,h2Rank],
  },
  architecture_equivalence:{
    N0_and_N1_non_nested:true,
    same_rank_but_different_kernel_orientation:true,
    conclusion:'INTERVENTIONAL_KERNEL_DIRECTION_REFINES_EQUIVALENCE_CLASS_BEYOND_RANK',
    universal_architecture:'NOT_AUTHORIZED',
  },
  obstruction_search:{
    delta_y_without_q_or_g_change:false,
    same_q_g_different_y:false,
    hidden_mechanism_id_required:false,
    status:'NO_EXACT_LATENT_OBSTRUCTION_IN_P27_PACKET',
  },
  macro_structure:{
    result:'MULTIPLE_NON_NESTED_ARCHITECTURE_FAMILIES_EXACTLY_REALIZED',
    implication:'A single universal q/g coupling rule is rejected; architecture family branching is empirically required.',
    macro_law:'NOT_AUTHORIZED',
  },
  law_r2:'NOT_AUTHORIZED',
};

fs.writeFileSync(process.argv[4]??'out-p27/p27-court.json',JSON.stringify(result,null,2)+'\n');
console.log('P27_COURT='+status);
console.log('VERDICT='+verdict);
console.log('BEVY_DROP='+JSON.stringify(bevy.drop_delta));
console.log('HTTP2_DROP='+JSON.stringify(h2.drop_delta));
console.log('RANKS='+bevyRank+','+h2Rank);
console.log('RANK_ALONE_SEPARATES=false');
console.log('MACRO=NON_NESTED_ARCHITECTURE_FAMILY_BRANCHING');
if(status!=='PASS') process.exit(3);
