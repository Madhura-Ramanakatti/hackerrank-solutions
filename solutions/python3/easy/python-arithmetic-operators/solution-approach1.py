# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true
# Problem     Arithmetic Operators
# Difficulty  Easy
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-15, 06:13 p.m.
# Technique   basic-arithmetic-operators
# Time        O(1)
# Space       O(1)
# Insight     The implementation performs standard arithmetic operations on two integers read from standard input and prints the results sequentially.
# Interview   Before: "How do I perform basic math in Python?" After: "You use the +, -, and * operators. This approach runs in O(1) time and O(1) space, directly handling the two input integers as specified in the problem statement."
# Pitfalls    (1) Failing to convert input strings to integers using int() before performing arithmetic operations.  (2) Printing the difference as b - a instead of the required a - b.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
    
