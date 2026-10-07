import fs from "node:fs";

const [obsPath,outPath] = process.argv.slice(2);
if (!obsPath || !outPath) throw new Error("usage: node court.mjs observed.json court.json");
const obs = JSON.parse(fs.readFileSync(obsPath,"utf8"));
const expected = [-1,-1,0];
const exact = JSON.stringify(obs.kernel) === JSON.stringify(expected);
const pass = exact &&
  obs.label === "X1_CROSS_COUPLED_BYPASS_OBSTRUCTION" &&
  obs.baseline?.q===1 && obs.baseline?.g===1 && obs.baseline?.y===1 &&
  obs.drop?.q===0 && obs.drop?.g===0 && obs.drop?.y===1 &&
  obs.digest_equal === true &&
  obs.upstream_tests?.baseline === "PASS" &&
  obs.upstream_tests?.no_avx2 === "PASS" &&
  obs.direct_y_intervention === false;

const verdict = pass
  ? "PASS_X1_EXACT_OBSTRUCTION__STRONG_SCALAR_NECESSITY_FAILS_AT_ACTION_GRAIN__N0_N1_CONDITIONAL_EXHAUSTIVENESS_PRESERVED__LAW_R2_NOT_AUTHORIZED"
  : "FAIL_OR_HOLD_P28_X1_CANDIDATE";

const out = {
  stage:"EvoNOMOS Generation VIII LAW-R1-P28",
  pass,
  verdict,
  observed_kernel:obs.kernel,
  classification: pass ? "ONTOLOGY_OBSTRUCTION_NOT_THIRD_STRONG_SCALAR_FAMILY" : "UNRESOLVED",
  authorized: pass ? [
    "BLAKE3 exact hosted candidate realizes X1=(-1,-1,0) under the frozen P28 measurement.",
    "Strong scalar q-necessity fails for this action grain because y persists while q and g drop.",
    "The conditional theorem that N0/N1 exhaust strong scalar mediation remains mathematically valid."
  ] : [],
  not_authorized:[
    "exactly three universal architecture families",
    "LAW-R2",
    "macro design law",
    "SOLID derivation",
    "manuscript readiness",
    "universal latent-state theorem"
  ]
};
fs.writeFileSync(outPath, JSON.stringify(out,null,2)+"\n");
console.log("P28_COURT="+(pass?"PASS":"FAIL"));
console.log("P28_VERDICT="+verdict);
if (!pass) process.exit(1);
