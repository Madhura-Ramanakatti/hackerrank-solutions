# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true
# Problem     Min and Max
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-30, 08:58 a.m.
# Technique   numpy-axis-reduction
# Time        O(N * M)
# Space       O(N * M)
# Insight     The implementation reduces the 2D array along the horizontal axis to find row-wise minimums, then computes the maximum value of the resulting 1D array.
# Interview   Before: "I would iterate through each row to find the minimum, then track the global maximum." After: "Using NumPy's axis-specific reduction, I can perform these operations in O(N * M) time, which is efficient for large matrices."
# Pitfalls    (1) Confusing axis 0 (column-wise) with axis 1 (row-wise) leads to incorrect reduction results.  (2) Failing to handle the input dimensions N and M correctly when constructing the NumPy array.
# ──────────────────────────────────────────────────

import numpy as np

n, m = map(int, input().split())

arr = np.array([
    list(map(int, input().split()))
    for _ in range(n)
])

result = np.min(arr, axis=1)

print(np.max(result))
