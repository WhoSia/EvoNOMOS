#!/usr/bin/env node
import fs from 'node:fs';

const base=process.argv[2]??'active/g8-origin-r1-p11-p1';
const read=p=>JSON.parse(fs.readFileSync(base+'/'+p,'utf8'));
const demand=read('contract/DUAL_REAL_DEMAND_CONTRACT.json');
const rival=read('contract/RIVAL_CONSTITUTION.json');
const outcome=read('contract/OUTCOME_FIREWALL.json');
const oracle=read('contract/SEARCH_FETCH_EXPOSURE_ORACLE.json');
const fail=m=>{console.error('PRESEAL_FAIL '+m);process.exit(1);};

if(demand.world.exact_source!=='dd421b79216c9b42eefd7b0191e546919f8be3f1') fail('source');
if(demand.phase0.issue!==852||demand.phase1.issue!==853) fail('demand pair');
if(!demand.freeze.pair_frozen_before_treatment) fail('pair not frozen');
if(JSON.stringify(demand.phase0.required_capabilities)!=='["search"]') fail('exa capability');
if(JSON.stringify(demand.phase1.required_capabilities)!=='["search"]') fail('tavily capability');

const wide=rival.treatments.WIDE_BOUNDARY_REUSE;
const seg=rival.treatments.CAPABILITY_SEGREGATED;
if(!wide.must_preserve.some(x=>x.includes('search and fetch'))) fail('wide boundary not frozen');
if(!wide.must_do.some(x=>x.includes('truthful Exa fetch'))) fail('wide exa conformance missing');
if(!wide.must_do.some(x=>x.includes('truthful Tavily extract/fetch'))) fail('wide tavily conformance missing');
if(!seg.must_do.some(x=>x.includes('independently satisfiable'))) fail('segregation missing');
if(!seg.must_do.some(x=>x.includes('Expose')||x.includes('expose web_fetch'))) fail('seg exposure missing');

if(JSON.stringify(outcome.vector_by_phase)!=='["S","L","C","A","Q"]') fail('vector');
if(outcome.scalarization!==false||outcome.winner!=='FORBIDDEN') fail('winner firewall');
if(outcome.breach!=='HOLD_OUTCOME_BLINDNESS_BREACH; no same-wave rescue') fail('breach semantics');
if(oracle.oracle_id!=='SEARCH_FETCH_EXPOSURE_V01') fail('oracle');
if(!oracle.forbidden_successes.some(x=>x.includes('unsupported'))) fail('stub loophole');
if(rival.shared_constraints.winner!==null) fail('rival winner leaked');

const treatmentCandidates=[
  base+'/arms',
  base+'/materialized',
  base+'/treatments'
];
for(const p of treatmentCandidates){
  if(fs.existsSync(p)) fail('treatment bytes exist at '+p);
}

console.log('P11_P1_CONSTITUTION=PASS');
console.log('P11_P1_TREATMENT_BYTES=ZERO');
console.log('P11_P1_OUTCOMES=CLOSED');
