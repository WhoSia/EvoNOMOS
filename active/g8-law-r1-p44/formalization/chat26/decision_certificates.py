"""Exact bounded acceptance certificates over an explicitly declared finite universe.

Classical finite version-space semantics. The universe and atom meanings are
investigator-authored for Paper B; no source/maintainer judgment inferred.
"""
from itertools import combinations
from contract_judgment import Fact, Verdict, compatible_worlds, verdict, WORLDS, accepts_fixed_patch


def consistent_evidence(evidence):
    """Unknown strings are not legitimate contractual facts."""
    facts = frozenset(evidence)
    if not facts.issubset(set(Fact)):
        raise ValueError("Unrecognized evidence atom")
    return bool(compatible_worlds(facts))


def minimal_certificates(target: Verdict):
    """All inclusion-minimal evidence sets forcing ACCEPT or REJECT.

    Search over four signed atoms and explicitly filter contradictions.
    Guarantees minimality *only* within the declared finite four-world court.
    """
    if target not in (Verdict.ACCEPT, Verdict.REJECT):
        raise ValueError("target must be ACCEPT or REJECT")
    candidates = []
    for size in range(len(Fact) + 1):
        for tup in combinations(tuple(Fact), size):
            evidence = frozenset(tup)
            if not consistent_evidence(evidence):
                continue
            if verdict(evidence) != target:
                continue
            if any(witness.issubset(evidence) for witness in candidates):
                continue
            candidates.append(evidence)
    return tuple(candidates)


def ambiguity_witness(evidence=()):
    """Return two fully specified, still compatible worlds with opposed judgments.

    A HOLD is accompanied by verifiable contrasting countermodels, rather than
    a blanket claim that insufficient information exists.
    """
    if not consistent_evidence(evidence):
        return None
    worlds = compatible_worlds(evidence)
    yes = next((w for w in worlds if accepts_fixed_patch(w)), None)
    no = next((w for w in worlds if not accepts_fixed_patch(w)), None)
    if yes is None or no is None:
        return None
    return yes, no


def reveal_partition(evidence, question):
    """Exact compatible-world partitions, excluding impossible answers.

    Unlike a generic question list this returns the actual worlds in each
    feasible branch, allowing independent verification of any verdict.
    """
    facts = frozenset(evidence)
    if not consistent_evidence(facts):
        raise ValueError("Contradictory/invalid starting evidence")
    if question == "errata":
        branches = (Fact.REPORT_ONLY, Fact.ERRATA_REQUIRED)
    elif question == "book":
        branches = (Fact.BOOK_UNPROTECTED, Fact.BOOK_PROTECTED)
    else:
        raise ValueError("Unknown question")
    return {atom: compatible_worlds(facts | {atom}) for atom in branches
            if compatible_worlds(facts | {atom})}


def exact_two_question_strategy(p_errata: float, p_book: float):
    """Select first question minimizing expected count under supplied marginals.

    Zero-error evaluation of A=(not E) and (not B) under an explicitly assumed
    prior over the four authored worlds. A positive answer to E or B rejects.
    Expected count for E-first = 2 - P(E); B-first = 2 - P(B).
    This is ordinary decision-tree theory, not a P44 causal effect.
    """
    if not (0 <= p_errata <= 1 and 0 <= p_book <= 1):
        raise ValueError("Probabilities must be in [0,1]")
    counts = {"errata": 2 - p_errata, "book": 2 - p_book}
    best = min(counts.values())
    return tuple(k for k, n in counts.items() if n == best), counts
