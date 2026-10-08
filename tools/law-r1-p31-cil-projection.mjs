#!/usr/bin/env node
// EvoNOMOS P31: a narrow executable CIL-C1 lifecycle sensitivity demonstration.
// This is NOT a new effect estimate, causal law, or architecture recommender.
import {readFileSync} from "node:fs";
import assert from "node:assert/strict";
const receiptPath = new URL("../active/g8-law-r1-p3/P3_TERMINAL_SEAL.json", import.meta.url);
const evidence = JSON.parse(readFileSync(receiptPath, "utf8"));
const phases = evidence.dual_minus_disperse;
const birth = phases.phase0;
const repeat1 = phases.phase1;

function project(futureRepeatCount) {
  if (!Number.isInteger(futureRepeatCount) || futureRepeatCount < 0) {
    throw new Error("futureRepeatCount must be a nonnegative integer");
  }
  const lOnlyCumulativeScenario = birth.L + futureRepeatCount * repeat1.L;
  const lOnlyThreshold =
    repeat1.L < 0 ? Math.ceil(birth.L / (-repeat1.L)) : null;
  return {
    source_stage: evidence.stage,
    experiment: "Uptime Kuma #7316 then #7559",
    observed_demand_count: 2,
    actually_observed_repeat_count: 1,
    forecast_repeat_count: futureRepeatCount,
    measured_birth_vector: birth,
    measured_first_repeat_vector: repeat1,
    coordinate_L_only: {
      scenario_cumulative_difference: lOnlyCumulativeScenario,
      first_hypothetical_break_even_repeat_count: lOnlyThreshold,
      assumed_future_per_repeat_L_difference: repeat1.L,
      repeated_saving_is_empirically_confirmed_beyond_first_repeat: false,
      at_or_below_zero: lOnlyCumulativeScenario <= 0
    },
    coordinate_A_separate: {
      measured_birth_tax: birth.A,
      future_repeat_A: "UNMEASURED (first repeat had A=0)",
      architecture_overhead_recovered: "NOT_ESTABLISHED"
    },
    coordinate_S_separate: {
      birth_difference: birth.S,
      first_repeat_difference: repeat1.S,
      future_replication: "UNVERIFIED"
    },
    correctness_domain: "BOUNDED_NO_NETWORK_ONLY",
    advice: "ABSTAIN_NO_OVERALL_ARCHITECTURE_WINNER",
    theory_status: "ILLUSTRATIVE_CONDITIONAL_ACCOUNTING_NOT_SOLID_DERIVATION"
  };
}

function test() {
  assert.equal(birth.L, 14);
  assert.equal(birth.S, -3);
  assert.equal(birth.A, 3);
  assert.equal(repeat1.L, -5);
  assert.equal(repeat1.S, -3);
  assert.equal(repeat1.A, 0);
  for (const [n,expected] of [[0,14],[1,9],[2,4],[3,-1],[4,-6]]) {
    const v = project(n);
    assert.equal(v.coordinate_L_only.scenario_cumulative_difference, expected);
    assert.equal(v.coordinate_L_only.first_hypothetical_break_even_repeat_count,3);
    assert.equal(v.advice,"ABSTAIN_NO_OVERALL_ARCHITECTURE_WINNER");
  }
  for (const bad of [-1,1.5,NaN]) assert.throws(()=>project(bad));
  return {tests:"PASS",source:evidence.stage,scope:"arithmetic and claim-ceiling only"};
}

if (process.argv.includes("--self-test")) {
  console.log(JSON.stringify(test(),null,2));
} else {
  const where = process.argv.indexOf("--future-repeat-count");
  const count = where >= 0 ? Number(process.argv[where+1]) : 1;
  console.log(JSON.stringify(project(count),null,2));
}
