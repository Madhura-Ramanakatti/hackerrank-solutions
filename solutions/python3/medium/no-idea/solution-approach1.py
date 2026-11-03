# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true
# Problem     No Idea!
# Difficulty  Medium
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-03, 05:57 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT


n,m = map(int,input().split())

arr = list(map(int, input().split()))

A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0


for x in arr:
    if x in A:
        happiness += 1
    elif x in B:
        happiness -=1
        
print(happiness)

