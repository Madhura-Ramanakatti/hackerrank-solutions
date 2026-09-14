# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
# Problem     Python If-Else
# Difficulty  Easy
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-14, 06:59 p.m.
# Technique   conditional-logic-branching
# Time        O(1)
# Space       O(1)
# Insight     The code groups odd numbers and the inclusive range of 6 to 20 as Weird, while handling the remaining even cases as Not Weird.
# Interview   Before: "How would you handle multiple conditional ranges for an integer?" After: "I used a single conditional check for the Weird cases to achieve O(1) time complexity, ensuring the inclusive ranges 2-5 and 6-20 are correctly evaluated against the parity of n."
# Pitfalls    (1) Failing to include the upper bound 20 in the Weird range due to exclusive range logic.  (2) Misinterpreting the inclusive range 2 to 5 as Not Weird for odd numbers.  (3) Neglecting the requirement that the number must be even for the Not Weird conditions.
# ──────────────────────────────────────────────────



if __name__ == '__main__':
    n = int(input().strip())
if n % 2 != 0 or 6<=n<=20:
    print("Weird")
else:
    if 2<=n<=5 or n>20: 
        print("Not Weird")
