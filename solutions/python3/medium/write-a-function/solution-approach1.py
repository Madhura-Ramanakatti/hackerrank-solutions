# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
# Problem     Write a function
# Difficulty  Medium
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-28, 08:06 a.m.
# Technique   conditional-logic-leap-year
# Time        O(1)
# Space       O(1)
# Insight     The function evaluates the Gregorian calendar leap year conditions by prioritizing the 400-year cycle, followed by the 100-year exception, and finally the 4-year rule.
# Interview   Before: "How would you determine if a year is a leap year?" After: "I check the divisibility rules in order of precedence: 400, then 100, then 4. This O(1) approach correctly handles the Gregorian calendar's exceptions, such as 1900 being a common year and 2000 being a leap year."
# Pitfalls    (1) Incorrectly ordering the conditions, such as checking divisibility by 4 before checking the 100 or 400-year exceptions.  (2) Failing to account for the rule that years divisible by 100 are not leap years unless they are also divisible by 400.
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

