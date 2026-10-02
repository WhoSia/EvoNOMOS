import fs from 'node:fs';

const go = JSON.parse(fs.readFileSync(process.argv[2] ?? 'out-p26/p26-otel-go.json','utf8'));
const php = JSON.parse(fs.readFileSync(process.argv[3] ?? 'out-p26/p26-otel-php.json','utf8'));

const expected = [
  ['baseline',1,0,0],
  ['drop',0,0,0],
  ['restore',1,0,0],
  ['baseline',1,1,1],
  ['drop',0,1,0],
  ['restore',1,1,1],
];

function key(r){ return r.intervention + '/' + r.g; }

function analyze(packet){
  const map = new Map(packet.rows.map(r => [key(r), r]));
  const errors = [];
  for(const [name,q,g,y] of expected){
    const r = map.get(name + '/' + g);
    if(!r){ errors.push('missing:' + name + '/' + g); continue; }
    if(r.q !== q) errors.push('q:' + name + '/' + g + ':' + r.q + '!=' + q);
    if(r.y !== y) errors.push('y:' + name + '/' + g + ':' + r.y + '!=' + y);
    if(r.gate_before !== g || r.gate_after !== g) errors.push('gate:' + name + '/' + g);
    if(r.y !== (r.q & r.g)) errors.push('mediation:' + name + '/' + g);
  }
  return {
    mechanism: packet.mechanism,
    source_status: packet.status,
    errors,
    gate_invariance: errors.filter(x => x.startsWith('gate:')).length === 0,
    mediation: errors.filter(x => x.startsWith('mediation:') || x.startsWith('y:')).length === 0,
    drop_q: map.get('drop/1')?.q,
    restore_q: map.get('restore/1')?.q,
    signature: [...map.values()]
      .sort((a,b) => key(a).localeCompare(key(b)))
      .map(r => key(r) + ':' + r.q + r.y)
      .join('|')
  };
}

const ga = analyze(go);
const pa = analyze(php);

const sameInducedActions =
  ga.drop_q === 0 && pa.drop_q === 0 &&
  ga.restore_q === 1 && pa.restore_q === 1;

const exactPackets = ga.errors.length === 0 && pa.errors.length === 0;
const naturality = exactPackets && sameInducedActions;
const gateInvariant = ga.gate_invariance && pa.gate_invariance;
const mediation = ga.mediation && pa.mediation;
const u0Survives = naturality && gateInvariant && mediation;

const result = {
  stage:'EvoNOMOS Generation VIII LAW-R1-P26',
  suffix:'Experiment',
  status:u0Survives ? 'PASS' : 'FAIL',
  scientific_verdict:u0Survives
    ? 'PASS_U0_INTERVENTIONAL_SURVIVAL__CROSS_LANGUAGE_NATURALITY_AND_MEDIATION_PASS__UNIQUENESS_NOT_AUTHORIZED'
    : 'FAIL_U0_INTERVENTIONAL_INVARIANT__SHARED_INTERFACE_RETAINS_AUTHORITY',
  mechanisms:{go:ga,php:pa},
  typed_intervention:{
    family:'TRACE_SAMPLED_STATE_DROP_RESTORE',
    quotient_drop:'1_TO_0',
    quotient_restore:'0_TO_1',
    mechanism_independent:naturality
  },
  u0_invariants:{
    quotient_naturality:naturality ? 'PASS' : 'FAIL',
    gate_invariance:gateInvariant ? 'PASS' : 'FAIL',
    complete_mediation:mediation ? 'PASS' : 'FAIL',
    shared_and:exactPackets ? 'PASS' : 'FAIL',
    mechanism_id_required:false
  },
  architecture_identifiability:{
    U0_UNIFIED_RESTRICTED:u0Survives ? 'SURVIVES_FROZEN_INTERVENTIONS' : 'FALSIFIED',
    U1_SHARED_INTERFACE_SUPERCLASS:'REMAINS_COMPATIBLE',
    uniqueness:'NOT_AUTHORIZED_BY_NESTED_MODEL_THEOREM',
    identified_object:'INTERVENTIONAL_EQUIVALENCE_CLASS_UNDER_FROZEN_DROP_RESTORE'
  },
  macro_structure:{
    result:u0Survives ? 'BOUNDED_INTERVENTIONAL_SURVIVAL_NOT_UNIQUE' : 'UNIFIED_ARCHITECTURE_REJECTED',
    macro_law:'NOT_AUTHORIZED'
  },
  law_r2:'NOT_AUTHORIZED'
};

fs.writeFileSync(process.argv[4] ?? 'out-p26/p26-experiment.json',JSON.stringify(result,null,2)+'\n');
console.log('P26_EXPERIMENT=' + result.status);
console.log('VERDICT=' + result.scientific_verdict);
console.log('NATURALITY=' + result.u0_invariants.quotient_naturality);
console.log('GATE_INVARIANCE=' + result.u0_invariants.gate_invariance);
console.log('MEDIATION=' + result.u0_invariants.complete_mediation);
console.log('UNIQUENESS=NOT_AUTHORIZED_BY_NESTED_MODEL_THEOREM');
if(result.status !== 'PASS') process.exit(3);
