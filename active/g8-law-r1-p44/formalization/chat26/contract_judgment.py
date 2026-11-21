"""Bounded Paper B fixed-patch judgment under incomplete contracts.

This is a faithful *research-authored* 2x2 version-space model of Paper B v16,
not a measured sample of reviewers or a verifier for arbitrary source patches.
Standard-library only; Python >=3.10.
"""
from dataclasses import dataclass
from enum import Enum
from itertools import product


@dataclass(frozen=True)
class World:
    errata_required: bool
    book_prefix_protected: bool


class Fact(str, Enum):
    ERRATA_REQUIRED = "errata_required"
    REPORT_ONLY = "technical_reports_only"
    BOOK_PROTECTED = "book_prefix_protected"
    BOOK_UNPROTECTED = "book_prefix_unprotected"


class Verdict(str, Enum):
    ACCEPT = "ACCEPT"
    REJECT = "REJECT"
    HOLD = "HOLD"
    INCONSISTENT = "INCONSISTENT"


WORLDS = tuple(World(e, b) for e, b in product((False, True), repeat=2))
FACT_FOR = {
    ("errata", True): Fact.ERRATA_REQUIRED,
    ("errata", False): Fact.REPORT_ONLY,
    ("book", True): Fact.BOOK_PROTECTED,
    ("book", False): Fact.BOOK_UNPROTECTED,
}


def accepts_fixed_patch(world: World) -> bool:
    """Observed patch: reports supported; errata unsupported; book prefix changes."""
    return not world.errata_required and not world.book_prefix_protected


def compatible_worlds(evidence=()):
    evidence = frozenset(evidence)
    return tuple(w for w in WORLDS if
                 (Fact.ERRATA_REQUIRED not in evidence or w.errata_required)
                 and (Fact.REPORT_ONLY not in evidence or not w.errata_required)
                 and (Fact.BOOK_PROTECTED not in evidence or w.book_prefix_protected)
                 and (Fact.BOOK_UNPROTECTED not in evidence or not w.book_prefix_protected))


def verdict(evidence=()) -> Verdict:
    worlds = compatible_worlds(evidence)
    if not worlds:
        return Verdict.INCONSISTENT
    possible = {accepts_fixed_patch(w) for w in worlds}
    if possible == {True}:
        return Verdict.ACCEPT
    if possible == {False}:
        return Verdict.REJECT
    return Verdict.HOLD


def reveal(evidence, dimension: str):
    """Both possible replies to one factual question; impossible replies flagged."""
    if dimension not in ("errata", "book"):
        raise ValueError("dimension must be 'errata' or 'book'")
    return {value: verdict(set(evidence) | {FACT_FOR[(dimension, value)]})
            for value in (False, True)}


def all_consistent_disclosures():
    """All 3^2 possible missing/no/yes disclosure states of this fixed world set."""
    for errata, book in product((None, False, True), repeat=2):
        facts = set()
        if errata is not None:
            facts.add(FACT_FOR[("errata", errata)])
        if book is not None:
            facts.add(FACT_FOR[("book", book)])
        yield frozenset(facts)
