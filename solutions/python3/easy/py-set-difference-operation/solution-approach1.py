# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true
# Problem     Set .difference() Operation
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-21, 10:50 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
english = set(map(int, input().split()))

m = int(input())
french = set(map(int, input().split()))

print(len(english - french))
