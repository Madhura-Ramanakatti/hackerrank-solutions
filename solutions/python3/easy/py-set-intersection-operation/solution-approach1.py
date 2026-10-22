# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=true
# Problem     Set .intersection() Operation
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-22, 04:32 p.m.
# Technique   set-intersection-operator
# Time        O(N + M)
# Space       O(N + M)
# Insight     The code calculates the intersection of two sets using the bitwise AND operator, which returns a new set containing only elements present in both input sets.
# Interview   Before: "How would you find common elements between two lists?" After: "I would convert both lists to sets and use the intersection operator, resulting in O(N + M) time complexity, where N and M are the sizes of the two input sets."
# Pitfalls    (1) Using the & operator requires both operands to be sets, whereas the .intersection() method accepts any iterable as the second argument.  (2) Failing to convert input strings to integers before creating the set will result in a set of strings, which may lead to incorrect comparisons if inputs are numeric.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())

English = set(map(int, input().split()))

M = int(input())

French =set(map(int,input().split()))

print(len(English & French))


