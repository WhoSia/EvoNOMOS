"""Arithmetic reanalysis of 0.3 *reported synthetic* average loss effects.

SOURCE: archived EvoNOMOS Chat Archive/1.md, EvoNOMOS 0.3 completion.
Not executable original 0.3 data; source CSV/report bytes not recovered.
The calculation makes no inferential claim about real human/agent maintainers.
"""
from fractions import Fraction

NEUTRAL = Fraction('22.499')
AWARE = Fraction('-6.386')
MANIFEST = Fraction('-7.222')
DIP_EFFECTS = {
    'neutral': Fraction('92.141'),
    'principle': Fraction('3.098'),
    'manifest': Fraction('3.688'),
}

def mean_loss_effect(neutral_share: Fraction, aware_share: Fraction,
                     manifest_share: Fraction) -> Fraction:
    weights = (neutral_share, aware_share, manifest_share)
    if any(w < 0 for w in weights) or sum(weights) != 1:
        raise ValueError('Population shares must be nonnegative and sum to 1')
    return neutral_share*NEUTRAL + aware_share*AWARE + manifest_share*MANIFEST

def neutral_threshold_when_other_groups_equal() -> Fraction:
    informed = (AWARE + MANIFEST) / 2
    return -informed / (NEUTRAL - informed)

if __name__ == '__main__':
    q = neutral_threshold_when_other_groups_equal()
    print('ORIGINAL_REPORT_ONLY (source CSV not recovered)')
    print('reported_differences', dict(neutral=float(NEUTRAL), principle=float(AWARE), manifest=float(MANIFEST)))
    print('neutral_share_threshold', str(q), '=', float(q))
    print('equally_weighted_three_group_effect', float(mean_loss_effect(Fraction(1,3), Fraction(1,3), Fraction(1,3))))
    print('DIP_three_group_effects', {k:float(v) for k,v in DIP_EFFECTS.items()})
