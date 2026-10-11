# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true
# Problem     Introduction to Sets
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-11, 09:02 a.m.
# ──────────────────────────────────────────────────

def average(array):
    distinct_heights = set(arr)
    total = sum(distinct_heights)
    count = len(distinct_heights)
    result = total / count
    return round(result, 3)
    
    
    

