"""Decision-quality audit of previously published P35-P5 AGGREGATE counts.

Does NOT refit original Go AST/cochange models, invent per-commit data, or
pretend the 47 seed-queries are independent.  A 'do not alert' policy is
a decision baseline, not a predictor that can solve joint-change cases.
"""
from dataclasses import dataclass
from fractions import Fraction

@dataclass(frozen=True)
class Counts:
    positives: int
    negatives: int
    top1_hits: int
    false_alerts: int
    def validate(self):
        assert self.positives >= 0 and self.negatives >= 0
        assert 0 <= self.top1_hits <= self.positives
        assert 0 <= self.false_alerts <= self.negatives
        return self

P35_B0_B1=Counts(positives=13,negatives=34,top1_hits=9,false_alerts=34).validate()
P35_B2=Counts(positives=13,negatives=34,top1_hits=8,false_alerts=34).validate()

@dataclass(frozen=True)
class Penalties:
    false_alert: Fraction
    miss_joint: Fraction
    wrong_location: Fraction
    def validate(self):
        assert all(x>=0 for x in (self.false_alert,self.miss_joint,self.wrong_location))
        return self

def loss_original_always_alert(counts: Counts, penalty: Penalties) -> Fraction:
    """If wrong location implies missed needed site PLUS mislocalized review."""
    return (counts.false_alerts*penalty.false_alert
        +(counts.positives-counts.top1_hits)*(penalty.miss_joint+penalty.wrong_location))

def loss_never_alert(counts: Counts, penalty: Penalties) -> Fraction:
    return counts.positives*penalty.miss_joint

def break_even_false_alert_to_miss_ratio(counts:Counts,wrong_location_to_miss:Fraction=Fraction(0)) -> Fraction:
    """Only when false_alerts>0, miss_joint>0, other costs fixed to w*m."""
    if counts.false_alerts==0:raise ValueError("no observed false alerts")
    return Fraction(counts.top1_hits,counts.false_alerts) - Fraction(counts.positives-counts.top1_hits,counts.false_alerts)*wrong_location_to_miss

def verdict(p:Penalties, counts:Counts=P35_B0_B1)->str:
    original=loss_original_always_alert(counts,p)
    none=loss_never_alert(counts,p)
    if original==none:return "TIE"
    return "ALERT" if original<none else "ABSTAIN"

if __name__=="__main__":
    for p in (Penalties(Fraction(1),Fraction(1),Fraction(0)),
              Penalties(Fraction(1,10),Fraction(1),Fraction(1))):
        print("cost",p,"original",loss_original_always_alert(P35_B0_B1,p),
              "no-alert",loss_never_alert(P35_B0_B1,p),"choice",verdict(p))
    print("false_alert/miss threshold when wrong_location=0",
          break_even_false_alert_to_miss_ratio(P35_B0_B1))
    print("false_alert/miss threshold when wrong_location=miss",
          break_even_false_alert_to_miss_ratio(P35_B0_B1,Fraction(1)))
