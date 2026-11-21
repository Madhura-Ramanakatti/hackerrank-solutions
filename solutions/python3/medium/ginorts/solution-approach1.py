# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true
# Problem     ginortS
# Difficulty  Medium
# Subdomain   Built-Ins
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-21, 11:17 a.m.
# Technique   partitioned-sorting-concatenation
# Time        O(N log N)
# Space       O(N)
# Insight     The implementation partitions the input string into four distinct character categories and sorts each independently before concatenating them in the specified priority order.
# Interview   Before: "I would use a custom comparator function with sort()." After: "I partitioned the string into four lists based on character type and parity, then sorted each individually. This approach achieves O(N log N) time complexity while strictly adhering to the required sorting hierarchy."
# Pitfalls    (1) Failing to sort the individual character groups, which violates the requirement that each category must be sorted internally.  (2) Incorrectly ordering the digit parity, as the problem requires odd digits to precede even digits.  (3) Using an unstable sorting approach that might disrupt the relative order if not handled by the specific category partitioning.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT


s = input().strip()


lowercase = sorted(c for c in s if c.islower())
uppercase = sorted(c for c in s if c.isupper())
odd_digits = sorted(c for c in s if c.isdigit() and int(c) % 2 == 1)
even_digits = sorted(c for c in s if c.isdigit() and int(c) % 2 == 0)
print("".join(lowercase + uppercase + odd_digits + even_digits))

