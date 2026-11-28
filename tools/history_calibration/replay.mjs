// Run from any directory with Node 18+; no network required for saved-feature replay.
import {readFileSync} from 'node:fs';
import assert from 'node:assert/strict';
import {evaluate} from './evaluate.mjs';
import {sensitivity} from './sensitivity.mjs';
const read=n=>JSON.parse(readFileSync(new URL(n,import.meta.url),'utf8'));
const sel=read('selection.json'),features=read('source_features.json');
const train=[1,2,3].flatMap(i=>read('train_'+i+'.json'));
const test=[1,2,3].flatMap(i=>read('test_'+i+'.json'));
const audit=[1,2].flatMap(i=>read('ancestry_compare_'+i+'.json'));
const result=evaluate(sel,features,train,test);
assert.deepEqual(result,read('results.json'));
assert.deepEqual(sensitivity(sel,features,train,test,audit,result),read('sensitivity_results.json'));
console.log('PASS: saved-feature ranking and posthoc ancestry sensitivity; no source refetch or confirmatory result.');
