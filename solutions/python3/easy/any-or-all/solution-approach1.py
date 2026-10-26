# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true
# Problem     Any or All
# Difficulty  Easy
# Subdomain   Built-Ins
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-26, 10:21 p.m.
# ──────────────────────────────────────────────────

n = int(input())
numbers = list(map(int, input().split()))
print(all(x > 0 for x in numbers) and any(str(x) == str(x)[::-1] for x in numbers))


