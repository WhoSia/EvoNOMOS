#!/usr/bin/env node
import fs from 'node:fs';
import crypto from 'node:crypto';

const [custodyPath, methodsetPath, outPath]=process.argv.slice(2);
if(!custodyPath||!methodsetPath||!outPath) throw new Error('usage: seal <custody.json> <methodset.json> <out.json>');
const custody=JSON.parse(fs.readFileSync(custodyPath,'utf8'));
const methods=JSON.parse(fs.readFileSync(methodsetPath,'utf8'));
const fail=m=>{ console.error('P12_P2_HOLD '+m); process.exit(1); };

if(custody.donor!=='495982232cf1af184eac0a97871ef8161e8708ee') fail('donor');
if(custody.sdk!=='v65.50.0') fail('sdk');
if(custody.neutral_tree_equal!==true) fail('neutral scaffold divergence');
if(custody.oracle_sha_equal!==true) fail('oracle divergence');
if(custody.full_build_oracle!=='PASS'||custody.composed_build_oracle!=='PASS') fail('build/oracle');
if(methods.status!=='PASS'||methods.equal!==true||methods.required_present!==true) fail('methodset');
if(custody.onedrive_opened!==false) fail('OneDrive opened');
if(custody.lifecycle_coordinates_opened!==false) fail('lifecycle coordinates opened');

const canonical={
  stage:'EvoNOMOS Generation VIII ORIGIN-R1-P12-P2',
  status:'PAIR_COMPARABLE__PRE_REVEAL__OUTCOMES_CLOSED',
  donor:custody.donor,
  sdk:custody.sdk,
  neutral_tree_equal:true,
  oracle_sha256:custody.oracle_sha256,
  public_methodset_equal:true,
  mandatory_core:['Save','Load','Stat','List','Remove','Delete'],
  full:{commit:custody.full_commit,tree:custody.full_tree,oracle:'PASS'},
  composed:{commit:custody.composed_commit,tree:custody.composed_tree,oracle:'PASS'},
  onedrive_opened:false,
  lifecycle_coordinates_opened:false,
  winner:null,
  cbl_c1_verdict:null
};
const encoded=JSON.stringify(canonical,null,2)+'\n';
fs.writeFileSync(outPath,encoded);
const digest=crypto.createHash('sha256').update(encoded).digest('hex');
fs.writeFileSync(outPath+'.sha256',digest+'  '+outPath.split('/').pop()+'\n');
console.log('P12_P2_COMPARABILITY=PASS');
console.log('P12_P2_OUTCOMES=CLOSED');
