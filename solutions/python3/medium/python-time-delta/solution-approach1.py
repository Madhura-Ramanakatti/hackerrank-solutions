# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-time-delta/problem?isFullScreen=true
# Problem     Time Delta
# Difficulty  Medium
# Subdomain   Date and Time
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-23, 07:43 a.m.
# ──────────────────────────────────────────────────

#!/bin/python3

import os
from datetime import datetime 

# Complete the time_delta function below.
def time_delta(t1, t2):
    fmt = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)
    
    
    return str(int(abs((dt1 - dt2).total_seconds())))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
