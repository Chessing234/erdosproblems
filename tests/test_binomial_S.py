#!/usr/bin/env python3
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from binomial_S import ISSUE_PREFIX, S

def test_prefix():
    for i, want in enumerate(ISSUE_PREFIX):
        n = i + 2
        assert S(n) == want, (n, S(n), want)

if __name__ == "__main__":
    test_prefix()
    print("ok - binomial S")
