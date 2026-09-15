# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-division/problem?isFullScreen=true
# Problem     Python: Division
# Difficulty  Easy
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-15, 06:17 p.m.
# Technique   arithmetic-operator-application
# Time        O(1)
# Space       O(1)
# Insight     The implementation utilizes Python's floor division operator for integer results and the standard division operator for floating-point results.
# Interview   Before: "How do you perform division in Python?" After: "Python provides // for floor division and / for float division, both operating in O(1) time complexity regardless of the integer magnitude."
# Pitfalls    (1) Confusing the floor division operator // with the standard division operator /.  (2) Assuming integer division performs rounding instead of truncation toward negative infinity.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)
    
    
