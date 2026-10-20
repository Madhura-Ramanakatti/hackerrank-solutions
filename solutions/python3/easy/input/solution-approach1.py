# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/input/problem?isFullScreen=true
# Problem     Input()
# Difficulty  Easy
# Subdomain   Built-Ins
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-20, 09:24 p.m.
# Technique   python-eval-evaluation
# Time        O(N)
# Space       O(N)
# Insight     The solution leverages the Python 2 eval function to dynamically parse and compute the polynomial expression string by substituting the variable x with its provided integer value.
# Interview   Before: "How would you parse a mathematical string expression?" After: "In Python 2, one can use eval() to compute the result of a string expression directly. This approach runs in O(N) time relative to the length of the polynomial string, effectively verifying the equality P(x) == k."
# Pitfalls    (1) The use of eval() is restricted to Python 2 environments as specified in the problem statement.  (2) The input polynomial string must be formatted as a valid Python expression for the eval() function to execute correctly.
# ──────────────────────────────────────────────────

x, k = map(int, input().split())
polynomial = input()

print(eval(polynomial) == k)
