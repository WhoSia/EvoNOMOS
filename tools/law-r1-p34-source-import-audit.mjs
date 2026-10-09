#!/usr/bin/env node
// P34-P1 deliberately bounded CommonJS source import witness extractor.
// The identity of contract/change authority is NOT inferred from require edges.
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";

const root=process.argv[2]||"world";
const previous=process.argv[3]||"out/p34-projection.json";
const output=process.argv[4]||"out/p34-imports.json";
const fileList={
 caller:"server/model/monitor.js",
 dispatcher:"server/notification.js"
};
const blobs={
 caller:"2ad572e53ed051825425f8783c91195cbd243d77",
 dispatcher:"b1a42d003a92e3760f6d33a4be59784a9cb4dbf2"
};
function importWitness(name,filename){
 const raw=fs.readFileSync(root+"/"+filename);
 const sha=crypto.createHash("sha1").update("blob "+raw.length+"\0").update(raw).digest("hex");
 assert.equal(sha,blobs[name]);
 const s=raw.toString("utf8"),w=[];
 const rx=/\brequire\s*\(\s*["']([^"' ]+)["']\s*\)/g;
 for(const hit of s.matchAll(rx)){
  const sourceSpecifier=hit[1],location=hit.index;
  const line=1+s.slice(0,location).split("\n").length-1;
  w.push({from:filename,specifier:sourceSpecifier,line,
   resolved_local_js:sourceSpecifier.startsWith(".")?
    path.posix.normalize(path.posix.join(path.posix.dirname(filename),sourceSpecifier))+
     (path.posix.extname(sourceSpecifier)?"":".js"):
    null,
   syntax:"COMMONJS_STATIC_REQUIRE_CALL"});
 }
 return {sha,imports:w,source:s};
}
const caller=importWitness("caller",fileList.caller);
const dispatcher=importWitness("dispatcher",fileList.dispatcher);
const c=caller.imports.filter(x=>x.specifier==="../notification");
assert.equal(c.length,1);
assert.equal(c[0].line,48);
assert.equal(c[0].resolved_local_js,fileList.dispatcher);
assert.equal(caller.source.split("Notification.send(").length-1,2);
const callsite=caller.source.indexOf("async sendCertNotificationByTargetDays(");
assert.ok(callsite>0);
const second=caller.source.indexOf("Notification.send(",callsite);
assert.ok(second>callsite);
const certLine=caller.source.slice(0,second).split("\n").length;
assert.equal(certLine,1596);
const providers=dispatcher.imports.filter(x=>x.specifier.startsWith("./notification-providers/"));
assert.ok(providers.length>30);
for(const p of providers)assert.equal(p.from,fileList.dispatcher);
const prior=JSON.parse(fs.readFileSync(previous,"utf8"));
assert.equal(prior.collision_pairs_executed,64);
assert.equal(prior.weak_graph_equal,true);
assert.equal(prior.original_git_blob,blobs.caller);
const record={
 schema:"P34_SOURCE_IMPORT_EDGE_AUDIT_V1",
 source_commit:prior.base_source_commit,
 sources:Object.fromEntries(Object.entries(fileList).map(([k,v])=>[k,{file:v,blob:blobs[k]}])),
 static_commonjs_edge_count:{caller:caller.imports.length,dispatcher:dispatcher.imports.length},
 exact_caller_to_notification:c[0],
 certificate_notification_callsite:{file:fileList.caller,line:certLine,token:"Notification.send("},
 notification_dispatcher_provider_require_count:providers.length,
 first_provider_imports:providers.slice(0,5),
 prior_source_bounded_contract_output:prior.verdict,
 graph_scope:"COMMONJS literal require specifiers for 2 pinned files; no AST resolution of dynamic require, import aliases, runtime edges or complete repository",
 authority_status:"NOT_IDENTIFIABLE_FROM_IMPORT_SYNTAX",
 import_edge_claim:"Monitor source imports Notification source; the Provider object may call methods through it, but this does not prove who has the right to edit the abstract contract",
 consequence:"Structural dependency graph and contract-change authority are separate measured or externally certified objects; do not infer DIP owner from import edges",
 ruling:"P34_P1_STATIC_SOURCE_IMPORT_EDGES_PASS__CONTRACT_AUTHORITY_HOLD__LAW_R2_NOT_AUTHORIZED"
};
fs.mkdirSync(output.substring(0,output.lastIndexOf("/"))||".",{recursive:true});
fs.writeFileSync(output,JSON.stringify(record,null,2)+"\n");
console.log(JSON.stringify({status:"PASS",callerRequires:caller.imports.length,
 providerRequires:providers.length,edge:c[0].resolved_local_js,authority:"NOT_IDENTIFIED"}));
