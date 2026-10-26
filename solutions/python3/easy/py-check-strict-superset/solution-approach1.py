# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true
# Problem     Check Strict Superset
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-26, 10:26 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT




A = set(input().split())

n = int(input())

print(all(A > set(input().split()) for _ in range(n)))


