# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/np-eye-and-identity/problem?isFullScreen=true
# Problem     Eye and Identity
# Difficulty  Easy
# Subdomain   Numpy
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-18, 09:04 p.m.
# ──────────────────────────────────────────────────

import numpy
numpy.set_printoptions(legacy='1.13')

rows, columns = map(int, input().split())
print(numpy.eye(rows, columns))
