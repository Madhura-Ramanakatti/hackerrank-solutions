# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true
# Problem     Iterables and Iterators
# Difficulty  Medium
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-28, 09:27 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT



from math import comb

n = int(input())

letters = input().split()

k = int(input())

a_count = letters.count('a')

total_ways = comb(n,k)

ways_without_a = comb(n-a_count, k)

probability = 1 - ways_without_a / total_ways
print(f"{probability:4f}")

