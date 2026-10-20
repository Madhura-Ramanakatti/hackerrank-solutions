# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true
# Problem     itertools.combinations()
# Difficulty  Easy
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-20, 09:43 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT


from itertools import combinations 

s,k = input().split()

k = int(k)

s = sorted(s)

for i in range(1, k + 1):
    for c in combinations(s, i):
        print(''.join(c))
