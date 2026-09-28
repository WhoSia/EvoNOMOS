#!/usr/bin/env node
import fs from "node:fs";

const fail=(message)=>{throw new Error(message)};
const bool=(o,k)=>{if(typeof o?.[k]!=="boolean")fail(`missing boolean: ${k}`);return o[k]};
const num=(o,k)=>{if(typeof o?.[k]!=="number"||!Number.isFinite(o[k]))fail(`missing number: ${k}`);return o[k]};

export function decideLineage(input){
  if(!input||typeof input!=="object")fail("input must be an object");
  if(input.schema_version!==1)fail("schema_version must be 1");

  const g=input.generation_delta??{};
  const generationAxes=["theory","ontology","data_regime","measurement","court","authority"];
  const changedAxes=generationAxes.filter(k=>bool(g,k));

  const r=input.origin_recovery??{};
  const recoveryChecks={
    founding_explanandum_preserved:bool(r,"founding_explanandum_preserved"),
    real_structural_interventions_resumed:bool(r,"real_structural_interventions_resumed"),
    rival_policy_competition_resumed:bool(r,"rival_policy_competition_resumed"),
    observed_reversal_or_failure_boundary:bool(r,"observed_reversal_or_failure_boundary"),
    design_decision_consequences:bool(r,"design_decision_consequences"),
    independent_world_contacts:num(r,"independent_world_contacts")>=2
  };
  const recoveryComplete=Object.values(recoveryChecks).every(Boolean);

  const d=input.drift_after_recovery??{};
  const methodCapture=bool(d,"method_or_infrastructure_became_primary_object");
  const methodOnlyStages=num(d,"consecutive_method_only_mainline_stages");
  const relapse=methodCapture||methodOnlyStages>=3;

  const activeExperimentOpen=Boolean(input.active_experiment_open);
  const timing=activeExperimentOpen
    ?"AFTER_ACTIVE_EXPERIMENT_TERMINAL"
    :"IMMEDIATE";

  let decision;
  let recommended;
  const rationale=[];

  if(changedAxes.length){
    decision="OPEN_NEW_GENERATION";
    recommended=input.new_generation_label??"Generation IX P0";
    rationale.push(`GENERATION_DELTA:${changedAxes.join(",")}`);
  }else if(!recoveryComplete){
    decision="KEEP_ORIGIN_R1";
    recommended=input.current_lineage??"Generation VIII ORIGIN-R1";
    rationale.push("ORIGIN_RECOVERY_INCOMPLETE");
  }else if(relapse){
    decision="OPEN_ORIGIN_R2";
    recommended=(input.current_generation??"Generation VIII")+" ORIGIN-R2";
    rationale.push(methodCapture?"POST_RECOVERY_METHOD_CAPTURE":"POST_RECOVERY_METHOD_ONLY_STREAK");
  }else{
    decision="GRADUATE_ORIGIN_TO_NEW_LINEAGE";
    recommended=input.graduation_label??((input.current_generation??"Generation VIII")+" LAW-R1");
    rationale.push("ORIGIN_RECOVERY_COMPLETE","NO_POST_RECOVERY_RELAPSE","NO_GENERATION_DELTA");
  }

  return {
    schema_version:1,
    decision,
    transition_timing:timing,
    recommended_lineage:recommended,
    changed_generation_axes:changedAxes,
    origin_recovery_complete:recoveryComplete,
    recovery_checks:recoveryChecks,
    relapse_detected:relapse,
    rationale_codes:rationale,
    invariants:[
      "R2_REQUIRES_A_SECOND_DOCUMENTED_RETURN_EVENT",
      "LINEAGE_LENGTH_ALONE_NEVER_JUSTIFIES_R2",
      "NEW_GENERATION_REQUIRES_THEORY_ONTOLOGY_DATA_MEASUREMENT_COURT_OR_AUTHORITY_DELTA",
      "ACTIVE_EXPERIMENT_MUST_CLOSE_BEFORE_LABEL_TRANSITION"
    ]
  };
}

function selfTest(){
  const base={
    schema_version:1,
    current_generation:"Generation VIII",
    current_lineage:"Generation VIII ORIGIN-R1",
    graduation_label:"Generation VIII LAW-R1",
    active_experiment_open:false,
    generation_delta:{theory:false,ontology:false,data_regime:false,measurement:false,court:false,authority:false},
    origin_recovery:{
      founding_explanandum_preserved:true,
      real_structural_interventions_resumed:true,
      rival_policy_competition_resumed:true,
      observed_reversal_or_failure_boundary:true,
      design_decision_consequences:true,
      independent_world_contacts:3
    },
    drift_after_recovery:{
      method_or_infrastructure_became_primary_object:false,
      consecutive_method_only_mainline_stages:0
    }
  };
  const cases=[
    [base,"GRADUATE_ORIGIN_TO_NEW_LINEAGE"],
    [{...base,origin_recovery:{...base.origin_recovery,independent_world_contacts:1}},"KEEP_ORIGIN_R1"],
    [{...base,drift_after_recovery:{method_or_infrastructure_became_primary_object:true,consecutive_method_only_mainline_stages:1}},"OPEN_ORIGIN_R2"],
    [{...base,generation_delta:{...base.generation_delta,data_regime:true}},"OPEN_NEW_GENERATION"]
  ];
  for(const [input,expected] of cases){
    const got=decideLineage(input).decision;
    if(got!==expected)fail(`self-test failed: expected ${expected}, got ${got}`);
  }
  return {status:"PASS",cases:cases.length};
}

const argv=process.argv.slice(2);
if(argv[0]==="--self-test"){
  console.log(JSON.stringify(selfTest(),null,2));
}else{
  const path=argv[0];
  if(!path)fail("usage: node tools/lineage-decision.mjs <input.json> | --self-test");
  const input=JSON.parse(fs.readFileSync(path,"utf8"));
  console.log(JSON.stringify(decideLineage(input),null,2));
}
