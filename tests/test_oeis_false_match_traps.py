#!/usr/bin/env python3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from oeis_false_match_traps import partner_divisors, r_pairs


def test_pairs_agree_until_60():
    for n in range(1, 60):
        assert r_pairs(n) == partner_divisors(n), n


def test_first_split_at_60():
    # Issue #356: r(60)=13 (pairs) vs A174903(60)=9 (divisors with a partner).
    assert r_pairs(60) == 13
    assert partner_divisors(60) == 9


if __name__ == "__main__":
    test_pairs_agree_until_60()
    test_first_split_at_60()
    print("ok - oeis false-match traps")
