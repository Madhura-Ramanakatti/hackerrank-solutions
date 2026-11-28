# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true
# Problem     Iterables and Iterators
# Difficulty  Medium
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-28, 09:27 a.m.
# Technique   combinatorial-probability-complement
# Time        O(N)
# Space       O(N)
# Insight     The probability of selecting at least one 'a' is calculated by subtracting the probability of selecting zero 'a's from the total probability space using combinations.
# Interview   Before: "How would you count all possible subsets containing 'a'?" After: "I used the complement rule: 1 minus the probability of picking only non-'a' elements. This approach runs in O(N) time due to the list count operation and handles the selection constraints efficiently using combinations."
# Pitfalls    (1) Failing to account for the complement probability when calculating the likelihood of at least one occurrence.  (2) Misinterpreting the combination formula by using permutations instead of unordered tuples as specified in the problem explanation.  (3) Incorrectly handling the case where the number of non-'a' elements is less than k, which results in zero ways to select without 'a'.
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

