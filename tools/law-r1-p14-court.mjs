import fs from 'node:fs';
const input=process.argv[2] ?? 'out-p14/p14-interventions.json';
const output=process.argv[3] ?? 'out-p14/p14-court.json';
const d=JSON.parse(fs.readFileSync(input,'utf8'));

const repPass=d.representation_invariance?.all_pass===true;
const antiPass=d.anti_rationalization_pass===true;
const compatStable=(d.stable_primitives??[]).includes('COMPATIBILITY_OBLIGATION');
const coexistBounded=(d.bounded_identified??[]).includes('COEXISTENCE_REQUIREMENT');
const authorityBounded=(d.bounded_identified??[]).includes('RELEASE_AUTHORITY');
const sameState=d.same_normalized_X_G_E_conflicting_action_observed===true;

let verdict;
let status='PASS';
let lawR2='NOT_AUTHORIZED';

if(!repPass || !antiPass || d.fresh_source_count<4){
  verdict='HOLD_INTERVENTION_MATRIX_INSUFFICIENT__NO_POST_HOC_EXPANSION';
  status='HOLD';
} else if(sameState){
  verdict='FAIL_CONTEXT_PRIMITIVE_MODEL__DEPENDENCY_COLLAPSE_REQUIRES_RECONSTITUTION';
  lawR2='CANDIDATE_ONLY';
} else if(compatStable && coexistBounded && authorityBounded){
  verdict='PASS_STABLE_COMPATIBILITY_PRIMITIVE_REPLICATED__COEXISTENCE_AND_AUTHORITY_ORTHOGONALIZED_BOUNDED__R2_NOT_AUTHORIZED';
} else if(compatStable){
  verdict='PASS_STABLE_COMPATIBILITY_PRIMITIVE_REPLICATED__COEXISTENCE_AND_AUTHORITY_PARTIALLY_ORTHOGONALIZED__R2_NOT_AUTHORIZED';
} else {
  verdict='PASS_COMPATIBILITY_REPLICATION_ONLY__COEXISTENCE_AUTHORITY_UNDERIDENTIFICATION_RETAINED__R2_NOT_AUTHORIZED';
}

const result={
  stage:'EvoNOMOS Generation VIII LAW-R1-P14',
  status,
  verdict,
  scientific_readout:{
    compatibility_obligation:compatStable?'STABLE_PRIMITIVE_TWO_DOMAIN_EXACT_REPLICATION':'NOT_STABLE',
    coexistence_requirement:coexistBounded?'IDENTIFIED_BOUNDED_ONE_DOMAIN_EXACT':'UNRESOLVED',
    release_authority:authorityBounded?'IDENTIFIED_BOUNDED_ONE_DOMAIN_EXACT_LIFECYCLE_DECOUPLED':'UNRESOLVED',
    dependency_orientation:d.dependency_orientation,
    representation_invariance:repPass?'PASS':'FAIL',
    anti_rationalization:antiPass?'PASS':'FAIL',
    same_normalized_X_G_E_conflicting_action:sameState?'OBSERVED':'NOT_OBSERVED'
  },
  ruling:{
    stable_X_primitives:compatStable?['COMPATIBILITY_OBLIGATION']:[],
    bounded_X_coordinates:[
      ...(coexistBounded?['COEXISTENCE_REQUIREMENT']:[]),
      ...(authorityBounded?['RELEASE_AUTHORITY']:[])
    ],
    lifecycle_phase:'RETAINS_P12_IDENTIFIED_STATUS',
    state_ontology:'SURVIVES_CURRENT_ATTACK',
    policy:'INTERACTION_BEARING',
    law_r2:lawR2,
    next_authority:'REMAIN_WITHIN_LAW_R1'
  },
  caution:'Stable status is granted only to compatibility because it now has two exact cross-domain families. Coexistence and authority remain bounded until independently replicated in second exact domains.'
};

fs.writeFileSync(output,JSON.stringify(result,null,2)+'\n');
console.log(status==='PASS'?'LAW_R1_P14_COURT=PASS':'LAW_R1_P14_COURT=HOLD');
console.log(`VERDICT=${verdict}`);
console.log(`STABLE=${result.ruling.stable_X_primitives.join(',')||'NONE'}`);
console.log(`BOUNDED=${result.ruling.bounded_X_coordinates.join(',')||'NONE'}`);
console.log(`LAW_R2=${lawR2}`);
if(status!=='PASS') process.exit(2);
