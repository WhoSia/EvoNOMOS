#!/usr/bin/env node

function key(x) {
  return JSON.stringify(x);
}

function factorizationReport(rows) {
  const fibers = new Map();
  for (const row of rows) {
    const z = key(row.Z);
    if (!fibers.has(z)) fibers.set(z, new Map());
    fibers.get(z).set(key(row.Y), (fibers.get(z).get(key(row.Y)) || 0) + 1);
  }
  const collisions = [];
  for (const [z, ys] of fibers.entries()) {
    if (ys.size > 1) collisions.push({ Z: JSON.parse(z), Y_values: [...ys.keys()].map(JSON.parse) });
  }
  return {
    sufficient_on_rows: collisions.length === 0,
    collision_count: collisions.length,
    collisions,
  };
}

function sameFibers(rows, mapA, mapB) {
  for (let i = 0; i < rows.length; i++) {
    for (let j = 0; j < rows.length; j++) {
      if ((key(mapA(rows[i])) === key(mapA(rows[j]))) !==
          (key(mapB(rows[i])) === key(mapB(rows[j])))) return false;
    }
  }
  return true;
}

function structuredGateResidualization(rows, coarse, refined) {
  const coarseReport = factorizationReport(rows.map(r => ({ Z: coarse(r), Y: r.Y })));
  const refinedReport = factorizationReport(rows.map(r => ({ Z: refined(r), Y: r.Y })));
  return {
    apparent_collision: !coarseReport.sufficient_on_rows,
    resolved_by_refinement: !coarseReport.sufficient_on_rows && refinedReport.sufficient_on_rows,
    survives_refinement: !refinedReport.sufficient_on_rows,
  };
}

function minimumSetCover(universe, sets) {
  const U = new Set(universe);
  const names = Object.keys(sets);
  for (let k = 0; k <= names.length; k++) {
    const choose = (start, picked) => {
      if (picked.length === k) {
        const covered = new Set();
        for (const n of picked) for (const x of sets[n]) covered.add(x);
        if ([...U].every(x => covered.has(x))) return picked;
        return null;
      }
      for (let i = start; i < names.length; i++) {
        const out = choose(i + 1, [...picked, names[i]]);
        if (out) return out;
      }
      return null;
    };
    const found = choose(0, []);
    if (found) return found;
  }
  return null;
}

const exactCollision = [
  { Z: { Q:1, R:1, G:[1,1] }, Y:1 },
  { Z: { Q:1, R:1, G:[1,1] }, Y:0 },
];
const c1 = factorizationReport(exactCollision);
if (c1.sufficient_on_rows || c1.collision_count !== 1) throw new Error("collision criterion failed");

const homogeneous = [
  { Z: { Q:1, R:1, G:[1,1] }, Y:1 },
  { Z: { Q:1, R:0, G:[1,1] }, Y:1 },
  { Z: { Q:0, R:0, G:[1,1] }, Y:0 },
];
if (!factorizationReport(homogeneous).sufficient_on_rows) throw new Error("homogeneous fibers failed");

const gateRows = [
  { Q:1, R:1, Gc:1, G:[1,0], Y:0 },
  { Q:1, R:1, Gc:1, G:[1,1], Y:1 },
];
const gr = structuredGateResidualization(
  gateRows,
  r => ({Q:r.Q,R:r.R,G:r.Gc}),
  r => ({Q:r.Q,R:r.R,G:r.G})
);
if (!gr.resolved_by_refinement || gr.survives_refinement) throw new Error("structured-G residualization failed");

const quotientRows = [
  {a:0,b:"x"}, {a:0,b:"x"}, {a:1,b:"y"}, {a:1,b:"y"}
];
if (!sameFibers(quotientRows, r => r.a, r => r.b)) throw new Error("fiber equivalence failed");

const basis = minimumSetCover(
  ["alias|gate","alias|hidden","gate|hidden"],
  {
    I_measure:["alias|gate","alias|hidden"],
    I_gate:["alias|gate","gate|hidden"],
    I_hidden:["alias|hidden","gate|hidden"],
  }
);
if (!basis || basis.length !== 2) throw new Error("minimum separating basis failed");

console.log("P30_FIBER_FACTORIZATION=PASS");
console.log("P30_EXACT_COLLISION_FALSIFIER=PASS");
console.log("P30_STRUCTURED_G_RESIDUALIZATION=PASS");
console.log("P30_QUOTIENT_FIBER_EQUIVALENCE=PASS");
console.log("P30_MINIMUM_SEPARATING_BASIS=2");
console.log("P30_LAW_R2_DIRECT_AUTHORITY=FORBIDDEN");
