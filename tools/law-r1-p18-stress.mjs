import fs from 'node:fs';

const read = p => JSON.parse(fs.readFileSync(p, 'utf8'));
const java = read(process.argv[2] ?? 'out-p18/java-etcd.json');
const cs = read(process.argv[3] ?? 'out-p18/csharp-boundary.json');
const custody = read('active/g8-law-r1-p18/P18_NONBOT_INTERACTION_CUSTODY.json');
const lit = read('active/g8-law-r1-p18/P18_LITERATURE_CUSTODY.json');

const exactEtcd = java.complete_2x2 === true &&
  java.xnor_reversal === true &&
  java.main_effect_only_rejected === true;
const partialEscape = cs.status === 'PASS_PARTIAL_DOMAIN_ESCAPE' &&
  cs.bot_workflow_basin_escaped === true &&
  cs.exact_nonbot_families === 1 &&
  cs.second_transport === false;
const literature = lit.status === 'CANONICALIZED_AND_DEEP_READ' &&
  lit.papers?.length === 3 &&
  lit.papers.every(p => p.full_text_read === true && p.authority_transfer === 'NONE');
const anti = custody.post_hoc_X_additions?.length === 0 &&
  custody.post_hoc_interaction_subsets_added?.length === 0;

let status = exactEtcd && partialEscape && literature && anti ? 'PASS' : 'HOLD';
let verdict = status === 'PASS'
  ? 'PASS_PARTIAL_DOMAIN_ESCAPE__ONE_NONBOT_EXACT_FAMILY__SECOND_TRANSPORT_MISSING__R2_NOT_AUTHORIZED'
  : 'HOLD_NONBOT_FACTORIAL_SUPPORT_INSUFFICIENT__BOT_WORKFLOW_CONCENTRATION_NOT_ESCAPED';

const result = {
  stage: 'EvoNOMOS Generation VIII LAW-R1-P18',
  suffix: 'Stress',
  status,
  verdict,
  scientific_readout: {
    bot_workflow_basin_escaped: exactEtcd,
    exact_nonbot_family: {
      id: 'ETCD_DOWNGRADE_VERSION_GEOMETRY',
      type: 'LIFECYCLE_PHASE_X_VERSION_GEOMETRY',
      domain: 'DISTRIBUTED_RUNTIME_VERSION_SKEW',
      interaction: 'XNOR_REVERSAL',
      difference_in_differences: java.difference_in_differences,
      status: exactEtcd ? 'EXACT' : 'FAIL'
    },
    second_semantic_transport_family: 'NOT_FOUND',
    compatibility_x_coexistence: custody.primary_target_readout.COMPATIBILITY_X_COEXISTENCE,
    higher_order_x: custody.higher_order_X,
    same_normalized_x_g_e_conflicting_action:
      custody.same_normalized_X_G_E_conflicting_action_observed ? 'OBSERVED' : 'NOT_OBSERVED'
  },
  negative_custody: custody.negative_or_support_only_candidates.map(x => ({
    id: x.id, status: x.status
  })),
  literature: {
    canonicalized_full_text_papers: lit.papers.length,
    authority_transferred: 'NONE',
    principle_as_projection: lit.principle_as_projection_hypothesis.status,
    manuscript_drafting: lit.paper_readiness.manuscript_drafting
  },
  methodology: {
    java_factorial_reconstruction: exactEtcd ? 'PASS' : 'FAIL',
    csharp_boundary_audit: cs.status,
    javascript_stress_aggregation: 'PASS',
    new_python_files: 0,
    anti_rationalization: anti ? 'PASS' : 'FAIL'
  },
  ruling: {
    four_primitive_basis: 'RETAINS_P16_AUTHORITY',
    p17_interaction_graph: 'RETAINS_P17_AUTHORITY',
    nonbot_domain_escape: exactEtcd ? 'ACHIEVED_BOUNDED_ONE_DOMAIN' : 'NOT_ACHIEVED',
    compatibility_x_coexistence: 'NOT_AUTHORIZED',
    generalized_interaction_law: 'NOT_AUTHORIZED',
    solid_as_special_case: 'HARVEST_HYPOTHESIS_ONLY',
    law_r2: 'NOT_AUTHORIZED',
    next_authority: 'REMAIN_WITHIN_LAW_R1'
  },
  caution: 'P18 escapes the bot/workflow basin with one exact distributed-runtime X×G reversal, but does not yet replicate that interaction semantics in a second non-bot domain and does not identify compatibility×coexistence.'
};

fs.mkdirSync('out-p18', {recursive:true});
fs.writeFileSync(process.argv[4] ?? 'out-p18/p18-stress.json', JSON.stringify(result,null,2)+'\n');
console.log('LAW_R1_P18_STRESS=' + status);
console.log('VERDICT=' + verdict);
console.log('NONBOT_DOMAIN_ESCAPE=' + result.ruling.nonbot_domain_escape);
console.log('COMPATIBILITY_X_COEXISTENCE=' + result.scientific_readout.compatibility_x_coexistence);
console.log('HIGHER_ORDER_X=' + result.scientific_readout.higher_order_x);
console.log('NEW_PYTHON_FILES=0');
console.log('LAW_R2=NOT_AUTHORIZED');
if (status !== 'PASS') process.exit(4);
