# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true
# Problem     Loops
# Difficulty  Easy
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-16, 09:58 a.m.
# Technique   range-based-iteration
# Time        O(n)
# Space       O(1)
# Insight     The code iterates through all non-negative integers i strictly less than n and prints the square of each value.
# Interview   Before: "I should use a while loop to track the index." After: "A range-based for loop is more idiomatic in Python for this O(n) task, as it naturally handles the i < n constraint without manual incrementing."
# Pitfalls    (1) Using range(n + 1) instead of range(n) would violate the i < n constraint.  (2) Failing to handle the input as an integer will cause a type error during multiplication.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    for  i in range(n):
        print(i*i)
        
