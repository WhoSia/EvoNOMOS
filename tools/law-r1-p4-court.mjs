#!/usr/bin/env node
import fs from "node:fs";
const [wpath,ipath,outpath]=process.argv.slice(2);
if(!wpath||!ipath||!outpath) throw new Error("usage");
const w=JSON.parse(fs.readFileSync(wpath,"utf8"));
const i=JSON.parse(fs.readFileSync(ipath,"utf8"));
const fail=x=>{throw new Error("P4_HOLD "+x);};
if(w.verdict!=="PASS_WORLD_CONTACT_CENSUS") fail("world");
if(i.verdict!=="PASS_REAL_IMPLEMENTATION_LOCAL_HTTP_ORACLE") fail("indigo");
if(!w.uptime_kuma.all_five_site_path) fail("uptime");
if(!w.home_assistant.all_abstain) fail("ha");
const out={
 stage:"EvoNOMOS Generation VIII LAW-R1-P4",
 axis1:{
  status:"UNDERDEVELOPED_BUT_WORLD_CONTACTED",
  next:"DIRECT_BLINDED_PRINCIPLE_PRIOR_VS_EVIDENCE_CONDITIONED_RIVAL_CHOICE",
  llm_witness:w.uptime_kuma.llm_mediated_witness
 },
 axis2:{
  status:"ADVANCED",
  positive:{
   real_merge_count:w.uptime_kuma.merge_census.length,
   five_site_recurrence:true,
   real_implementation:"Indigo",
   oracle:"LOCAL_HTTP"
  },
  abstention:{
   independent_worlds:w.home_assistant.worlds.length,
   boundary:w.home_assistant.support_domain_boundary,
   action:"ABSTAIN"
  }
 },
 cil:{
  prior:"CIL_C1_SUPPORT_EXTENDED__BOUNDARY_SCOPE_REFINED__TWO_REAL_DEMANDS__BOUNDED_NO_NETWORK",
  authority:"CIL_C1_REAL_IMPLEMENTATION_TRANSPORT__FIVE_REAL_MERGES__LOCAL_HTTP_ORACLE__ABSTENTION_BOUNDARY_ESTABLISHED",
  production_external_api_equivalence:"UNESTABLISHED",
  universal_rule:"WITHHELD"
 },
 cbl_change:"NONE",
 scalarization:false,
 winner:null,
 solid_verdict:"WITHHELD"
};
fs.mkdirSync(outpath.includes("/")?outpath.slice(0,outpath.lastIndexOf("/")):".",{recursive:true});
fs.writeFileSync(outpath,JSON.stringify(out,null,2)+"\n");
console.log("LAW_R1_P4_COURT=PASS");
console.log(JSON.stringify({axis1:out.axis1.status,axis2:out.axis2.status,cil:out.cil.authority,abstain:out.axis2.abstention.action,winner:null}));
