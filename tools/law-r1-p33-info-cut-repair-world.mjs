#!/usr/bin/env node
// P33 pinned Uptime Kuma source repair candidates, bounded VM oracle.
// #7639 known retrospectively; NOT a blind prediction nor full production Q.
import assert from "node:assert/strict";
import fs from "node:fs";
import crypto from "node:crypto";
import vm from "node:vm";

const world=process.argv[2] || "world";
const out=process.argv[3] || "out/p33-info-cut.json";
const paths={
 caller:"server/model/monitor.js",
 dispatcher:"server/notification.js",
 template:"server/notification-providers/notification-provider.js"
};
const blobs={
 caller:"2ad572e53ed051825425f8783c91195cbd243d77",
 dispatcher:"b1a42d003a92e3760f6d33a4be59784a9cb4dbf2",
 template:"42079176c01cd2e6d46160bb6f6408d4ba263fd7"
};
const source={};
for(const key of Object.keys(paths)){
 const raw=fs.readFileSync(world+"/"+paths[key]);
 const hash=crypto.createHash("sha1").update("blob "+raw.length+"\0").update(raw).digest("hex");
 assert.equal(hash,blobs[key],"unexpected pinned source: "+key);
 source[key]=raw.toString("utf8");
}
function extract(s,anchor,next){
 const a=s.indexOf(anchor),b=s.indexOf(next,a);
 assert.ok(a>=0 && b>a,"missing source anchor: "+anchor);
 assert.equal(s.indexOf(anchor,a+anchor.length),-1);
 const end=s.lastIndexOf("\n    }",b);
 assert.ok(end>a);
 return s.slice(a,end+6);
}
const callerAnchor="async sendCertNotificationByTargetDays(certCN, certType, daysRemaining, targetDays, notificationList) {";
const dispatchAnchor="static async send(notification, msg, monitorJSON = null, heartbeatJSON = null) {";
const caller=extract(source.caller,callerAnchor,"\n    /**\n     * Get the status of the previous heartbeat");
const dispatch=extract(source.dispatcher,dispatchAnchor,"\n    /**\n     * Save a notification");
const address=extract(source.template,"extractAddress(monitorJSON) {","\n    /**\n     * Renders a message template");
const render=extract(source.template,"async renderTemplate(template, msg, monitorJSON, heartbeatJSON) {","\n    /**\n     * Throws an error");
const tick=String.fromCharCode(96), interpolation="$"+"{";
const existing=tick+"["+interpolation+"this.name}]["+interpolation+"this.url}] "+interpolation+"certType} certificate "+interpolation+"certCN} will expire in "+interpolation+"daysRemaining} days"+tick+"\n                );";
const changed=tick+"["+interpolation+"this.name}]["+interpolation+"this.url}] "+interpolation+"certType} certificate "+interpolation+"certCN} will expire in "+interpolation+"daysRemaining} days"+tick+",\n                    { name: this.name, type: this.type, url: this.url, hostname: this.hostname }\n                );";
assert.equal(caller.split(existing).length-1,1,"caller signature drift");
const callerFix=caller.replace(existing,changed);

const dispatchAdd=dispatchAnchor+"\n"+
'        if (monitorJSON === null && typeof msg === "string" && msg.includes(" certificate ")) {\n'+
'            const parsed = /^\\[([^\\]]+)\\]\\[([^\\]]+)\\] /.exec(msg);\n'+
'            if (parsed) monitorJSON = { name: parsed[1], url: parsed[2], type: "http" };\n'+
'        }\n';
assert.equal(dispatch.split(dispatchAnchor+"\n").length-1,1);
const dispatchFix=dispatch.replace(dispatchAnchor+"\n",dispatchAdd);
class FakeLiquid{
 parse(s){return s;}
 render(template,c){return template.replace(/\{\{\s*([A-Za-z]+)\s*\}\}/g,(_x,k)=>String(c[k]));}
}
const provider=vm.runInNewContext("({"+address+","+render+"})",{Liquid:FakeLiquid,DOWN:0});
async function run(arm,monitor){
 const code=arm==="caller"?dispatch:dispatchFix;
 const notification=vm.runInNewContext("(class Notification {"+code+"})");
 let observed=null;
 notification.providerList={fixture:{
  async send(config,msg,monitorJSON,heartbeatJSON){
   observed=await provider.renderTemplate("{{ name }}|{{ hostnameOrURL }}",msg,monitorJSON,heartbeatJSON);
   return "OK";
  }
 }};
 const R={getRow:async()=>null,exec:async()=>null};
 const log={debug:()=>{},error:()=>{}};
 const clazz=vm.runInNewContext("(class Monitor {"+(arm==="caller"?callerFix:caller)+"})",{Notification:notification,R,log});
 const o=new clazz();
 Object.assign(o,{id:3,type:"http",...monitor});
 await o.sendCertNotificationByTargetDays("CERT","TLS",5,7,[{name:"fixture",config:JSON.stringify({type:"fixture"})}]);
 assert.notEqual(observed,null);
 return observed;
}
const ordinary=[{name:"alpha",url:"https://one.invalid/"},{name:"beta",url:"https://two.invalid/path"}];
const collision=[{name:"alpha][https://x.invalid/",url:"https://y.invalid/"},{name:"alpha",url:"https://x.invalid/][https://y.invalid/"}];
for(const o of ordinary.concat(collision)) new URL(o.url);
const encode=o=>"["+o.name+"]["+o.url+"] TLS certificate CERT will expire in 5 days";
assert.equal(encode(collision[0]),encode(collision[1]));
assert.notDeepEqual(collision[0],collision[1]);
const results={};
for(const arm of ["caller","dispatcher"]){
 const basic=await Promise.all(ordinary.map(o=>run(arm,o)));
 const expectedOrdinary=ordinary.map(o=>o.name+"|"+o.url);
 assert.deepEqual(basic,expectedOrdinary,"bounded ordinary oracle failed: "+arm);
 const extended=await Promise.all(collision.map(o=>run(arm,o)));
 const expectedExtended=collision.map(o=>o.name+"|"+o.url);
 results[arm]={
  edited_files:arm==="caller"?[paths.caller]:[paths.dispatcher],
  ordinary_oracle:"PASS",
  collision_oracle:JSON.stringify(extended)===JSON.stringify(expectedExtended)?"PASS":"FAIL",
  collision_actual:extended,collision_expected:expectedExtended
 };
}
assert.equal(results.caller.collision_oracle,"PASS");
assert.equal(results.dispatcher.collision_oracle,"FAIL");
const report={
 schema:"P33_BOUNDED_REAL_SOURCE_ALTERNATIVE_REPAIRS_AND_INFO_CUT_V1",
 source_birth:"398482d590daaac0d44e288c9be3bc6f6667f8b8",
 pinned_git_blobs:blobs,
 source_issue_seen_before_choice:"https://github.com/louislam/uptime-kuma/issues/7639",
 candidate_edit_grammar:"two bounded JS changes: source caller forwards context vs notification dispatch parses the old message",
 modification_supports_are_disjoint_singletons:true,
 safe_domain_oracle_both_pass:true,
 extended_collision_oracle_only_caller_passes:true,
 indistinguishable_legacy_message:encode(collision[0]),
 distinct_required_outputs:collision.map(o=>o.name+"|"+o.url),
 results,
 logical_proposition:"If observation f(x)=f(y) and target g(x)!=g(y), no deterministic downstream decoder h can satisfy g=h composed with f for both.",
 novelty_ceiling:"STANDARD_KERNEL_FACTORIZATION_THEOREM_APPLIED_TO_PINNED_SOURCE_NOT_NEW_THEOREM",
 execution_scope:"Pinned extracted real JS methods in VM with DB/notification/Liquid mocks. No full server, external notification, customer configuration or production equivalence.",
 verdict:"BOUNDED_TWO_REPAIR_OPTIONS_PASS__EXTENDED_ORACLE_DEFEATS_STRING_RECOVERY__STRONG_B2_NOT_BEATEN__LAW_R2_HOLD"
};
fs.mkdirSync(out.substring(0,out.lastIndexOf("/"))||".",{recursive:true});
fs.writeFileSync(out,JSON.stringify(report,null,2)+"\n");
console.log(JSON.stringify({result:"PASS",ordinary:2,collision:2,caller:results.caller.collision_oracle,dispatcher:results.dispatcher.collision_oracle}));
