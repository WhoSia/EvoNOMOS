#!/usr/bin/env node
import fs from "node:fs";

const input = process.argv[2];
const output = process.argv[3];
if (!input) throw new Error("usage: node law-r1-p30-zlib-court.mjs <probe-log> [output-json]");

const raw = fs.readFileSync(input, "utf8");
const kv = {};
for (const line of raw.split(/\r?\n/)) {
  const i = line.indexOf("=");
  if (i > 0) kv[line.slice(0, i)] = line.slice(i + 1);
}
const n = k => Number(kv[k]);

const frozenZExact =
  n("WITH_DICT_Q") === 1 &&
  n("NO_DICT_Q") === 1 &&
  n("WITH_DICT_R") === 1 &&
  n("NO_DICT_R") === 1 &&
  n("WITH_DICT_G_INIT") === 1 &&
  n("NO_DICT_G_INIT") === 1 &&
  n("WITH_DICT_G_INPUT") === 1 &&
  n("NO_DICT_G_INPUT") === 1 &&
  n("WITH_DICT_G_OUTPUT") === 1 &&
  n("NO_DICT_G_OUTPUT") === 1 &&
  n("SAME_Z") === 1;

const hSeparated =
  n("WITH_DICT_H_DICT_LEN") > 0 &&
  n("NO_DICT_H_DICT_LEN") === 0 &&
  n("H_DIFF") === 1;

const ySeparated =
  n("WITH_DICT_Y") === 1 &&
  n("NO_DICT_Y") === 0 &&
  n("Y_DIFF") === 1;

let verdict;
let classification;

if (!frozenZExact) {
  verdict = "PASS_APPARENT_COLLISION_RESOLVED_BY_MEASUREMENT_OR_STRUCTURED_GATE_REFINEMENT__LAW_R2_NOT_AUTHORIZED";
  classification = "NO_EXACT_MATCHED_REPAIRED_STATE";
} else if (!ySeparated) {
  verdict = "HOLD_NO_ADMISSIBLE_STATE_COLLISION_WITNESS";
  classification = "NO_Y_HETEROGENEITY_IN_MATCHED_Z_FIBER";
} else if (!hSeparated) {
  verdict = "PASS_EXACT_REPAIRED_STATE_COLLISION__DETERMINISTIC_SUFFICIENCY_FALSIFIED_AT_FROZEN_GRAIN__LAW_R2_NOT_AUTHORIZED";
  classification = "EXACT_COLLISION_WITHOUT_PREDECLARED_H_RESCUE";
} else {
  verdict = "PASS_SAME_REPAIRED_STATE_DIFFERENT_Y__HIDDEN_COORDINATE_REFINEMENT_REQUIRED__LAW_R2_NOT_AUTHORIZED";
  classification = "EXACT_Z_COLLISION_WITH_PROSPECTIVE_H_DICT_RESCUE";
}

const result = {
  stage: "G8 LAW-R1-P30",
  candidate: "madler/zlib preset dictionary",
  frozen_Z_exact: frozenZExact,
  prospective_H_dict_separates: hSeparated,
  Y_separates: ySeparated,
  measurements: {
    with_dict: {
      Q: n("WITH_DICT_Q"),
      R: n("WITH_DICT_R"),
      G: [n("WITH_DICT_G_INIT"), n("WITH_DICT_G_INPUT"), n("WITH_DICT_G_OUTPUT")],
      H_dict_len: n("WITH_DICT_H_DICT_LEN"),
      rc: n("WITH_DICT_RC"),
      out_len: n("WITH_DICT_OUT_LEN"),
      Y: n("WITH_DICT_Y")
    },
    no_dict: {
      Q: n("NO_DICT_Q"),
      R: n("NO_DICT_R"),
      G: [n("NO_DICT_G_INIT"), n("NO_DICT_G_INPUT"), n("NO_DICT_G_OUTPUT")],
      H_dict_len: n("NO_DICT_H_DICT_LEN"),
      rc: n("NO_DICT_RC"),
      out_len: n("NO_DICT_OUT_LEN"),
      Y: n("NO_DICT_Y")
    },
    compressed_len: n("COMPRESSED_LEN"),
    plain_len: n("PLAIN_LEN")
  },
  classification,
  verdict,
  law_r2_authorized: false,
  claim_ceiling: [
    "exact result applies only to the frozen zlib action grain",
    "H_dict was prospectively admitted before hosted outcome",
    "successful H_dict rescue is state refinement, not persistent refinement failure",
    "LAW-R2, macro law, SOLID derivation, manuscript authority, and universal latent-state impossibility remain unauthorized"
  ]
};

const text = JSON.stringify(result, null, 2) + "\n";
process.stdout.write(text);
if (output) fs.writeFileSync(output, text);

if (verdict.startsWith("HOLD_")) process.exitCode = 3;
