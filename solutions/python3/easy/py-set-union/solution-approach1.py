# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true
# Problem     Set .union() Operation
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-13, 08:07 a.m.
# Technique   set-union-operator
# Time        O(n + m)
# Space       O(n + m)
# Insight     The union of two sets is computed using the bitwise OR operator to aggregate unique elements from both collections into a single set.
# Interview   Before: "How would you count unique students across two lists?" After: "I use the set union operator, which runs in O(n + m) time, to merge the collections and return the length of the resulting set, effectively handling duplicates automatically."
# Pitfalls    (1) Confusing the | operator with the .union() method, noting that | requires both operands to be sets while .union() accepts any iterable.  (2) Assuming the input sets are already sorted, which is not guaranteed by the set data structure.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT


n = int(input())
english = set(map(int, input().split()))

m = int(input())

french = set(map(int, input().split()))

print(len(english | french))
