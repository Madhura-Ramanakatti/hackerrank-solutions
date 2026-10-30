# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true
# Problem     Min and Max
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-30, 08:58 a.m.
# ──────────────────────────────────────────────────

import numpy as np

n, m = map(int, input().split())

arr = np.array([
    list(map(int, input().split()))
    for _ in range(n)
])

result = np.min(arr, axis=1)

print(np.max(result))
