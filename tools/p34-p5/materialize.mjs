#!/usr/bin/env node
// Builds separate source worlds for the pre-registered P34-P5 Go experiment.
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
const root=process.argv[2]||"restic";
const original=fs.readFileSync("tools/p34-p4/pair.go","utf8");
const tests=fs.readFileSync("tools/p34-p4/pair_test.go","utf8");
const newTests=fs.readFileSync("tools/p34-p5/keyfile_requirement_test.go","utf8");
const anchors={
direct:"func (d *direct) Save(c context.Context,h restic.Handle,r restic.RewindReader)error{return d.state.save(c,h,r)}",
composed:"func (x *writeUnit) save(c context.Context,h restic.Handle,r restic.RewindReader)error{return x.state.save(c,h,r)}"
};
const hash=s=>crypto.createHash("sha256").update(s).digest("hex");
function patch(s,arm){
 const old=anchors[arm];
 if(s.split(old).length!==2)throw Error("immutable P4 method anchor drift");
 const check='if h.Type==restic.KeyFile && r.Length()>8 {return errors.New("P34_KEYFILE_LIMIT_EXCEEDED")}';
 const replacement=old.replace("error{return","error{\n "+check+"\n return").replace(/\)}$/,")\n}");
 return s.replace(old,replacement);
}
const measurements={schema:"P34_P5_PAIRED_SOURCE_PATCHES_V1",baseline_sha256:hash(original),variants:{}};
for(const arm of ["baseline","direct","composed"]){
 const dir=path.join(root,"internal/backend","p34p5"+arm);
 const src=arm==="baseline"?original:patch(original,arm);
 fs.mkdirSync(dir,{recursive:true});
 fs.writeFileSync(path.join(dir,"pair.go"),src);
 fs.writeFileSync(path.join(dir,"pair_test.go"),tests);
 fs.writeFileSync(path.join(dir,"keyfile_requirement_test.go"),newTests);
 const touched=arm==="baseline"?0:1;
 measurements.variants[arm]={file_count:touched,method_count:touched,
  added_lines:touched*4,removed_lines:touched,
  source_method:arm==="direct"?"direct.Save":arm==="composed"?"writeUnit.save":"none",
  sha256:hash(src)};
}
fs.mkdirSync("out",{recursive:true});
fs.writeFileSync("out/p34-p5-source-diffs.json",JSON.stringify(measurements,null,2)+"\n");
console.log("P34_P5_GENERATED_TWO_DISTINCT_GO_SOURCE_WORLDS_AND_BASELINE");
