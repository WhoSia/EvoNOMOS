#!/usr/bin/env node
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import {spawnSync} from "node:child_process";
import assert from "node:assert/strict";
const tmp=fs.mkdtempSync(path.join(os.tmpdir(),"p30-evidence-"));
const script="tools/law-r1-p30-cpython-evidence-audit.mjs";
const base={
 stage:"G8 LAW-R1-P30",candidate:"CPython UTF-8 incremental decoder",
 runtime:"3.12.12 (exact source)",implementation:"CPython",
 arm_a:{before:{Q:1,R:"cpython-codecs-utf8-incremental",G:[1,1,1,1],H_pending_length:1,H_pending_hex:"c2",H_flag:0,O_now:""},future:{ok:1,unicode:"©",utf8:"c2a9"}},
 arm_b:{before:{Q:1,R:"cpython-codecs-utf8-incremental",G:[1,1,1,1],H_pending_length:1,H_pending_hex:"c3",H_flag:0,O_now:""},future:{ok:1,unicode:"é",utf8:"c3a9"}},
 current_equal:true,same_W:true,future_different:true,prospective_pending_content_separates:true
};
function execute(obj) {
 const file=path.join(tmp,"probe.json");
 fs.writeFileSync(file,JSON.stringify(obj));
 return spawnSync(process.execPath,[script,file],{encoding:"utf8"});
}
try{
 assert.equal(execute(base).status,0,"positive exact-source-shaped fixture must pass");
 let count=0;
 for(const mutation of [
   x=>x.future_different=false,
   x=>x.current_equal=false,
   x=>x.arm_a.before.G=[1,0,1,1],
   x=>x.arm_a.before.H_pending_length=2,
   x=>x.arm_a.before.H_pending_hex="ff",
   x=>x.arm_b.future.utf8="c2a9",
   x=>x.arm_b.future.unicode="©",
   x=>x.arm_b.before.O_now="x",
   x=>x.runtime="3.13.5",
   x=>x.implementation="PyPy",
   x=>x.arm_a.future.ok=0,
   x=>x.arm_b.before.H_flag=null,
 ]){
   const corrupted=structuredClone(base);
   mutation(corrupted);
   const r=execute(corrupted);
   assert.notEqual(r.status,0,"mutated fixture unexpectedly passed: "+count);
   count++;
 }
 console.log("P30_EVIDENCE_AUDIT_POSITIVE_FIXTURE=PASS");
 console.log("P30_EVIDENCE_AUDIT_MUTATION_REJECTION="+count+"/"+count);
 console.log("P30_EVIDENCE_AUDIT_FIXTURES_NOT_WORLD_EVIDENCE=PASS");
} finally {
 fs.rmSync(tmp,{recursive:true,force:true});
}
