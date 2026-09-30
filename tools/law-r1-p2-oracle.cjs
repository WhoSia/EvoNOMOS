#!/usr/bin/env node
const fs=require("fs");
const path=require("path");

const [dispRoot,dualRoot,outPath]=process.argv.slice(2);
if(!dispRoot||!dualRoot||!outPath) throw new Error("usage: oracle <dispersed> <dual> <receipt>");

const providers=["IssueTracker","NetGSM","Mutlucell","Verimor","IletiMerkezi"];
const fileName=n=>n.replace(/(?<!^)(?=[A-Z])/g,"-").toLowerCase();
const read=(root,rel)=>fs.readFileSync(path.join(root,rel),"utf8");
const assert=(cond,msg)=>{if(!cond) throw new Error(msg);};

async function behavior(root,name,phase){
  const P=require(path.resolve(root,"server/notification-providers",fileName(name)+".js"));
  const p=new P();
  const cases=phase===0
    ? [["down","service unavailable",0],["up","service recovered",1],["test","test notification",null]]
    : [["send","phase1 sms",0],["test","test sms",null]];
  const out=[];
  for(const [label,msg,status] of cases){
    const hb=status===null?null:{status};
    out.push([label,await p.send({type:name},msg,{name:"M"},hb)]);
  }
  return out;
}

async function main(){
  const replay={};
  for(const name of providers){
    const phase=name==="IssueTracker"?0:1;
    const a=await behavior(dispRoot,name,phase);
    const b=await behavior(dualRoot,name,phase);
    assert(JSON.stringify(a)===JSON.stringify(b),"behavior mismatch "+name);
    replay[name]={phase,cases:a};
  }

  const ds=read(dispRoot,"server/notification.js");
  const di=read(dispRoot,"src/components/notifications/index.js");
  const dd=read(dispRoot,"src/components/NotificationDialog.vue");
  for(const n of providers){
    assert(ds.includes(`const ${n} = require`),"dispersed backend import missing "+n);
    assert(ds.includes(`new ${n}()`),"dispersed backend list missing "+n);
    assert(di.includes(`import ${n} from`),"dispersed frontend import missing "+n);
    assert(di.includes(`${n}: ${n}`),"dispersed form map missing "+n);
    assert(dd.includes(`${n}:`),"dispersed category membership missing "+n);
  }

  const rb=read(dualRoot,"server/notification-providers/law-r1-p2-membership-registry.js");
  const rf=read(dualRoot,"src/components/notifications/law-r1-p2-membership-registry.js");
  const rs=read(dualRoot,"server/notification.js");
  const ri=read(dualRoot,"src/components/notifications/index.js");
  const rd=read(dualRoot,"src/components/NotificationDialog.vue");
  for(const n of providers){
    assert(rb.includes(n),"dual backend registry missing "+n);
    assert(rf.includes(n),"dual frontend registry missing "+n);
    assert(!rs.includes(`const ${n} = require`) && !rs.includes(`new ${n}()`),"dual leaked membership to server integration "+n);
    assert(!ri.includes(`import ${n} from`) && !ri.includes(`${n}: ${n}`),"dual leaked membership to frontend integration "+n);
    assert(!rd.includes(`${n}:`),"dual leaked membership to dialog "+n);
  }

  const receipt={
    schema_version:"law-r1-p2-comparability-v1",
    source_commit:"398482d590daaac0d44e288c9be3bc6f6667f8b8",
    phase0:{demand_issue:7316,providers:["IssueTracker"],behavior_equivalent:true,ui_discoverable_both:true},
    phase1:{demand_issue:7559,providers:["NetGSM","Mutlucell","Verimor","IletiMerkezi"],behavior_equivalent:true,ui_discoverable_both:true},
    membership_authority:{
      DISPERSED_MEMBERSHIP_EXTENSION:{semantic_sites:5},
      DUAL_RUNTIME_MEMBERSHIP_REGISTRY:{semantic_registries:2}
    },
    replay,
    verdict:"PASS_PRE_REVEAL_COMPARABILITY",
    forbidden_not_computed:["S","L","C","A","Q","LOC","churn","scalar winner","architecture recommendation","CIL empirical update"]
  };
  fs.mkdirSync(path.dirname(outPath),{recursive:true});
  fs.writeFileSync(outPath,JSON.stringify(receipt,null,2)+"\n");
  console.log("LAW_R1_P2_PRE_REVEAL_COMPARABILITY=PASS");
}

main().catch(e=>{console.error(e);process.exit(1);});
