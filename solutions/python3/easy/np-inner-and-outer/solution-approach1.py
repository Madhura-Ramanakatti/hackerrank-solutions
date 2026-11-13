# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-inner-and-outer/problem?isFullScreen=true
# Problem     Inner and Outer
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-13, 09:00 a.m.
# ──────────────────────────────────────────────────

import numpy as np 

a = np.array(list(map(int, input().split())))
b = np.array(list(map(int,input().split())))


print(np.inner(a,b))
print(np.outer(a,b))







