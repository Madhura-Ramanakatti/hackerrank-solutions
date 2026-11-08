# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true
# Problem     Find Angle MBC
# Difficulty  Medium
# Subdomain   Math
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-08, 12:51 p.m.
# ──────────────────────────────────────────────────


import math

AB = int(input())
BC = int(input())

angle = math.degrees(math.atan(AB / BC))

result = math.floor(angle + 0.5)

print(str(result) + "\u00b0")
