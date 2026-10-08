#!/usr/bin/env node
// P31: non-scalarized source-treatment metrics from real, bounded worktrees.
// A successful code diff is not a predictive structural law.
import fs from "node:fs";
import {execFileSync} from "node:child_process";
const [direct,shared,output]=process.argv.slice(2);
if(!direct||!shared)throw new Error("Usage: node ... DIRECT SHARED OUTPUT");
const run=(cwd,args)=>execFileSync("git",["-C",cwd,...args],{encoding:"utf8"});
function measure(root,label){
 const tracked=run(root,["diff","--numstat"]).trim().split("\n").filter(Boolean).map(line=>{
  const [a,d,...part]=line.split("\t");
  return {path:part.join("\t"),added:Number(a),removed:Number(d)};
 });
 const untracked=run(root,["ls-files","--others","--exclude-standard"]).trim().split("\n").filter(Boolean);
 const ancillary=untracked.map(path=>({path,lines:fs.readFileSync(root+"/"+path,"utf8").split("\n").length-1}));
 const code=tracked.filter(r=>r.path.endsWith(".go"));
 const tests=ancillary.filter(r=>r.path.endsWith("_test.go"));
 const sql=ancillary.filter(r=>r.path.endsWith(".sql"));
 return {architecture:label,
   tracked_source:tracked,
   new_source:ancillary,
   proxy_vector:{
     S_modified_tracked_files:tracked.length,
     L_tracked_go_lines_added:code.reduce((a,b)=>a+b.added,0),
     L_tracked_go_lines_removed:code.reduce((a,b)=>a+b.removed,0),
     new_test_lines:tests.reduce((a,b)=>a+b.lines,0),
     new_sql_lines:sql.reduce((a,b)=>a+b.lines,0)
   },
   methodology:"Partial S/L source-surface measurements only; C capability burden, A architectural overhead and Q semantic equivalence need separate adjudication."
 };
}
const result={stage:"G8 LAW-R1-P31",candidate:"Team shared vs duplicated source-maintenance",data:[measure(direct,"DIRECT"),measure(shared,"SHARED")],authority:{
  "s_and_l_measured":true,"c_a_q_measured":false,"causal_architectural_advantage":false,
  "independent_followup":false,"law_r2":false
 }};
const text=JSON.stringify(result,null,2)+"\n";
process.stdout.write(text);
if(output)fs.writeFileSync(output,text);
