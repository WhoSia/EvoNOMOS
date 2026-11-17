# One patch, two maintenance requests and two client contracts

Run `python3 meyer_judgment_pair.py` from this directory. The earlier [library reconstruction](./15_MEYER_LIBRARY_CLOSURE.md) remains the source for the scenario and the baseline inputs. This executable comparison adapts that reconstruction. Neither the erratum nor the exact output strings come from the 1988 example.

The candidate adds a provider for technical reports. It leaves both existing files byte-identical, changes the rendered book prefix from `book` to `BOOK`, and delegates the unsupported erratum to the existing catalog. Every candidate comparison uses those same bytes. Only the demand and the protected observations vary. Both contracts preserve the journal and proceedings observations and the legacy rejection of an unrelated unknown kind. The second also protects the book rendering.

| Required change | Protected legacy observations | Demand met | Contract preserved | Candidate acceptable |
|---|---|---|---|---|
| Render technical reports | Journal, proceedings, unknown | Yes | Yes | Yes |
| Render technical reports | Journal, proceedings, unknown, book | Yes | No | No |
| Render reports and errata | Journal, proceedings, unknown | No | Yes | No |
| Render reports and errata | Journal, proceedings, unknown, book | No | No | No |

A separate additive provider supplies both new kinds and preserves every legacy observation, including book rendering, without editing either existing file. All four task specifications are satisfiable through the same permitted file-addition boundary.

Let the proposed input to a judgment contain only the before and after code. The candidate gives that input the same value in all four cases. A function of that input alone has one value, while the observed maintenance judgment has two. This is a finite witness that the declared demand and protected observations matter for this decision. A label tied exclusively to those fixed bytes also contributes identical input in all four cases. An assessment that receives no governing demand or caller obligation can state its assumption or withhold a maintenance verdict where these admissible specifications disagree.

This is an illustration with project-authored obligations. The earlier historical audit covers one benchmark's saved inputs. The executable case measures neither the classification accuracy of that benchmark nor judge responses to varying context.
