#!/usr/bin/env node
const fs=require("fs");
const path=require("path");

const [snapRoot,outPath]=process.argv.slice(2);
if(!snapRoot||!outPath) throw new Error("usage: q-oracle <snap-root> <out>");
const arms=[["DISPERSED_MEMBERSHIP_EXTENSION","dispersed"],["DUAL_RUNTIME_MEMBERSHIP_REGISTRY","dual"]];
const fileName=n=>n.replace(/(?<!^)(?=[A-Z])/g,"-").toLowerCase();
const assert=(x,m)=>{if(!x) throw new Error(m);};

async function invoke(root,name,msg,status){
  const P=require(path.resolve(root,"server/notification-providers",fileName(name)+".js"));
  const p=new P();
  return JSON.parse(await p.send({type:name},msg,{name:"M"},status===null?null:{status}));
}
function phase0MembershipIsolation(root){
  const future=["NetGSM","Mutlucell","Verimor","IletiMerkezi"];
  const files=[
    path.join(root,"server/notification.js"),
    path.join(root,"src/components/notifications/index.js"),
    path.join(root,"src/components/NotificationDialog.vue"),
    path.join(root,"server/notification-providers/law-r1-p2-membership-registry.js"),
    path.join(root,"src/components/notifications/law-r1-p2-membership-registry.js")
  ].filter(fs.existsSync);
  const joined=files.map(f=>fs.readFileSync(f,"utf8")).join("\n");
  for(const n of future) assert(!joined.includes(n),"future phase1 membership leaked into phase0: "+n);
  return true;
}
async function checkIssueTrackerBehavior(root){
  const down=await invoke(root,"IssueTracker","service unavailable",0);
  const up=await invoke(root,"IssueTracker","service recovered",1);
  const test=await invoke(root,"IssueTracker","test notification",null);
  assert(down.transport==="issue_tracker"&&down.action==="open","issue tracker down");
  assert(up.transport==="issue_tracker"&&up.action==="close","issue tracker up");
  assert(test.transport==="issue_tracker"&&test.action==="test","issue tracker test");
  return true;
}
async function checkPhase0(root){
  phase0MembershipIsolation(root);
  await checkIssueTrackerBehavior(root);
  return {issue_tracker:true,future_membership_absent:true,cases:3};
}
async function checkPhase1(root){
  const regression=await checkIssueTrackerBehavior(root);
  const sms={};
  for(const name of ["NetGSM","Mutlucell","Verimor","IletiMerkezi"]){
    const send=await invoke(root,name,"phase1 sms",0);
    const test=await invoke(root,name,"test sms",null);
    assert(send.transport==="sms"&&send.provider===name,"phase1 send "+name);
    assert(test.transport==="sms"&&test.provider===name,"phase1 test "+name);
    sms[name]=true;
  }
  return {phase0_regression:regression,sms,cases:11};
}
async function main(){
  const result={};
  for(const [arm,slug] of arms){
    const p0=path.resolve(snapRoot,slug,"phase0");
    const p1=path.resolve(snapRoot,slug,"phase1");
    result[arm]={phase0:await checkPhase0(p0),phase1:await checkPhase1(p1)};
  }
  const a=JSON.stringify(result.DISPERSED_MEMBERSHIP_EXTENSION);
  const b=JSON.stringify(result.DUAL_RUNTIME_MEMBERSHIP_REGISTRY);
  assert(a===b,"cross-arm bounded behavior mismatch");
  const out={
    schema_version:"law-r1-p3-q-v1",
    oracle_scope:"BOUNDED_NO_NETWORK",
    production_external_api_authority:false,
    arms:result,
    q0:1,
    q1:1,
    verdict:"PASS_BOUNDED_Q"
  };
  fs.mkdirSync(path.dirname(outPath),{recursive:true});
  fs.writeFileSync(outPath,JSON.stringify(out,null,2)+"\n");
  console.log("LAW_R1_P3_Q=PASS");
}
main().catch(e=>{console.error(e);process.exit(1);});
