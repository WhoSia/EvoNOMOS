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
