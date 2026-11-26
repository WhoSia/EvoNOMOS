# EvoNOMOS LawKit

LawKit is the executable theory/tool layer of EvoNOMOS.

## Quickstart: contract-preserving repair frontier

Python 3.10+; standard library only. From the repository root:

```bash
python lawkit/reference/repair_frontier.py lawkit/fixtures/repair_frontier_example.json feature
python lawkit/reference/test_repair_frontier.py
python lawkit/reference/test_repair_frontier.py --bench
```

The example returns cost 5 for `start`, 3 for `local`, 0 for `done`, and null for `blocked`. The cheaper upstream-owned edit is excluded, as is the unsafe intermediate state. Each finite non-goal result names the next edge by its zero-based input index. Following these edges reaches a goal with the reported total cost.

Input is a JSON object containing:

- `states`: mapping from state names to objects with Boolean `safe` and a list of string `goals`.
- `allowed_owners`: explicit list of owner identifiers allowed to perform edits.
- `edges`: arrays `[source, destination, owner, positive_integer_cost]`.

The solver computes exact costs to a declared goal for every safe starting state in this finite directed graph. It checks distance inequalities and decreasing path witnesses; null means unreachable within this graph, not impossible in the real codebase. An absent goal produces null for all safe states. The model must already encode all relevant history, intermediate safety and permissions. No source parser, inferred authorization, strategic equilibrium or human-effort estimate is implied. The test suite includes an independent Bellman-Ford oracle, invalid-certificate controls, and the recorded P42 finite graph (not a fresh native Chi run).

The benchmark compares repeated forward shortest-path searches with a single reverse multi-source search plus certificate checking. It reports seven interleaved timings per condition, including sparse/absent goals. It is an algorithmic comparison on the same declared graph, not a performance comparison against other architecture tools.

Its purpose is not to encode SOLID, DIP, OCP, ISP, DRY, or another software-design maxim as a commandment. It turns **world evidence + prospectively frozen demands + architecture moderators + lifecycle evidence + authority constraints** into bounded conditional-law statements, falsifiers and abstentions.

## Explore permission trade-offs

Find all nondominated repairs from one safe state when named additional owner permissions are considered hypothetically:

```bash
python lawkit/reference/repair_permissions.py lawkit/fixtures/repair_frontier_example.json start feature --candidate-owner upstream
python lawkit/reference/test_repair_permissions.py
python lawkit/reference/benchmark_permissions.py
```

The example has two options: cost 5 with no additional owner, and cost 1 with hypothetical upstream permission. Each option includes its edge-index path. Permission labels are supplied by the model, not inferred from repository history; this does not grant permission. An empty result means no repair in the declared graph.

The solver prunes labels using set inclusion of required permissions and positive additive path cost. The benchmark includes a cached subset-enumeration baseline and an exponential-output stress case; the solver is not uniformly faster. In the stress case with k independent optional owners, all 2^k permission/cost combinations can be nondominated. Synthetic costs are not engineer hours. Python standard library only.

## Optimize under an additional-owner budget

Find one minimum-cost safe repair rather than enumerate the entire Pareto frontier:

```bash
python lawkit/reference/repair_budget.py lawkit/fixtures/repair_frontier_example.json start feature --candidate-owner upstream --max-additional-owners 1
python lawkit/reference/test_repair_budget.py --bench
```

The example returns cost 1 and edge 2; a budget of zero returns cost 5. A null option denotes no feasible path in the declared model. Repeated edits by the same extra owner consume one budget unit. Ties need not return the same path as another exact solver.

The search uses (state, additional-owner bitset) and an admissible reverse-distance heuristic that relaxes only the owner budget. The number of possible lifted states is at most |V| times the sum of binomial(k,i) for i=0..min(b,k). It can still be exponential. The benchmark compares against lifted Dijkstra and enumeration of maximal allowed-owner subsets, including path witnesses and their validation. Small queries can favor the simpler subset baseline. No claim of inferred repository authorization or measured maintenance labor.

## Product thesis

Traditional design guidance often starts from:

`principle → implementation advice`

LawKit targets:

`exact world → real demand pair → source evidence → moderator geometry → candidate mechanism → prospective intervention → lifecycle evidence → bounded law / reversal / abstention`

That makes it usable during actual development without pretending that a named rule is universally correct.

## Commands and protocol surfaces

```bash
evonomos-law inspect <moderator-envelope.json>
evonomos-law adjudicate <moderator-envelope.json> <lifecycle.json> <authority-firewall.json>
evonomos-law admit-world <world-envelope.json>
```

- `inspect` — pre-outcome mechanism inspection; no design choice.
- `adjudicate` — post-outcome coordinate/reversal classification under an explicit authority ceiling.
- `admit-world` — conjunctive fresh-world admission; no scalar repository score and no design recommendation.
- `project-law` — LAW-R1 prospective moderator-surface compiler; selects rival tests, emits abstention reasons and preserves falsifiers without choosing an architecture.
- `lawkit/measurements/provider_family_lifecycle_v01.py` — exact-Git two-phase provider-family lifecycle measurement over `S/L/C/A/Q`.
- `lawkit/courts/cil_cbl_support_v01.mjs` — support-domain court for CIL-C1 and CBL-C1 with explicit no-winner semantics.

## Source adapters

`lawkit/adapters/` is the developer-facing evidence compiler.

The first adapter, `github_provider_family_v01.mjs`, checks an exact Git checkout against a frozen source-evidence specification. It verifies source identity, architecture authority sites, runtime interface evidence and pre-demand provider absence. The adapter emits evidence; it does not choose an architecture.

The protocol is canonical; implementation language is not.

### Observed-source repair graph (Chi case study)

The Python adapter verifies local snapshot Git blob identities and compiles supplied Boolean observations, declared transitions, and hypothetical path-to-owner mappings into a finite repair graph. It counts added and deleted lines using Python SequenceMatcher (not engineer effort or minimum edit distance). It rejects mixed-owner transitions; split those into separately evidenced intermediate states. Observations are supplied evidence, not independently authenticated by the generic adapter. It is not a whole-program analyzer.

For a reproducible example, obtain the two original context.go files from [pre-merge](https://github.com/go-chi/chi/blob/6adf733e0ebb79ade04909069f6abdc6f53648a8/context.go) and [merged](https://github.com/go-chi/chi/blob/15767233591fd4267ae99d05299fa3807c375cdd/context.go). Save as base.go and merged.go. The isolated Go 1.23+ harness checks both source blobs, compares them with two authored alternatives, runs tests, and produces a manifest and model.json. It uses type shims, not the full upstream Chi module.

```bash
PYTHONPATH=lawkit/adapters python lawkit/adapters/chi_clone/run_chi.py base.go merged.go evidence
PYTHONPATH=lawkit/adapters python lawkit/adapters/chi_clone/test_observed_repair.py evidence
python lawkit/reference/repair_budget.py evidence/model.json base public --max-additional-owners 0
python lawkit/reference/repair_budget.py evidence/model.json base full --candidate-owner upstream --max-additional-owners 1
PYTHONPATH=lawkit/adapters python lawkit/adapters/chi_clone/bench_chi.py evidence
```

On Windows PowerShell set `$env:PYTHONPATH='lawkit/adapters'` first instead of the inline assignment. The narrow goal returns line cost 9 with app ownership; the stronger sampled goal returns 27 only with hypothetical upstream ownership. These are bounded retrospective comparisons of a declared candidate set, not a blind prediction, full contract, inferred permission, or real maintenance-cost estimate. The optional benchmark fills only public slices; it does not establish full-capability equivalence.

### Incomplete observation evidence

For the archived R114 Chi case, use the independently recorded SHA-256 of the evidence ZIP:

```bash
python lawkit/reference/observed_bounds.py EvoNOMOS_R114_evidence.zip 852cf2d6115f747a30b329c21dafa054343d06ade8a6fd47c6ae0bcec895e220 base full --candidate-owner upstream --max-additional-owners 1 --hide merged:native_private
python lawkit/reference/test_observed_bounds.py EvoNOMOS_R114_evidence.zip
python lawkit/reference/observation_certificate.py EvoNOMOS_R114_evidence.zip
```

The [R114 evidence archive](https://drive.google.com/file/d/1IasQ0eTXgVDZAprM3Ly1UMpN_mYnWll3/view) is pinned to the SHA above. The checker compares its inventory, file digests, observation logs and declared state predicates/transition endpoints. It does not independently attest execution, recompute source line costs without source files, or establish authenticity from a digest supplied by the archive itself.

The query hides one known observation for a sensitivity experiment, returning optimistic cost 27 and a pessimistic null option (unreachable). For fixed edges, owner budget and positive conjunctive observations, assigning all unknowns true and all unknowns false gives exact extreme costs over independent Boolean completions. Equal costs certify the cost, not necessarily a unique repair path or a real-world contract. The 12-observation fixture has 4,096 masking patterns; the test checks all four goal/budget queries against exhaustive completion extrema. The certificate script is deliberately fixture-specific and exponential; it identifies retrospective sufficient subsets, not a prospective optimal testing strategy.

## Current candidate laws

- **CIL-C1 — Conditional Inversion / Membership-Propagation Law Candidate**
- **CBL-C1 — Capability-Bundle Mismatch Law Candidate**

P11 sharpens the distinction between them: membership-surface propagation (`S`) and handwritten source churn (`L`) can dissociate across worlds, while capability-conformance burden (`C`) can remain independently measurable. LAW-R1-P0 therefore treats `S/L/C/A/Q` non-collapse as constitutional, not cosmetic.

P12 is retained as a terminal non-result. Its full-corequirement CBL-C1 falsifier cell is **unresolved**, and `project-law` explicitly forbids treating that non-result as falsification.

## Development direction

1. source adapters extract auditable world evidence;
2. world-admission protocols reject contaminated or non-discriminating cases;
3. rival constitutions define bounded interventions before treatment bytes;
4. Actions executes exact-world experiments under log firewalls;
5. lifecycle measurement preserves distinct coordinates instead of scalarizing them;
6. support-domain courts update candidate laws without recommending a winner;
7. law families compete, fail, split, mutate or retire.

A better LawKit is an engineering achievement. New scientific authority still requires fresh world contact.
