# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true
# Problem     Compress the String! 
# Difficulty  Medium
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-06, 08:31 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT



from itertools import groupby


s = input()


for key, group in groupby(s):
    count = len(list(group))
    
    print((count, int(key)),end = " ")
    
    
