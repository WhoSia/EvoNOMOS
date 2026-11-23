"""Paper B v51: context-to-warrant map, not a new logic or superior to strong ADR.

Evaluate three *different* normative types separately. Do not collapse a failed
behavioral contract into a defeated design heuristic. No automatic decisions.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Optional
import json


class Kind(str, Enum):
    CONTRACT = 'behavior_contract'
    POLICY = 'authorized_policy'
    HEURISTIC = 'defeasible_advice'


class Status(str, Enum):
    SUPPORT = 'supported'
    DEFEAT = 'defeated'
    BOTH = 'conflicted'
    UNKNOWN = 'undetermined'


@dataclass(frozen=True)
class Context:
    id: str
    future_extensions: Optional[bool]
    behavior_preserved: Optional[bool]
    authorized_rule: Optional[bool]
    evidence_source: str


@dataclass(frozen=True)
class Warrant:
    kind: Kind
    id: str
    reason: str


def decide(w: Warrant, c: Context) -> Status:
    if not c.id or not c.evidence_source:
        raise ValueError('missing context provenance')
    if w.kind == Kind.CONTRACT:
        value = c.behavior_preserved
    elif w.kind == Kind.POLICY:
        value = c.authorized_rule
    elif w.kind == Kind.HEURISTIC:
        value = c.future_extensions
    else:
        raise ValueError('unknown normative kind')
    return Status.UNKNOWN if value is None else (Status.SUPPORT if value else Status.DEFEAT)


def changes(warrants, before: Context, after: Context):
    return [dict(id=w.id, kind=w.kind.value, before=decide(w,before).value,
                 after=decide(w,after).value)
            for w in warrants]


def test():
    warrants = (Warrant(Kind.CONTRACT,'C','preserve existing behavior'),
                Warrant(Kind.POLICY,'P','authorized local policy'),
                Warrant(Kind.HEURISTIC,'H','extension forecast justifies abstraction'))
    initial = Context('t0',True,True,True,'historical scenario')
    revised = Context('t1',False,True,True,'revised forecast')
    out = changes(warrants,initial,revised)
    assert [x['after'] for x in out] == ['supported','supported','defeated']
    assert out[2]['before']=='supported'
    # A removed policy is not a broken behavioral contract or invalid forecast.
    policy_removed = Context('t2',True,True,False,'policy authority ledger')
    assert [x['after'] for x in changes(warrants,initial,policy_removed)] == ['supported','defeated','supported']
    unknown = Context('t3',None,None,None,'evidence pending')
    assert [x['after'] for x in changes(warrants,initial,unknown)] == ['undetermined']*3
    # Fail-closed missing source; no invented evidence.
    try:
        decide(warrants[0],Context('bad',True,True,True,''))
    except ValueError:
        pass
    else:
        raise AssertionError('missing evidence provenance accepted')
    return {'result':'PASS_TYPED_MAP_INVARIANTS','cases':3,'warrants':3,
            'novelty_established':False,'strong_adr_comparator':'NOT_IMPLEMENTED',
            'human_benefit':'NOT_MEASURED','context_change':out}


if __name__=='__main__':
    print(json.dumps(test(),indent=2,ensure_ascii=False))
