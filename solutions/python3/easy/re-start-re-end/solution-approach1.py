# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true
# Problem     Re.start() & Re.end()
# Difficulty  Easy
# Subdomain   Regex and Parsing
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-25, 11:16 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT



import re 

s = input()
k = input()

matches = list(re.finditer(f'(?={re.escape(k)})',s))


if matches:
    for m in matches:
        print((m.start(),m.start() + len(k) - 1))
else:
    print((-1, -1))
    
    
    
