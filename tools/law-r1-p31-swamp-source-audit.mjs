#!/usr/bin/env node
// P31: source-only admission verification. No behavioral outcome is inferred.
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import {createHash} from "node:crypto";
import {execFileSync} from "node:child_process";

const root=process.argv[2];
if(!root)throw Error("Usage: node law-r1-p31-swamp-source-audit.mjs <checked-out-repo> [receipt.json]");
const expected="9fb288e10730ad214cc1e4413c7664903ee4830a";
assert.equal(execFileSync("git",["-C",root,"rev-parse","HEAD"],{encoding:"utf8"}).trim(),expected);
const files={
 "db/migrations/00019_applications_autoincrement_soft_delete.sql":"92cbd3ab7d54d9205dd84061ea9addeb50c5c929",
 "db/migrations/00001_initial_schema.sql":"002915c06122273ad3d715df68b7c9a5eb0a3145",
 "store/company_filter.go":"3fc3a6a681d68660297649efcc5ed12d88fc100d",
 "stage/document.go":"069b1b289fd3e6e2a0565b908bca7d5dba15b7c0",
 "db/migrations/00020_document_writes.sql":"d6095616491981059e0439f4230698cc0a7031a1"
};
const sources={};
for(const [file,gitBlob] of Object.entries(files)){
 const bytes=fs.readFileSync(path.join(root,file));
 const blobHeader=Buffer.from("blob "+bytes.length+"\0");
 const actual=createHash("sha1").update(blobHeader).update(bytes).digest("hex");
 assert.equal(actual,gitBlob,"source changed: "+file);
 sources[file]=bytes.toString("utf8");
}
const migration=sources["db/migrations/00019_applications_autoincrement_soft_delete.sql"];
const initial=sources["db/migrations/00001_initial_schema.sql"];
const filter=sources["store/company_filter.go"];
const document=sources["stage/document.go"];
const docWrites=sources["db/migrations/00020_document_writes.sql"];
assert.match(migration,/CREATE TABLE applications_new \([\s\S]*?id\s+INTEGER PRIMARY KEY AUTOINCREMENT/);
assert.match(migration,/CREATE UNIQUE INDEX applications_live_posting_id/);
assert.match(migration,/WHERE deleted_at IS NULL/);
assert.match(migration,/INSERT INTO applications_new[\s\S]*?SELECT id, posting_id/);
const match=initial.match(/CREATE TABLE company_filters \(([\s\S]*?)\n\);/);
assert.ok(match,"company_filters source DDL is missing");
assert.match(match[1],/id\s+INTEGER PRIMARY KEY,/);
assert.doesNotMatch(match[1],/\bAUTOINCREMENT\b/);
const replacement=filter.slice(filter.indexOf("func (s *Store) ReplaceCompanyFilters("));
assert.ok(replacement.length>0);
const deleting=replacement.indexOf("s.DeleteCompanyFilters(");
const creating=replacement.indexOf("s.CreateCompanyFilter(");
assert.ok(deleting>=0&&creating>deleting,"filter replacement ordering changed");
const writer=document.slice(document.indexOf("func (st *Stage) WriteDocument("));
const guard=writer.indexOf("st.application(ctx, applicationID)");
const write=writer.indexOf("st.documents.Write(");
assert.ok(guard>=0 && write>guard,"application existence guard not proven before write");
assert.match(docWrites,/CREATE TABLE document_writes \([\s\S]*?id\s+INTEGER PRIMARY KEY AUTOINCREMENT/);

const output={
 stage:"G8 LAW-R1-P31",
 verdict:"PASS_SOURCE_GROUNDED_SWAMP_CONTEXTUAL_ACTION_RIVALS__BEHAVIORAL_COMPARISON_NOT_EXECUTED",
 upstream_repo:"dklassen/swamp",upstream_commit:expected,
 verified_blob_shas:files,
 source_findings:{
  applications:"AUTOINCREMENT with soft delete and live-only posting uniqueness in migration 00019",
  company_filters:"plain INTEGER PRIMARY KEY in initial schema",
  replacement:"ReplaceCompanyFilters deletes and recreates filters",
  documents:"WriteDocument calls application guard before document writes",
  document_writes:"append-only write events use AUTOINCREMENT"
 },
 not_proven:["global absence of external company_filter references","production migration risk frequency","behavioral superiority of blanket/targeted schema migrations","independence of real demand outcomes"],
 p31_closed:false,law_r2_authorized:false
};
console.log(JSON.stringify(output,null,2));
if(process.argv[3])fs.writeFileSync(process.argv[3],JSON.stringify(output,null,2)+"\n");
