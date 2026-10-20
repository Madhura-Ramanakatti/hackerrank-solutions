# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true
# Problem     itertools.combinations()
# Difficulty  Easy
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-20, 09:43 p.m.
# Technique   itertools-combinations-lexicographic-sort
# Time        O(k * nCr(n, k))
# Space       O(n)
# Insight     The implementation sorts the input string to ensure that itertools.combinations produces subsequences in lexicographic order, then iterates through all lengths from one to k.
# Interview   Before: "How would you generate all combinations of varying lengths?" After: "I sort the string first to satisfy the lexicographic requirement, then use itertools.combinations in a loop up to k. This runs in O(k * nCr(n, k)) time, ensuring all subsequences are printed in the correct order."
# Pitfalls    (1) Failing to sort the input string, which causes combinations to be emitted in the order of original indices rather than lexicographic order.  (2) Using range(k) instead of range(1, k + 1), which misses the combinations of length k.  (3) Forgetting to join the tuple elements returned by combinations, resulting in printed tuples instead of concatenated strings.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT


from itertools import combinations 

s,k = input().split()

k = int(k)

s = sorted(s)

for i in range(1, k + 1):
    for c in combinations(s, i):
        print(''.join(c))
