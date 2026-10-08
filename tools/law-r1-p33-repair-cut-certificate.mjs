#!/usr/bin/env node
/**
 * P33 finite repair-cut certificate for the already-known Uptime Kuma source.
 * Classical finite hitting-set and kernel-factorization facts; NOT a new theorem.
 * No actual production transport test. The bounded source execution is supplied
 * by tools/law-r1-p33-info-cut-repair-world.mjs.
 */
import assert from "node:assert/strict";
import fs from "node:fs";

const prior=JSON.parse(fs.readFileSync(process.argv[2]??"out/p33-info-cut.json","utf8"));
const out=process.argv[3]??"out/p33-cut-certificate.json";
assert.equal(prior.source_birth,"398482d590daaac0d44e288c9be3bc6f6667f8b8");
assert.equal(prior.original_unchanged_ordinary_oracle,"FAIL");
assert.equal(prior.results.caller.ordinary_oracle,"PASS");
assert.equal(prior.results.dispatcher.ordinary_oracle,"PASS");
assert.equal(prior.results.caller.collision_oracle,"PASS");
assert.equal(prior.results.dispatcher.collision_oracle,"FAIL");
const encode=(name,url)=>"["+name+"]["+url+"] TLS certificate CERT will expire in 5 days";
const witnesses=[];
for(let i=0;i<64;i++){
  const prefix="test"+i;
  const a="https://x"+i+".invalid/";
  const b="https://y"+i+".invalid/";
  const pair=[
    {name:prefix+"]["+a,url:b},
    {name:prefix,url:a+"]["+b}
  ];
  for(const p of pair) new URL(p.url);
  const o0=encode(pair[0].name,pair[0].url);
  const o1=encode(pair[1].name,pair[1].url);
  assert.equal(o0,o1);
  assert.notDeepEqual(pair[0],pair[1]);
  witnesses.push({id:i,distinct_states:pair,common_legacy_observation:o0,
    different_required_context_outputs:true});
}

// Frozen edit-language grammar: a new independent channel must originate
// at caller (monitor.js). A dispatcher-only parser and template-only literal
// edit have the same f(x) for colliding states and cannot solve both.
const options=[
  {id:"CALLER_CONTEXT_CHANNEL",file:"server/model/monitor.js",crosses_information_cut:true},
  {id:"DISPATCHER_STRING_PARSER",file:"server/notification.js",crosses_information_cut:false},
  {id:"TEMPLATE_LITERAL_FALLBACK",file:"server/notification-providers/notification-provider.js",crosses_information_cut:false}
];
const obstructions=witnesses.map(w=>({
  witness_id:w.id,
  necessary_any_of:options.filter(o=>o.crosses_information_cut).map(o=>o.file)
}));
assert.ok(obstructions.every(o=>o.necessary_any_of.length===1));
const allFiles=options.map(x=>x.file),minimalHittingSets=[];
for(let mask=0;mask<(1<<allFiles.length);mask++){
  const selected=allFiles.filter((_,i)=>mask&(1<<i));
  if(!obstructions.every(o=>o.necessary_any_of.some(x=>selected.includes(x))))continue;
  if(selected.some(x=>{
    const less=selected.filter(y=>y!==x);
    return obstructions.every(o=>o.necessary_any_of.some(y=>less.includes(y)));
  }))continue;
  minimalHittingSets.push(selected);
}
assert.deepEqual(minimalHittingSets,[["server/model/monitor.js"]]);
// Satisfying a necessary cut is not sufficient: it also requires behavioral
// compatibility; the real-source caller method was verified under bounded Q.
const report={
  schema:"EVONOMOS_P33_REPAIR_INFORMATION_CUT_CERTIFICATE_V1",
  pinned_birth:prior.source_birth,
  analyzed_input_domain:"64 synthetic collision-pair witnesses with valid URL parser acceptance",
  collision_pair_count:witnesses.length,
  witness_construction:"unescaped [name][url] message from real pinned JS caller",
  witness_examples:witnesses.slice(0,4),
  permitted_edit_language:options,
  minimal_obstruction_hitting_sets:minimalHittingSets,
  significance:"Necessary cut-crossing source site under precisely frozen 3-option edit grammar and no external sidechannel",
  sufficiency:"Not implied by hitting set; checked for one actual source edit by a separate bounded VM harness",
  prior_code_executed_results:{
    original:prior.original_unchanged_ordinary_oracle,
    caller_ordinary:prior.results.caller.ordinary_oracle,
    caller_collision:prior.results.caller.collision_oracle,
    dispatcher_ordinary:prior.results.dispatcher.ordinary_oracle,
    dispatcher_collision:prior.results.dispatcher.collision_oracle
  },
  strong_rival:"Reiter conflict hitting set and standard program synthesis already cover abstract characterization; NOT a novel theorem or H-vs-B2 win",
  no_side_channel_assumption:true,
  not_claimed:["general soundness for arbitrary JS","complete program repair","production Q","unseen genuine software requirement forecast","novel mathematical theorem"],
  verdict:"PINNED_SOURCE_INFORMATION_CUT_CERTIFICATE_METHOD_PASS__SCIENCE_HOLD"
};
fs.mkdirSync(out.slice(0,out.lastIndexOf("/"))||".",{recursive:true});
fs.writeFileSync(out,JSON.stringify(report,null,2)+"\n");
console.log(JSON.stringify({status:"PASS",witnesses:witnesses.length,minimal_hitting_sets:minimalHittingSets.length,authority:"METHOD_ONLY"}));
