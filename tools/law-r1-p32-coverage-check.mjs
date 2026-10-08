#!/usr/bin/env node
/**
 * P32 theorem-instance checker, not a new theorem or a software-world experiment.
 * Fixed, demand-independent owner activation with nonnegative additive site costs
 * yields normalized monotone submodular coverage.
 */
import assert from "node:assert/strict";

function coverage(sets, weights, requested) {
  const activated = new Set();
  for (const demand of requested) for (const owner of sets[demand] ?? []) activated.add(owner);
  return [...activated].reduce((total, owner) => total + (weights[owner] ?? 0), 0);
}
function mixed(sets, weights, x = "x", y = "y") {
  return coverage(sets, weights, [x,y]) - coverage(sets, weights, [x]) -
    coverage(sets, weights, [y]) + coverage(sets, weights, []);
}
function overlapCost(sets, weights, x = "x", y = "y") {
  const ay = new Set(sets[y]);
  return sets[x].filter(m => ay.has(m)).reduce((acc, m) => acc + (weights[m] ?? 0), 0);
}
function masks(mask, names) {
  return names.filter((_, i) => (mask & (1 << i)) !== 0);
}
function selfTest() {
  const owners = ["a", "b", "c", "d"];
  const weights = {a:1,b:2,c:3,d:5};
  let tested = 0;
  for (let a = 0; a < 16; a++) for (let b = 0; b < 16; b++) {
    const sets = {x: masks(a, owners), y: masks(b, owners)};
    assert.equal(mixed(sets, weights), -overlapCost(sets, weights));
    assert.ok(mixed(sets, weights) <= 0);
    tested++;
  }
  const p = {x:["a","b"], y:["a","b"]};
  const q = {x:["a","b"], y:["b","c"]};
  const unit = {a:1,b:1,c:1};
  assert.deepEqual([coverage(p,unit,["x"]),coverage(p,unit,["y"])],[2,2]);
  assert.deepEqual([coverage(q,unit,["x"]),coverage(q,unit,["y"])],[2,2]);
  assert.equal(mixed(p,unit),-2);
  assert.equal(mixed(q,unit),-1);
  return {
    status:"PASS",
    exhaustive_mask_pairs:tested,
    under_theorem_assumptions:"mixed interaction exactly equals negative shared-owner weight",
    same_marginal_count_counterexample:{
      "pair_1":-2, "pair_2":-1,
      "B0_marginal_counts":"indistinguishable",
      "B0_plus_overlap":"distinguishable",
      "B2_DRS_or_change_hiding":"plausibly distinguishable; not refuted",
      "H_novelty":"NOT_ESTABLISHED"
    },
    failure_gate:"a positive observed mixed cost rejects fixed additive-owner coverage ONLY IF the measured cost satisfies the theorem's cost definition",
    real_source_or_out_of_sample:"NOT_TESTED",
    scientific_authority:"METHOD_ONLY__LAW_R2_NOT_AUTHORIZED"
  };
}
process.stdout.write(JSON.stringify(selfTest(),null,2)+"\n");
