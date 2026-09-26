#!/usr/bin/env node
import fs from 'node:fs';

const p = process.argv[2];
if (!p) {
  console.error('usage: lawkit-verify.mjs <inspection-json>');
  process.exit(1);
}
const x = JSON.parse(fs.readFileSync(p, 'utf8'));
const fail = (m) => { console.error(m); process.exit(1); };

if (x.law_candidate !== 'CIL-C1') fail('wrong law candidate');
if (x.authority !== 'HYPOTHESIS_ONLY_PRE_OUTCOME') fail('authority promotion detected');
if (x.mechanism_channels?.decision_authority !== 'ABSTAIN_PRE_OUTCOME') {
  fail('pre-outcome decision authority must abstain');
}
if (x.mechanism_channels?.future_same_family_demand !== 'UNOBSERVED') {
  fail('future demand must remain unobserved');
}
const forbidden = new Set(x.prohibited_inference ?? []);
for (const required of [
  'SOLID_IS_TRUE',
  'DIP_IS_UNIVERSALLY_BETTER',
  'INVERT_IS_RECOMMENDED_WITHOUT_LIFECYCLE_EVIDENCE',
  'SAME_SIGN_REPLICATION_IS_SUFFICIENT_AUTHORITY',
]) {
  if (!forbidden.has(required)) fail('missing prohibition: ' + required);
}
if ('winner' in x || 'recommended_design' in x || 'score' in x) {
  fail('winner/recommendation/scalar score leaked into LawKit v0.1');
}
console.log('EVONOMOS_LAWKIT_CIL_C1_PREOUTCOME=PASS');
console.log('EVONOMOS_LAWKIT_DECISION_AUTHORITY=ABSTAIN');
