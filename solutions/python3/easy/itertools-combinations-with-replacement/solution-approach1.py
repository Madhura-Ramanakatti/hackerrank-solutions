# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true
# Problem     itertools.combinations_with_replacement()
# Difficulty  Easy
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-18, 09:01 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

s,k = input().split()

s = sorted(s)

for combination in combinations_with_replacement(s,int(k)):
    print("".join(combination))
    
    
