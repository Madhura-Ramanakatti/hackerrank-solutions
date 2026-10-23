# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=true
# Problem     Set .symmetric_difference() Operation
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-23, 09:56 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
English = set(map(int, input().split()))

m = int(input())
French = set(map(int,input().split()))

result = English.symmetric_difference(French)


print(len(result))

