"""R78 scanned DRL article: page-grounded, non-exhaustive source audit.

This checks provenance integrity, not scientific novelty. All 31 scanned
pages have machine OCR output, but thirteen OCR page texts were reviewed; six corresponding page images
were visually inspected. The rest remain unverified machine OCR. OCR completion is not full scholarly validation.
"""
from dataclasses import dataclass
import json
from pathlib import Path
import argparse

FILE_ID = '1MB_mDL7TxssCviINpj__Icbdlv-KIkEd'
PAGES = 31
OCR_PAGES = frozenset(range(1, 32))
CHECKED = frozenset((1, 2, 6, 11, 13, 14, 16, 20, 21, 23, 26, 27, 31))
IMAGE_CHECKED = frozenset((1, 13, 14, 20, 23, 27))


@dataclass(frozen=True)
class Contact:
    claim: str
    pdf_page: int
    excerpt: str
    status: str = 'PAGE_OCR_CHECKED'

    def __post_init__(self):
        if not self.claim.strip() or not self.excerpt.strip():
            raise ValueError('blank claim or excerpt')
        if not 1 <= self.pdf_page <= PAGES:
            raise ValueError('PDF page outside source')
        if self.pdf_page not in CHECKED:
            raise ValueError('uninspected PDF page')
        if self.status != 'PAGE_OCR_CHECKED':
            raise ValueError('unearned verification status')


CONTACTS = (
    Contact('representation_adequacy', 1, 'framework for evaluating the expressive adequacy'),
    Contact('alternatives_status', 11, 'waiting for more information'),
    Contact('argument_sharing', 11, 'Some of the arguments can be shared'),
    Contact('decision_graph', 16, 'structure of a decision graph'),
    Contact('contest_criteria', 21, 'argue about whether a goal is desirable'),
    Contact('alternative_limit', 21, 'beyond the current expressive power of DRL'),
    Contact('capture_effort', 26, 'failure and frustration'),
    Contact('criteria_change', 13, 'If the criterion changes'),
    Contact('issue_dependency', 14, 'What are the issues that depend on this issue'),
    Contact('relations_are_claims', 20, 'All DRL relations are special types of Claims'),
    Contact('drl_empirical_claim', 27, 'However, that is a testable claim'),
)


def audit(contacts=CONTACTS):
    unique = set()
    for c in contacts:
        key = (c.claim, c.pdf_page)
        if key in unique:
            raise ValueError('duplicate claim-page assertion')
        unique.add(key)
    return {'source_id': FILE_ID, 'pages': PAGES, 'ocr_checked_pages': len(CHECKED),
            'contact_count': len(contacts), 'ocr_text_pages': len(OCR_PAGES),
            'image_inspected_pages': len(IMAGE_CHECKED),
            'full_text_ocr': True, 'full_manual_review': False,
            'claim_novelty': 'NOT_ESTABLISHED', 'source_scope': 'SELECTIVE_PAGES'}


def verify_excerpts(ocr_dir, contacts=CONTACTS):
    """Require page-specific OCR bytes, rather than trusting the claim ledger."""
    root = Path(ocr_dir)
    for c in contacts:
        file = root / f'page_{c.pdf_page:02d}.txt'
        if not file.is_file():
            raise ValueError(f'missing OCR page {c.pdf_page}')
        page = ' '.join(file.read_text(encoding='utf-8').casefold().split())
        expected = ' '.join(c.excerpt.casefold().split())
        if expected not in page:
            raise ValueError(f'excerpt not present in OCR page {c.pdf_page}: {c.claim}')
    return {'matched_claims': len(contacts), 'ocr_pages_read': len({c.pdf_page for c in contacts}),
            'status': 'OCR_TEXT_MATCH_NOT_FULL_MANUAL_VALIDATION'}


def test():
    x = audit()
    assert x['contact_count'] == 11 and x['ocr_checked_pages'] == 13
    assert x['ocr_text_pages'] == 31 and x['full_manual_review'] is False
    assert x['image_inspected_pages'] == 6
    bad = (
        lambda: Contact('bad', 0, 'x'),
        lambda: Contact('bad', 32, 'x'),
        lambda: Contact('bad', 3, 'not checked'),
        lambda: Contact('bad', 1, 'x', 'WHOLE_ARTICLE_REVIEWED'),
        lambda: Contact(' ', 1, 'x'),
        lambda: Contact('bad', 1, ''),
        lambda: audit(CONTACTS + (CONTACTS[0],)),
    )
    for fn in bad:
        try:
            fn()
        except ValueError:
            continue
        raise AssertionError('fail-open OCR provenance')
    try:
        verify_excerpts('/nonexistent-page-corpus')
    except ValueError:
        pass
    else:
        raise AssertionError('missing OCR corpus incorrectly accepted')
    return x | {'negative_controls': len(bad) + 1, 'result': 'PASS_PAGE_BOUNDARIES'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ocr-dir', default=None)
    args = parser.parse_args()
    result = test()
    if args.ocr_dir:
        result['ocr_source_check'] = verify_excerpts(args.ocr_dir)
    print(json.dumps(result, sort_keys=True))
