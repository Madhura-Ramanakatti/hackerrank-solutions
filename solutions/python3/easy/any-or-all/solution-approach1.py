# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true
# Problem     Any or All
# Difficulty  Easy
# Subdomain   Built-Ins
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-26, 10:21 p.m.
# Technique   boolean-logic-generator-expressions
# Time        O(n * d)
# Space       O(n)
# Insight     The solution evaluates the conjunction of two generator expressions, verifying that all integers are positive and at least one integer is palindromic.
# Interview   Before: "I would iterate through the list twice to check conditions." After: "Using all() and any() with generator expressions allows for O(n * d) time complexity, where d is the number of digits, efficiently checking both conditions in a single pass without storing intermediate boolean lists."
# Pitfalls    (1) Failing to handle the empty list case where all() returns True and any() returns False.  (2) Assuming palindromic checks require integer arithmetic instead of string slicing.  (3) Neglecting that all() returns True for an empty iterable, which might lead to incorrect results if the input list is empty.
# ──────────────────────────────────────────────────

n = int(input())
numbers = list(map(int, input().split()))
print(all(x > 0 for x in numbers) and any(str(x) == str(x)[::-1] for x in numbers))


