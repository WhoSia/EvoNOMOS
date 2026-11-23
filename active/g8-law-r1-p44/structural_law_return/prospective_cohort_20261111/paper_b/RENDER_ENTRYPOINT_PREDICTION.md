# Paper B §6 — Existing rendering entry points

This prospective comparison starts from the operation-file and shape-file baselines in `ocp_case.py`. It asks whether an additive adapter can deliver a feature when an old client must use its original rendering import. The independently authored requirement mentioned in the manuscript is still pending. This fixture is author-designed.

## Requirement and cases

Keep legacy calls returning `circle` and `square`. Add opt-in bracketed rendering, retaining the operation-layout error on an unknown kind and leaving the default unchanged if the option is used on a previous call.

- **Additional entry permitted.** A resolver can use an added module; `render.py` or both shape files retain their legacy bytes.
- **Original entry required.** A client calls the originally imported function with keyword `bracketed=True`. Each call starts in a fresh process with the fixture at the ordinary local import path. There is no installation hook, bootstrap or rebinding. The supported original call entries are `render.render(kind)` or `circle.render()` and `square.render()`. Test the exact additions from the first case again as negative controls.
- **Original entry with a pre-existing extension hook.** In a separate baseline, every original renderer may resolve an extension function from an optional module when explicitly requested. Test the same fixed client against an additive plugin. Record the hook as a prerequisite in the initial source, before comparing candidate changes.

| Delivered through | Existing files edited, operation layout | Existing files edited, shape layout |
| --- | ---: | ---: |
| Additional entry | 0 | 0 |
| Original entry on the original baseline | 1 | 2 |
| Original entry on the hook-equipped baseline | 0 | 0 |

The additive candidates from the first row should preserve legacy behavior but fail the opt-in test through the original entries. Hook-equipped candidates should accept it through original entries. Exercise both shapes, repeated default after opt-in, and the known unsupported-kind behavior of the operation layout. Preserve old tests as regressions. These are predictions for named candidates and explicit environments. Source edits do not measure maintenance effort. The pre-existing hook is part of a different baseline.
