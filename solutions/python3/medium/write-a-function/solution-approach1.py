# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
# Problem     Write a function
# Difficulty  Medium
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-28, 08:06 a.m.
# ──────────────────────────────────────────────────

def is_leap(year):
    leap = False
    
    if year % 400 == 0:
        return True
        #otherwise it is divisible by 100 is not a leap year.
    if year % 100 == 0:
        return False
        
        
    #Otherwise, a year divisible by 4 is a leap year.
    if year % 4 == 0:
        return True
    return leap

