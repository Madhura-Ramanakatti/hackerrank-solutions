# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=true
# Problem     Set .intersection() Operation
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-22, 04:32 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())

English = set(map(int, input().split()))

M = int(input())

French =set(map(int,input().split()))

print(len(English & French))


