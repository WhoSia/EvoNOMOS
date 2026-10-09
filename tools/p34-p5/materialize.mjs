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
