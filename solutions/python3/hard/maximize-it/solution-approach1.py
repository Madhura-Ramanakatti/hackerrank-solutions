# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true
# Problem     Maximize It!
# Difficulty  Hard
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-10, 05:26 p.m.
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


