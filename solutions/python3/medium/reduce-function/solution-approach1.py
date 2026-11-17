# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/reduce-function/problem?isFullScreen=true
# Problem     Reduce Function
# Difficulty  Medium
# Subdomain   Python Functionals
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-17, 08:45 a.m.
# ──────────────────────────────────────────────────



def product(fracs):
    t = reduce(lambda x, y: x * y,fracs,Fraction(1,1))
    return t.numerator, t.denominator

