# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-sort-sort/problem?isFullScreen=true
# Problem     Athlete Sort
# Difficulty  Medium
# Subdomain   Built-Ins
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-20, 08:25 a.m.
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
        
