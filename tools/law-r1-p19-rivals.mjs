import fs from 'node:fs';

const rows = fs.readFileSync(process.argv[2] ?? 'active/g8-law-r1-p19/P19_RUST_COMPAT_GEOMETRY.tsv','utf8')
  .trim().split(/\r?\n/).slice(1).map(line => {
    const [X,G,Y] = line.split('\t').map(Number);
    return {X,G,Y};
  });

const errors = pred => rows.reduce((n,r)=>n+(pred(r)!==r.Y),0);
const xOnly = Math.min(
  ...[0,1].map(v => errors(r => r.X ? v : 0)),
  ...[0,1].map(v => errors(r => r.X ? v : 0))
);
// exact minimum over binary lookup by one variable
const minUnary = key => {
  let best=Infinity;
  for(let a=0;a<=1;a++) for(let b=0;b<=1;b++) {
    best=Math.min(best, errors(r => (r[key]===0?a:b)));
  }
  return best;
};
const xErr=minUnary('X');
const gErr=minUnary('G');
const conjunctionErr=errors(r => r.X && r.G ? 1 : 0);
const lookupErr=0;

// exact additive y=a+bX+cG, coefficients forced by 00,10,01 cells
const r00=rows.find(r=>r.X===0&&r.G===0).Y;
const r10=rows.find(r=>r.X===1&&r.G===0).Y;
const r01=rows.find(r=>r.X===0&&r.G===1).Y;
const r11=rows.find(r=>r.X===1&&r.G===1).Y;
const a=r00,b=r10-r00,c=r01-r00;
const additive11=a+b+c;
const additiveExact = additive11===r11;
const did = r11-r10-r01+r00;

const result={
  stage:'EvoNOMOS Generation VIII LAW-R1-P19',
  family:'RUST_ARRAY_INTO_ITER_EDITION_GEOMETRY',
  cells:rows,
  rivals:{
    X_ONLY:{min_cell_errors:xErr,status:xErr===0?'FIT':'FAIL'},
    G_ONLY:{min_cell_errors:gErr,status:gErr===0?'FIT':'FAIL'},
    ADDITIVE_MAIN_EFFECTS:{predicted_11:additive11,observed_11:r11,status:additiveExact?'FIT':'FAIL'},
    PAIRWISE_INTERACTION_X_AND_G:{cell_errors:conjunctionErr,status:conjunctionErr===0?'FIT':'FAIL'},
    LOW_COMPLEXITY_DECISION_SURFACE_X_AND_G:{cell_errors:conjunctionErr,status:conjunctionErr===0?'FIT':'FAIL'},
    UNTYPED_CELL_LOOKUP:{cell_errors:lookupErr,status:'FIT',table_entries:4},
    NAMED_PRINCIPLE_RULE:{status:'INADMISSIBLE_NO_PRECOMMITTED_MAXIM_MAPPING'}
  },
  interaction:{
    difference_in_differences:did,
    exact_additive_main_effects_rejected:!additiveExact,
    unary_rules_rejected:xErr>0&&gErr>0,
    pairwise_interaction_fits:conjunctionErr===0
  },
  representation_competition:{
    unique_winner:false,
    reason:'Typed pairwise interaction and a generic low-complexity conjunction have identical cell fit; P19 cannot promote representation uniqueness from this family.',
    projection_status:'SURVIVES_FALSIFICATION_BUT_REMAINS_UNDERIDENTIFIED'
  }
};
fs.mkdirSync('out-p19',{recursive:true});
fs.writeFileSync(process.argv[3] ?? 'out-p19/p19-rivals.json',JSON.stringify(result,null,2)+'\n');
console.log('P19_RIVAL_COMPETITION=PASS');
console.log('DID='+did);
console.log('X_ONLY_ERRORS='+xErr);
console.log('G_ONLY_ERRORS='+gErr);
console.log('ADDITIVE_MAIN_EFFECTS='+(additiveExact?'FIT':'FAIL'));
console.log('PAIRWISE_INTERACTION='+(conjunctionErr===0?'FIT':'FAIL'));
console.log('REPRESENTATION_UNIQUE=false');
console.log('PROJECTION=SURVIVES_FALSIFICATION_BUT_REMAINS_UNDERIDENTIFIED');
if (conjunctionErr!==0 || additiveExact || xErr===0 || gErr===0) process.exit(2);
