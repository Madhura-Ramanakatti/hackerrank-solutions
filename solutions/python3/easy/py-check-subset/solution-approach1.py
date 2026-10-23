# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true
# Problem     Check Subset
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-23, 09:48 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT


T = int(input())

for i in range(T):
    n = int(input())
    A = set(map(int, input().split()))
    
    
    m = int(input())
    B = set(map(int, input().split()))
    
    print(A.issubset(B))
    
    
    
