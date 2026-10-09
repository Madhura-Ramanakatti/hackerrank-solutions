# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
# Problem     collections.Counter()
# Difficulty  Easy
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-09, 08:16 a.m.
# ──────────────────────────────────────────────────


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

X = int(input())
shoe_sizes = Counter(map(int, input().split()))

N = int(input())
money = 0

for i in range(N):
    size, price = map(int, input().split())

    if shoe_sizes[size] > 0:
        money += price
        shoe_sizes[size] -= 1

print(money)
