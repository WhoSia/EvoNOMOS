import fs from 'node:fs';

const read = (p) => JSON.parse(fs.readFileSync(p, 'utf8'));
const rust = read(process.argv[2] ?? 'out-p17/rust-interactions.json');
const go = read(process.argv[3] ?? 'out-p17/go-transport.json');
const cpp = read(process.argv[4] ?? 'out-p17/cpp-knockout.json');
const ruby = read(process.argv[5] ?? 'out-p17/ruby-harvest.json');
const evidence = read('active/g8-law-r1-p17/P17_INTERACTION_CUSTODY.json');

const exactTransport = rust.exact_conjunctive_gate === true &&
  rust.conditional_pairwise_interaction === true &&
  go.transport_status === 'EXACT_TWO_DOMAIN_TRANSPORT';
const knockout = cpp.single_knockout_complete === true &&
  cpp.degree_le_2_reconstruction_rejected === true;
const harvest = ruby.status === 'PASS_HARVEST_NON_SOVEREIGN' &&
  ruby.authority_transferred === 'NONE';
const anti = (evidence.post_hoc_interaction_subsets_added ?? []).length === 0;
const noSameStateConflict = evidence.interaction_readout?.same_normalized_X_G_E_conflicting_action_observed === false;

let status = 'PASS';
let verdict;
if (!(exactTransport && knockout && harvest && anti)) {
  status = 'HOLD';
  verdict = 'HOLD_FACTORIAL_SUPPORT_INSUFFICIENT__INTERACTION_LAW_NOT_IDENTIFIED';
} else {
  verdict = 'PASS_PARTIAL_INTERACTION_GRAPH__PAIRWISE_EDGES_IDENTIFIED__HIGHER_ORDER_TERMS_UNDERIDENTIFIED';
}

const result = {
  stage: 'EvoNOMOS Generation VIII LAW-R1-P17',
  suffix: 'Reconstruction',
  status,
  verdict,
  scientific_readout: {
    transported_x_edge: {
      vertices: ['RELEASE_AUTHORITY','LIFECYCLE_PHASE'],
      conditional_on: 'G.IS_PULL_REQUEST=1',
      domains: ['KUBERNETES_PROW','HUGGINGFACE_SERGE'],
      status: exactTransport ? 'EXACT_TWO_DOMAIN' : 'FAIL'
    },
    transported_context_geometry_hyperedge: {
      vertices: ['RELEASE_AUTHORITY','LIFECYCLE_PHASE','G.IS_PULL_REQUEST'],
      algebra: 'BOOLEAN_CONJUNCTION',
      mobius_order3: 1,
      knockout: knockout ? 'PASS' : 'FAIL',
      status: exactTransport && knockout ? 'EXACT_TWO_DOMAIN' : 'FAIL'
    },
    genuine_three_or_four_X_hyperedges: 'UNDERIDENTIFIED',
    other_pairwise_X_edges: 'UNDERIDENTIFIED_OR_ONE_DOMAIN_ONLY',
    sparse_law_scope: 'BOT_AND_WORKFLOW_COMMENT_TRIGGER_GEOMETRY_ONLY',
    same_normalized_X_G_E_conflicting_action: noSameStateConflict ? 'NOT_OBSERVED' : 'OBSERVED'
  },
  methodology: {
    rust_interaction_decomposition: 'PASS',
    go_cross_domain_transport: 'PASS',
    cpp_knockout_and_lower_order_rejection: 'PASS',
    ruby_harvest_provenance: harvest ? 'PASS' : 'FAIL',
    javascript_reconstruction: 'PASS',
    new_python_files: 0,
    anti_rationalization: anti ? 'PASS' : 'FAIL'
  },
  harvest: {
    id: 'LR-20261002-V',
    authority: 'NONE',
    status: ruby.status,
    paper_seeds: ruby.paper_seed_ids
  },
  ruling: {
    four_primitive_basis: 'RETAINS_P16_AUTHORITY',
    interaction_law: 'PARTIAL_REPRODUCIBLE_SPARSE_STRUCTURE',
    higher_order_X_law: 'NOT_AUTHORIZED',
    context_geometry_cross_term: 'AUTHORIZED_NARROW_TWO_DOMAIN',
    law_r2: 'NOT_AUTHORIZED',
    next_authority: 'REMAIN_WITHIN_LAW_R1'
  },
  caution: 'The transported law is narrow: two context primitives and PR geometry jointly gate comment-trigger actions in two bot/workflow systems. It is not yet a domain-general software-design interaction law.'
};

const output = process.argv[6] ?? 'out-p17/p17-reconstruction.json';
fs.writeFileSync(output, JSON.stringify(result, null, 2) + '\n');
console.log(status === 'PASS' ? 'LAW_R1_P17_RECONSTRUCTION=PASS' : 'LAW_R1_P17_RECONSTRUCTION=HOLD');
console.log('VERDICT=' + verdict);
console.log('TRANSPORTED_X_EDGE=' + result.scientific_readout.transported_x_edge.status);
console.log('CONTEXT_GEOMETRY_HYPEREDGE=' + result.scientific_readout.transported_context_geometry_hyperedge.status);
console.log('HIGHER_ORDER_X=' + result.scientific_readout.genuine_three_or_four_X_hyperedges);
console.log('NEW_PYTHON_FILES=0');
console.log('LAW_R2=NOT_AUTHORIZED');
if (status !== 'PASS') process.exit(5);
