# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=true
# Problem     Set .symmetric_difference() Operation
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-23, 09:56 p.m.
# Technique   set-symmetric-difference
# Time        O(N + M)
# Space       O(N + M)
# Insight     The symmetric difference operation identifies elements present in either the English or French set, but excludes those present in both, effectively calculating the cardinality of the exclusive union.
# Interview   Before: "I would iterate through both lists and count occurrences." After: "Using Python's built-in symmetric_difference method is more efficient, achieving O(N + M) time complexity by leveraging hash-based set lookups to identify unique elements across both subscriptions."
# Pitfalls    (1) Confusing symmetric difference with union, which would include students subscribed to both newspapers.  (2) Assuming the input lists are already sets, which requires explicit conversion to handle the symmetric_difference method correctly.  (3) Neglecting that the symmetric_difference method returns a new set, requiring the len() function to obtain the final count.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
English = set(map(int, input().split()))

m = int(input())
French = set(map(int,input().split()))

result = English.symmetric_difference(French)


print(len(result))

