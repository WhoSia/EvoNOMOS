#!/usr/bin/env node
import fs from "node:fs";
import assert from "node:assert/strict";
const [root,out]=process.argv.slice(2);
assert.ok(root&&out,"usage: root output");
const terminal=JSON.parse(fs.readFileSync("lawkit/fixtures/p12-terminal-closure.json"));
const archive=JSON.parse(fs.readFileSync("lawkit/discovery/p12_candidates.json"));
const world=archive.candidates.find(x=>x.id==="RESTIC_OCI_ONEDRIVE");
const six=["save","load","stat","list","remove","delete"];
assert.equal(terminal.terminal_status,"TERMINAL_NONRESULT");
assert.equal(terminal.scientific_firewall.lifecycle_coordinates_opened,false);
assert.equal(terminal.scientific_firewall.onedrive_phase1_opened,false);
assert.deepEqual(world.bundled_capabilities.slice().sort(),six.slice().sort());
assert.deepEqual(world.demand_capabilities.slice().sort(),six.slice().sort());
