# Paper B — Retrospective transfer probe: CPython assertNoLogs

2026-11-17 KST · Companion case for bilingual manuscript 11. [Main manuscript](https://app.notion.com/p/41bef561cf92811abb50f26b749e9ca5).

## Question

Can an independently authored change request give us a test for the new behavior while a different source tells us what the patch must still preserve? We selected CPython's already-merged addition of `TestCase.assertNoLogs`. This is a retrospective source-and-execution probe. The issue and original patch are external to Paper B. Case selection, observations, and the negative control are ours.

## Evidence available for a decision

| Source | Observation supported | Scope |
| --- | --- | --- |
| [Original feature request](https://github.com/python/cpython/issues/83566#issuecomment-1093851989) | Introduce `assertNoLogs(logger, level)`; a matching log causes failure and appears in its diagnostic. | The request defines the new behavior. It does not separately enumerate the old caller contract. |
| [Existing API documentation](https://docs.python.org/3.9/library/unittest.html#unittest.TestCase.assertLogs) | The value from `with assertLogs(...) as captured` provides raw `records` and formatted `output`. | The relevant section was also verified in `Doc/library/unittest.rst` at the merge commit's parent. The protection comes from the documented public result. |
| [Merged source and tests](https://github.com/python/cpython/commit/6b34d7b51e33fcb21b8827d927474ce9ed1f605c) | The shared context manager still yields a watcher in the old mode and yields `None` in the new mode. The tests distinguish them and also exercise child loggers, levels and exception propagation. | Exact formatting of new failure diagnostics is visible in test assertions. The probe uses the original request's weaker check that the captured log is present. |
| [New API documentation](https://docs.python.org/3.10/library/unittest.html#unittest.TestCase.assertNoLogs) | The new context manager yields no recording object. | The same statement was present in documentation added by the merge. It describes the new API, not the old one. |

## Execution

We loaded the parent and merged versions of four pure-Python `unittest` modules on CPython 3.12.14, using the host's `logging`. Git blob identities of all inputs are checked in [the probe](./probe_assert_no_logs.py). The unit under test is the public behavior of the historical `TestCase` methods in this host. The probe is smaller than a native build and the upstream test suite. It checks raw and formatted captures, failure in the absence of qualifying logs, restoration of logger settings, and four new behaviors: success with no qualifying record, `None` from `as`, an error containing the matching child log, and propagation of an unexpected exception.

| Source variant | New checks | Old `records` and `output` | Old assertion on no qualifying log | Logger settings |
| --- | --- | --- | --- | --- |
| Parent | Method absent | Both pass | Pass | Restored |
| Merged patch | 4/4 | Both pass | Pass | Restored |
| One-line negative control | 4/4 | Both fail | Pass | Restored |

For the negative control, we replaced the old-mode watcher return with `None` in the merged `_log.py`, leaving capture and failure logic in place. We never use this variant as an example of an upstream regression. It holds the candidate fixed across two assessment scopes: the four selected new checks all pass, while those checks plus the documented `assertLogs` return contract reject it. The parent shows that the legacy observers were already supported. We initially compared the identity of the handlers list, but the parent and merge both save a copy of that list. The probe now checks the restored handler objects and order, plus the logging level and propagation flag. List identity is outside the claim.

### Reproduce

With a CPython checkout containing the merge commit and the probe in your current directory:

```sh
revision=6b34d7b51e33fcb21b8827d927474ce9ed1f605c
mkdir -p before after
for name in case.py _log.py util.py result.py; do
    git -C /path/to/cpython show "$revision^:Lib/unittest/$name" > "before/$name"
    git -C /path/to/cpython show "$revision:Lib/unittest/$name" > "after/$name"
done
python3 probe_assert_no_logs.py before after
```

## Where this belongs in Paper B

Paper B's main controlled example remains the catalog. This case demonstrates a practical route to selecting an obligation: read the feature request to locate the new behavior, pin the old public documentation to identify an existing promise, and use a negative control to check whether the observations can detect its violation. It does not rank document sources or measure how often issue-only reviews miss real regressions. The next useful case is one in which documentation and tests support different scopes. Keep both interpretations in view until there is evidence about their authority. In a future comparison, each method can report the cited source and revision, the proposed obligation, the observation that would falsify it, and what happens to the fixed patch's verdict when the obligation is added.

Suggested short text for a later manuscript revision:

> In a retrospective CPython case, adding an assertion for the absence of logs also had to preserve the captured result of the existing assertion. The feature request gave us the first test. The prior API documentation gave us the second. A one-line negative control passed the selected new-behavior checks but lost the documented return value. This illustrates how independent sources can constrain the same patch before a verdict is drawn.

> CPython 사례에서는 로그가 없음을 확인하는 새 기능을 추가하면서, 기존 로그 검사에서 돌려주던 기록도 보존해야 했다. 새 동작은 기능 요청에서, 기존 약속은 변경 전 API 문서에서 확인했다. 반환 한 줄을 바꾼 대조군은 새 기능 검사를 통과했지만 문서에 적힌 기존 반환값을 잃었다.
