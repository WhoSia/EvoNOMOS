"""R75: auditable claim-to-prior-art links; a *falsification aid*, not novelty proof.

Reference corpus is a manually transcribed, minimal metadata ledger from original
PDF text available in Drive. It is not an automated full-text semantic evaluation.
Run: python -B rationale_precedence_audit.py
"""
from dataclasses import dataclass
from collections import defaultdict
import json


@dataclass(frozen=True)
class Source:
    sid: str
    title: str
    year: int
    drive_id: str
    locators: tuple[str, ...]
    verified_text: bool

    def __post_init__(self):
        if not all((self.sid.strip(), self.title.strip(), self.drive_id.strip())):
            raise ValueError('source needs identity and Drive reference')
        if not self.locators or any(not x.strip() for x in self.locators):
            raise ValueError('source needs precise textual locator')


@dataclass(frozen=True)
class Contact:
    claim_id: str
    source_id: str
    source_locator: str
    relationship: str  # EXACT_PRECEDENCE / PARTIAL_PRECEDENCE / BOUNDARY
    original_claim: str
    source_feature: str

    def __post_init__(self):
        if self.relationship not in {'EXACT_PRECEDENCE', 'PARTIAL_PRECEDENCE', 'BOUNDARY'}:
            raise ValueError('undeclared precedence semantics')
        if not all((self.claim_id.strip(), self.source_id.strip(),
                    self.source_locator.strip(), self.original_claim.strip(),
                    self.source_feature.strip())):
            raise ValueError('incomplete contact')


SOURCES = (
    Source('gibis88', 'gIBIS: A Hypertext Tool for Exploratory Policy Discussion', 1988,
           '1H4muyBGEh0saB6g0VftNx4Ch3YuFIaVw',
           ('Abstract: typed IBIS networks', 'Section on Figure 6: legal outgoing link types',
            'p.318: cost of explicit fine-grained nodes'), True),
    Source('arel07', 'A rationale-based architecture model for design traceability and reasoning', 2007,
           '1CMOiSH7UF3FqkaCr8EUq-e-W2ZSbvYEa',
           ('Abstract: assumptions, constraints, impact and root cause',
            'Sec. 3.2: ARtrace directed links and acyclic graph',
            'Sec. 3.4: qualitative and quantitative rationale'), True),
    Source('elim15', 'Eliminative Argumentation: A Basis for Arguing Confidence in System Properties', 2015,
           '1LkRMzLO8-v36K28zamv-i_VSgTEE_X0D',
           ('Sec. 4.1.6-4.1.8: rebutting, undercutting, undermining',
            'Sec. 3.1: unidentified defeaters',
            'Sec. 3.2: relative importance of defeaters'), True),
    Source('belnap77', 'A Useful Four-Valued Logic', 1977,
           '1w9LLa9y8FQAnQnokyfIDVo7AOjXI2xht',
           ("Editors' Prefatory, pp.5-7: four epistemic states",), True),
    Source('fde18', "Making Belnap's Useful Four-Valued Logic Useful", 2018,
           '1fAKOEEvQ6aS2Di2GLNU15xukHqx4kerJ',
           ('Abstract: missing conditional connective and its extension',
            'Sec. 5: implemented theorem prover'), True),
    Source('drl91', "What's in Design Rationale?", 1991,
           '1MB_mDL7TxssCviINpj__Icbdlv-KIkEd',
           ('PDF: direct text extraction empty; verify using separate authorized facsimile',), False),
)

CONTACTS = (
    Contact('typed_graph', 'gibis88', 'Abstract: typed IBIS networks',
            'EXACT_PRECEDENCE', 'Typed design-argument relationships are new',
            'gIBIS already used typed linked issue/position/argument graphs'),
    Contact('typed_links', 'gibis88', 'Section on Figure 6: legal outgoing link types',
            'EXACT_PRECEDENCE', 'Typed links with type restrictions are new',
            'gIBIS UI restricted legal outgoing link types'),
    Contact('low_effort', 'gibis88', 'p.318: cost of explicit fine-grained nodes',
            'PARTIAL_PRECEDENCE', 'Recording burden is an unexplored concern',
            'gIBIS discussed time and complexity cost of granularity'),
    Contact('rationale_tracing', 'arel07', 'Abstract: assumptions, constraints, impact and root cause',
            'EXACT_PRECEDENCE', 'Cross-decision rationale impact tracing is new',
            'AREL explicitly performs change impact and root-cause tracing'),
    Contact('source_linking', 'arel07', 'Sec. 3.2: ARtrace directed links and acyclic graph',
            'EXACT_PRECEDENCE', 'Explicit links from rationale to design objects are new',
            'AREL had directional rationale-to-architecture links'),
    Contact('design_cost', 'arel07', 'Sec. 3.4: qualitative and quantitative rationale',
            'PARTIAL_PRECEDENCE', 'Explicit design cost-benefit evidence is new',
            'AREL discusses costs, benefits and risks, but this article notes it does not explore quantitative design rationale'),
    Contact('attack_target', 'elim15', 'Sec. 4.1.6-4.1.8: rebutting, undercutting, undermining',
            'EXACT_PRECEDENCE', 'Three target categories for defeaters are new',
            '2015 SEI report names three distinct defeater targets'),
    Contact('unknown_attack', 'elim15', 'Sec. 3.1: unidentified defeaters',
            'PARTIAL_PRECEDENCE', 'Unrecognized attacks are novel to the atlas',
            'Unidentified defeaters are already an assurance concern'),
    Contact('four_states', 'belnap77', "Editors' Prefatory, pp.5-7: four epistemic states",
            'EXACT_PRECEDENCE', 'Four-valued positive/negative evidence state is new',
            'Belnap distinguished true, false, neither and both'),
    Contact('entailment', 'fde18', 'Abstract: missing conditional connective and its extension',
            'BOUNDARY', 'Four-state labels alone establish a novel inference logic',
            '2018 paper explicitly adds conditionals; four labels alone do not supply an entailment system'),
)


def audit(sources=SOURCES, contacts=CONTACTS):
    by_id = {s.sid: s for s in sources}
    if len(by_id) != len(sources):
        raise ValueError('duplicate source identity')
    claims = set()
    tally = defaultdict(int)
    for c in contacts:
        if c.claim_id in claims:
            raise ValueError('duplicate claim identity')
        claims.add(c.claim_id)
        if c.source_id not in by_id:
            raise ValueError('dangling source citation')
        s = by_id[c.source_id]
        if c.source_locator not in s.locators:
            raise ValueError('unverifiable text locator')
        if not s.verified_text:
            raise ValueError('uninspected PDF cannot anchor verified semantic claim')
        tally[c.relationship] += 1
    if any(c.relationship == 'EXACT_PRECEDENCE' and not c.source_feature
           for c in contacts):
        raise ValueError('precedence must be supported')
    return {'sources': len(sources), 'verified_primary_text_sources': sum(s.verified_text for s in sources),
            'unverified_pdf_text_sources': sum(not s.verified_text for s in sources),
            'claim_contact_count': len(contacts), 'contact_counts': dict(tally),
            'novelty': 'UNESTABLISHED', 'actual_review_time': 'NOT_MEASURED'}


def test():
    result = audit()
    assert result['claim_contact_count'] == 10
    assert result['contact_counts'] == {'EXACT_PRECEDENCE': 6,
                                         'PARTIAL_PRECEDENCE': 3, 'BOUNDARY': 1}
    invalid = [
        (SOURCES, CONTACTS + (CONTACTS[0],)),
        (SOURCES, CONTACTS + (Contact('new', 'bad', 'no', 'EXACT_PRECEDENCE','claim','feature'),)),
        (SOURCES, CONTACTS + (Contact('new', 'drl91', SOURCES[-1].locators[0], 'PARTIAL_PRECEDENCE','claim','feature'),)),
        (SOURCES, CONTACTS + (Contact('new', 'arel07', 'does not exist', 'EXACT_PRECEDENCE','claim','feature'),)),
        (SOURCES + (SOURCES[0],), CONTACTS),
    ]
    for corpus, contacts in invalid:
        try:
            audit(corpus, contacts)
        except ValueError:
            continue
        raise AssertionError('fail-open: invalid provenance contact accepted')
    assert all(c.source_id in {s.sid for s in SOURCES if s.verified_text}
               for c in CONTACTS)
    return result | {'negative_controls': len(invalid), 'result': 'PASS_FINITE_SOURCE_LEDGER'}


if __name__ == '__main__':
    print(json.dumps(test(), sort_keys=True, ensure_ascii=False))
