# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/validating-the-phone-number/problem?isFullScreen=true
# Problem     Validating phone numbers
# Difficulty  Easy
# Subdomain   Regex and Parsing
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-19, 06:15 p.m.
# Technique   regex-fullmatch-pattern
# Time        O(N * L)
# Space       O(1)
# Insight     The implementation uses a regular expression to enforce that the input string consists exactly of a starting digit from the set {7, 8, 9} followed by exactly nine additional digits.
# Interview   Before: "I would iterate through the string and check each character's type and length." After: "Using re.fullmatch with the pattern [789]\d{9} ensures O(L) validation per string, where L is the length, correctly handling the ten-digit requirement and the specific starting digit constraint."
# Pitfalls    (1) Using re.match instead of re.fullmatch would incorrectly validate strings longer than ten digits.  (2) Failing to anchor the regex with fullmatch or ^/$ allows invalid characters to exist before or after the ten-digit sequence.  (3) Assuming the input might contain non-digit characters requires the strict digit class \d to ensure only numeric strings are accepted.
# ──────────────────────────────────────────────────

import re

n = int(input())

for _ in range(n):
    number = input().strip()

    if re.fullmatch(r"[789]\d{9}", number):
        print("YES")
    else:
        print("NO")
        
        
