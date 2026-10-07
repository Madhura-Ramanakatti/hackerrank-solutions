# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true
# Problem     itertools.product()
# Difficulty  Easy
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-07, 08:56 a.m.
# Technique   itertools-cartesian-product
# Time        O(N * M)
# Space       O(N * M)
# Insight     The itertools.product function generates the Cartesian product of input iterables by effectively performing nested loops over the provided lists.
# Interview   Before: "I would write nested loops to iterate through both lists and append pairs to a result list." After: "Using itertools.product is more idiomatic and efficient, yielding an O(N * M) time complexity where N and M are the lengths of the input lists."
# Pitfalls    (1) Failing to unpack the product generator with the asterisk operator results in printing the iterator object instead of the required space-separated tuples.  (2) Assuming the input lists are not already sorted, which would violate the requirement that the Cartesian product output must be in sorted order.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product


A = list(map(int, input().split()))
B = list(map(int, input().split()))


print(*product(A,B))




