# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/validating-the-phone-number/problem?isFullScreen=true
# Problem     Validating phone numbers
# Difficulty  Easy
# Subdomain   Regex and Parsing
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-19, 06:15 p.m.
# ──────────────────────────────────────────────────

import re

n = int(input())

for _ in range(n):
    number = input().strip()

    if re.fullmatch(r"[789]\d{9}", number):
        print("YES")
    else:
        print("NO")
        
        
