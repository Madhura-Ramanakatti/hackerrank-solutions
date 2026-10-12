# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true
# Problem     Exceptions
# Difficulty  Easy
# Subdomain   Errors and Exceptions
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-12, 08:58 a.m.
# Technique   try-except-block-handling
# Time        O(T)
# Space       O(1)
# Pitfalls    (1) Failing to use integer division operator // as specified in the Python 3 note.  (2) Incorrectly catching generic Exception instead of specific ZeroDivisionError and ValueError types.  (3) Omitting the 'Error Code:' prefix required by the output format.
# ──────────────────────────────────────────────────


# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())

for i in range(T):
    a, b = input().split()

    try:
        print(int(a) // int(b))

    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")

    except ValueError as e:
        print("Error Code:", e)
