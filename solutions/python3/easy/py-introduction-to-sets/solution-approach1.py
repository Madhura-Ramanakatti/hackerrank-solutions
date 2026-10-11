# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true
# Problem     Introduction to Sets
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-11, 09:02 a.m.
# Technique   set-deduplication-average
# Time        O(N)
# Space       O(N)
# Insight     The implementation utilizes a set to filter unique elements from the input array, allowing for an efficient calculation of the average of distinct values.
# Interview   Before: "How would you calculate the average of unique elements in an array?" After: "I would convert the array to a set to eliminate duplicates in O(N) time and O(N) space, then compute the sum divided by the length of the set."
# Pitfalls    (1) Passing an empty list to the function will cause a ZeroDivisionError because the set length will be zero.  (2) Rounding the result before the final return might lead to precision errors if intermediate calculations were required.
# ──────────────────────────────────────────────────

def average(array):
    distinct_heights = set(arr)
    total = sum(distinct_heights)
    count = len(distinct_heights)
    result = total / count
    return round(result, 3)
    
    
    

