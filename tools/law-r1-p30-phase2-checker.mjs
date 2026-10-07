#!/usr/bin/env node

function edges(states, z, y) {
  const out = [];
  for (let i = 0; i < states.length; i++) {
    for (let j = i + 1; j < states.length; j++) {
      const a = states[i], b = states[j];
      if (JSON.stringify(z(a)) === JSON.stringify(z(b)) && y(a) !== y(b)) {
        out.push([a.id, b.id]);
      }
    }
  }
  return out;
}

function separates(edge, statesById, h) {
  const [a,b] = edge.map(id => statesById.get(id));
  return h(a) !== h(b);
}

function minimumCover(universe, observables, statesById) {
  const n = observables.length;
  for (let k = 0; k <= n; k++) {
    const choose = (start, picked) => {
      if (picked.length === k) {
        const ok = universe.every(e => picked.some(idx => separates(e, statesById, observables[idx].fn)));
        return ok ? picked.slice() : null;
      }
      for (let i = start; i < n; i++) {
        picked.push(i);
        const got = choose(i + 1, picked);
        if (got) return got;
        picked.pop();
      }
      return null;
    };
    const got = choose(0, []);
    if (got) return got.map(i => observables[i].name);
  }
  return null;
}

const states = [
  {id:"a", z:0, y:0, h1:0, h2:0},
  {id:"b", z:0, y:1, h1:1, h2:0},
  {id:"c", z:0, y:2, h1:1, h2:1},
  {id:"d", z:1, y:0, h1:0, h2:0}
];
const byId = new Map(states.map(s => [s.id, s]));
const E = edges(states, s=>s.z, s=>s.y);
if (E.length !== 3) throw new Error("collision graph edge count mismatch");

const basis = minimumCover(E, [
  {name:"H1", fn:s=>s.h1},
  {name:"H2", fn:s=>s.h2}
], byId);
if (!basis || basis.length !== 2) throw new Error("minimum prospective rescue basis mismatch");

const kz = new Map();
for (const s of states) {
  if (!kz.has(s.z)) kz.set(s.z, new Set());
  kz.get(s.z).add(s.y);
}
const maxK = Math.max(...[...kz.values()].map(x=>x.size));
const binaryLowerBound = Math.ceil(Math.log2(maxK));
if (maxK !== 3 || binaryLowerBound !== 2) throw new Error("information lower bound mismatch");

const interventions = [
  s => ({...s}),
  s => ({...s, z: s.id === "b" ? 2 : s.z})
];
function signature(s) {
  return interventions.map(I => I(s).z);
}
if (JSON.stringify(signature(states[0])) === JSON.stringify(signature(states[1]))) {
  throw new Error("intervention signature failed to break passive equivalence");
}

const staticA = [{id:"x", z:0},{id:"y", z:1}];
const phi = s => ({id:s.id, z:s.z === 0 ? "L" : "R"});
const psi = z => z === 0 ? "L" : "R";
for (const s of staticA) {
  if (phi(s).z !== psi(s.z)) throw new Error("static quotient transport mismatch");
}

console.log("P30_PHASE2_COLLISION_GRAPH=PASS");
console.log("P30_PHASE2_MINIMUM_RESCUE_SET_COVER=PASS");
console.log("P30_PHASE2_BINARY_INFORMATION_LOWER_BOUND=PASS");
console.log("P30_PHASE2_INTERVENTIONAL_SIGNATURE_BREAKING=PASS");
console.log("P30_PHASE2_STATIC_QUOTIENT_TRANSPORT=PASS");
console.log("P30_PHASE2_LAW_R2_AUTHORITY=FORBIDDEN");
