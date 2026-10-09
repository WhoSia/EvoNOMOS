#!/usr/bin/env node
// P34 source-pinned weak-graph projection separator: contract channel only.
// Retrospective known issue #7639; not independent prospective predictive proof.
import assert from "node:assert/strict";
import fs from "node:fs";
import crypto from "node:crypto";
import vm from "node:vm";

const root=process.argv[2]||"world";
const output=process.argv[3]||"out/p34-projection.json";
const path="server/model/monitor.js";
const raw=fs.readFileSync(root+"/"+path);
const sha=crypto.createHash("sha1").update("blob "+raw.length+"\0").update(raw).digest("hex");
assert.equal(sha,"2ad572e53ed051825425f8783c91195cbd243d77");
const source=raw.toString("utf8");
const anchor="async sendCertNotificationByTargetDays(certCN, certType, daysRemaining, targetDays, notificationList) {";
const terminator="\n    /**\n     * Get the status of the previous heartbeat";
const a=source.indexOf(anchor),b=source.indexOf(terminator,a);
assert.ok(a>=0 && b>a && source.indexOf(anchor,a+1)<0);
const end=source.lastIndexOf("\n    }",b);
assert.ok(end>a);
const original=source.slice(a,end+6);
const tick=String.fromCharCode(96),i="$"+"{";
const before=tick+"["+i+"this.name}]["+i+"this.url}] "+i+"certType} certificate "+i+"certCN} will expire in "+i+"daysRemaining} days"+tick+"\n                );";
const after=tick+"["+i+"this.name}]["+i+"this.url}] "+i+"certType} certificate "+i+"certCN} will expire in "+i+"daysRemaining} days"+tick+",\n                    { name: this.name, type: this.type, url: this.url, hostname: this.hostname }\n                );";
assert.equal(original.split(before).length-1,1);
const withContext=original.replace(before,after);
function callProjection(method){
 // Deliberately weak projection: module/method identity and static
 // Notification.send call target; it DOES NOT inspect arity/argument dataflow.
 return {
  owner:path,
  method:"sendCertNotificationByTargetDays",
  static_call_targets:[...method.matchAll(/Notification\.send\s*\(/g)].map(()=>"Notification.send")
 };
}
const graph0=callProjection(original),graph1=callProjection(withContext);
assert.deepEqual(graph0,graph1);
assert.equal(graph0.static_call_targets.length,1);
assert.equal(original.includes("this.name"),true);
assert.equal(withContext.includes("this.name"),true);

async function execute(method,state){
 const seen=[];
 const Notification={send:async(...args)=>{seen.push(args);return "OK";}};
 const R={getRow:async()=>null,exec:async()=>null};
 const log={debug:()=>{},error:()=>{}};
 const C=vm.runInNewContext("(class Monitor {"+method+"})",{Notification,R,log});
 const obj=new C();
 Object.assign(obj,{id:3,type:"http",...state});
 await obj.sendCertNotificationByTargetDays("CERT","TLS",5,7,[
  {name:"fixture",config:JSON.stringify({type:"fixture"})}
 ]);
 assert.equal(seen.length,1);
 const args=seen[0];
 return {arity:args.length,msg:args[1],
  context:args.length>=3?JSON.parse(JSON.stringify(args[2])):null};
}
function encode(s){return "["+s.name+"]["+s.url+"] TLS certificate CERT will expire in 5 days";}
const pair=[];
for(let k=0;k<64;k++){
 const x="https://x"+k+".invalid/",y="https://y"+k+".invalid/";
 const states=[
  {name:"test"+k+"]["+x,url:y},
  {name:"test"+k,url:x+"]["+y}
 ];
 states.forEach(z=>new URL(z.url));
 assert.equal(encode(states[0]),encode(states[1]));
 assert.notDeepEqual(states[0],states[1]);
 const legacy=await Promise.all(states.map(z=>execute(original,z)));
 const enriched=await Promise.all(states.map(z=>execute(withContext,z)));
 assert.equal(legacy[0].arity,2);assert.equal(legacy[1].arity,2);
 assert.equal(enriched[0].arity,3);assert.equal(enriched[1].arity,3);
 assert.equal(legacy[0].msg,legacy[1].msg);
 assert.equal(enriched[0].msg,enriched[1].msg);
 assert.equal(legacy[0].msg,enriched[0].msg);
 assert.equal(legacy[0].context,null);assert.equal(legacy[1].context,null);
 assert.equal(enriched[0].context.name,states[0].name);
 assert.equal(enriched[0].context.url,states[0].url);
 assert.equal(enriched[1].context.name,states[1].name);
 assert.equal(enriched[1].context.url,states[1].url);
 assert.notDeepEqual(enriched[0].context,enriched[1].context);
 pair.push({index:k,same_legacy_message:true,distinct_demand_context:true,
  original_arity:2,enriched_arity:3});
}
const report={
 schema:"P34_SOURCE_PINNED_GRAPH_PROJECTION_CONTRACT_SEPARATOR_V1",
 base_source_commit:"398482d590daaac0d44e288c9be3bc6f6667f8b8",
 original_git_blob:sha,
 arms:["pinned original caller","one-site experimental context-forwarding edit"],
 projection_scope:"ONLY method owner + literal Notification.send target, no typed arguments, module import graph completeness or call dataflow",
 weak_graph_projection:graph0,weak_graph_equal:true,
 actual_code_method_executed:true,
 collision_pairs_executed:pair.length,
 matched_legacy_message_in_each_pair:true,
 original_observation:"message and notification config; NO structured monitor context",
 enriched_observation:"same legacy message and notification config; structured monitorJSON argument added",
 stronger_static_competitor:"M1 with call arity or typed dataflow WOULD distinguish 2 versus 3 arguments; NO M2 scientific victory",
 output_target:"availability of exact monitor name and URL in the notification argument channel, NOT complete runtime repair cost",
 existing_demand:"legacy human-readable certificate message (unchanged in both arms)",
 extended_demand:"structured name and URL available for downstream notification template",
 control:"already-known issue #7639, retrospectively selected",
 theory:"Equal weak graph projection with unequal observation adequacy shows graph-only projection cannot exactly identify this target on these two source worlds. Standard factorization fact.",
 no_claims:["independent pre-registered future demand","M1 or CSDG defeated","full Uptime Kuma template/transports production Q","measured future maintenance cost","universal software Braess mechanism"],
 verdict:"P34_PINNED_WEAK_GRAPH_INSUFFICIENCY_METHOD_PASS__RICH_STATIC_M1_NOT_BEATEN__LAW_R2_HOLD"
};
fs.mkdirSync(output.substring(0,output.lastIndexOf("/"))||".",{recursive:true});
fs.writeFileSync(output,JSON.stringify(report,null,2)+"\n");
console.log(JSON.stringify({status:"PASS",pairs:pair.length,weak_graph_equal:true,
  original_argument_count:2,enriched_argument_count:3}));
