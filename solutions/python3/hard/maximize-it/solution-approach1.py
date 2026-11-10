# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true
# Problem     Maximize It!
# Difficulty  Hard
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-10, 05:26 p.m.
# Technique   cartesian-product-brute-force
# Time        O(N^K)
# Space       O(K + N)
# Insight     The solution computes the Cartesian product of all input lists to evaluate every possible combination of elements, identifying the maximum modulo result.
# Interview   Before: "I could use nested loops to pick one element from each list." After: "Since the number of lists K is small, using itertools.product is cleaner. This approach has O(N^K) time complexity, where N is the average list size, effectively exploring the entire search space to find the maximum modulo value."
# Pitfalls    (1) The itertools.product approach will exceed time limits if the total number of combinations is extremely large.  (2) Failing to slice the input list correctly by ignoring the first element, which represents the count of elements in that list.
# ──────────────────────────────────────────────────

from itertools import product

k, m = map(int, input().split())

lists = []

for _ in range(k):
    values = list(map(int, input().split()))
    lists.append(values[1:])

result = 0

for combination in product(*lists):
    total = sum(x ** 2 for x in combination)
    value = total % m
    result = max(result, value)

print(result)


