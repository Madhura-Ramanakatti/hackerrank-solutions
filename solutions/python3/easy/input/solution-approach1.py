# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/input/problem?isFullScreen=true
# Problem     Input()
# Difficulty  Easy
# Subdomain   Built-Ins
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-20, 09:24 p.m.
# ──────────────────────────────────────────────────

x, k = map(int, input().split())
polynomial = input()

print(eval(polynomial) == k)
