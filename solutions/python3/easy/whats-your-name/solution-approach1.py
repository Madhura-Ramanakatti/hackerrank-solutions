# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=true
# Problem     What's Your Name?
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-30, 08:53 p.m.
# Technique   f-string-interpolation
# Time        O(N+M)
# Space       O(N+M)
# Insight     The function utilizes Python f-string formatting to concatenate the provided first and last name strings into the required output template.
# Interview   Before: "How do I combine these strings with specific text?" After: "I used an f-string to format the output in O(N+M) time, where N and M are the lengths of the input strings, ensuring the exact punctuation required by the problem statement."
# Pitfalls    (1) Failing to include the exclamation mark immediately after the last name as specified in the output format.  (2) Adding extra spaces or omitting the required space between the first and last name in the f-string template.
# ──────────────────────────────────────────────────

#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

