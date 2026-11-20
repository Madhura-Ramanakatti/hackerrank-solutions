# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-sort-sort/problem?isFullScreen=true
# Problem     Athlete Sort
# Difficulty  Medium
# Subdomain   Built-Ins
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-20, 08:25 a.m.
# Technique   stable-sort-key-lambda
# Time        O(N log N)
# Space       O(N)
# Insight     Python's built-in sort function maintains stability, ensuring that rows with identical values at the specified index retain their original relative input order.
# Interview   Before: "I would implement a custom quicksort to handle the sorting logic." After: "Python's Timsort is stable and efficient, providing O(N log N) time complexity, which perfectly satisfies the requirement to preserve the original order for rows with identical attributes at index K."
# Pitfalls    (1) Assuming the sort is unstable, which would lead to incorrect ordering for rows with identical attributes at index K.  (2) Failing to account for the zero-based indexing of the K attribute as specified in the problem statement.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    arr.sort(key=lambda row: row[k])
    
    for row in arr:
        print(*row)
        
