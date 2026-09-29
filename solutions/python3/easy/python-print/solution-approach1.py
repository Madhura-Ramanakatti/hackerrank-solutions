# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true
# Problem     Print Function
# Difficulty  Easy
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-29, 08:52 a.m.
# Technique   range-loop-print-no-newline
# Time        O(n)
# Space       O(1)
# Insight     The implementation iterates through the range from one to n inclusive, printing each integer sequentially without a trailing newline or separator.
# Interview   Before: "I would concatenate the numbers into a string and print it." After: "By using the end parameter in the print function, I avoid string concatenation and extra memory usage, achieving O(n) time complexity while handling the n constraint efficiently."
# Pitfalls    (1) Using the default print end parameter adds a newline character after every integer, violating the requirement to print the sequence as a single string.  (2) Using range(n) instead of range(1, n + 1) causes the sequence to start at zero and exclude the final integer n.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i, end="")
        
