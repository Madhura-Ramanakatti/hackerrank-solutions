# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-mod-divmod/problem?isFullScreen=true
# Problem     Mod Divmod
# Difficulty  Easy
# Subdomain   Math
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-11, 06:15 p.m.
# Technique   built-in-arithmetic-functions
# Time        O(1)
# Space       O(1)
# Insight     The solution utilizes Python's native integer division, modulo operator, and the divmod function to compute and display the quotient and remainder of two integers.
# Interview   Before: "How would you compute the quotient and remainder of two numbers simultaneously?" After: "I would use the built-in divmod function, which returns a tuple of (a // b, a % b) in O(1) time, ensuring efficient handling of integer arithmetic as required by the problem constraints."
# Pitfalls    (1) Confusing the integer division operator // with the floating-point division operator / in Python 3.  (2) Failing to handle potential ZeroDivisionError if the second input integer is zero.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(input())
b = int(input())

print(a // b)
print(a % b)
print(divmod(a, b))

