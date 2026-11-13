# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-inner-and-outer/problem?isFullScreen=true
# Problem     Inner and Outer
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-13, 09:01 a.m.
# Technique   numpy-linear-algebra-primitives
# Time        O(N*M)
# Space       O(N*M)
# Insight     The implementation leverages NumPy's optimized linear algebra routines to compute the inner product of two vectors and the outer product matrix directly from input arrays.
# Interview   Before: "How would you compute the inner and outer products of two vectors manually?" After: "Using NumPy's inner and outer functions, we achieve O(N*M) time complexity for the outer product, where N and M are the lengths of the input arrays."
# Pitfalls    (1) Assuming the inner product is a matrix rather than a scalar value.  (2) Confusing the dimensions of the outer product result, which is an N by M matrix.  (3) Failing to handle input as space-separated integers before converting to NumPy arrays.
# ──────────────────────────────────────────────────

import numpy as np 

a = np.array(list(map(int, input().split())))
b = np.array(list(map(int,input().split())))


print(np.inner(a,b))
print(np.outer(a,b))







