# Paper B reproducibility notes

Run these commands from the Paper B directory with Python 3.10 or later. The three shape fixtures and two library fixtures execute local examples. The two archive audits read JSON and JSONL without executing archive sources.

```sh
python3 audit_are_we_solid.py /path/to/AreWeSOLID.zip
python3 audit_are_we_solid_alignment.py /path/to/AreWeSOLID.zip
python3 meyer_judgment_pair.py
python3 replay_meyer_disclosure.py
python3 ocp_case.py check
python3 ocp_batch_ownership_case.py
python3 ocp_render_entrypoint_case.py
python3 render_paper_b_figure.py /path/to/output
```

The figure command additionally uses Matplotlib. It generates the comparison of requests and placement rules from the shape and batch executions. The separate entry-point experiment belongs in its own table.

## Archive inputs and reference sources

The inspected archive's SHA-256 is `d2cfbe50dd12d189c0ee2b561a842757fa7483251df9025b602c498b753f0353`. The OCP inventory contains 48 reference pairs, 768 saved records, and 24 exact distinct templates after masking the submitted code. The alignment audit counts exact matches with both sides of the reference pairs, with and without trimming outer whitespace. Both comparisons yielded zero. This test establishes textual matching results in this archive.

The saved Python prompt is line 13 (record ID 12) of `AreWeSOLID/dataset/completions/test/ocp--codellama70b-temp0-latest--example/output_test.jsonl`. The getter example is one-based pair 37 of `AreWeSOLID/dataset/groundtruth/ocp_violations.json`.

## Fixed patch when requirements are only partly known

Read across for the book-prefix obligation. The other legacy obligations are fixed. A determinate verdict requires unanimity across compatible full specifications; disagreement yields defer.

| Disclosed demand | Contract excludes book prefix | Contract includes book prefix | Contract unspecified |
| --- | --- | --- | --- |
| Technical reports | Accept | Reject | Defer |
| Technical reports and errata | Reject | Reject | Reject |
| Unspecified | Defer | Reject | Defer |

## Optional bracketed rendering

| Delivered through | Old file edits, operation layout | Old file edits, shape layout | Added files in each layout |
| --- | ---: | ---: | ---: |
| Additional entry | 0 | 0 | 1 |
| Original entry on baseline | 1 | 2 | 0 |
| Original entry on hook-equipped baseline | 0 | 0 | 1 |

The feature candidates succeeded and preserved the old observed rendering behavior. Two sets of negative controls, each run on both layouts, checked that adding an adapter alone left the option unsupported on the original route and that a hook without the plugin could not produce decorated output. The hook is pre-existing relative to the third-row comparison. Its introduction is outside that row's edit count. These cases measure the listed implementations under specified routing. They leave independently authored requirements, other representations and real maintenance effort open.

Prediction: https://github.com/WhoSia/EvoNOMOS/commit/76fa9222a7149b7c98a6315375834f2bd909fe0e
Execution: https://github.com/WhoSia/EvoNOMOS/commit/0ede7b241c8f9f50436be9703561bb9e7cc9fb8b
