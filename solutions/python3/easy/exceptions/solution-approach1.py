# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true
# Problem     Exceptions
# Difficulty  Easy
# Subdomain   Errors and Exceptions
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-12, 08:58 a.m.
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
