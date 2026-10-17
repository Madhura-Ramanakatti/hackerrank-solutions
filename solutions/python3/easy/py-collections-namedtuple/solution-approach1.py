# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true
# Problem     Collections.namedtuple()
# Difficulty  Easy
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-17, 09:21 a.m.
# Technique   namedtuple-dynamic-attribute-access
# Time        O(N)
# Space       O(N)
# Insight     The implementation dynamically maps input column headers to a namedtuple class and aggregates the MARKS attribute across all student records.
# Interview   Before: "I would parse the spreadsheet by finding the index of the MARKS column manually." After: "Using namedtuple allows for cleaner attribute access by name, resulting in O(N) time complexity where N is the number of students, regardless of column order."
# Pitfalls    (1) Assuming the MARKS column is at a fixed index when it can appear in any position.  (2) Failing to cast the MARKS value to an integer before summation.  (3) Incorrectly formatting the output to fewer or more than two decimal places.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple
n = int(input())
Student = namedtuple('Student', input().split())
print("{:.2f}".format(sum(int(Student(*input().split()).MARKS)for _ in range(n))/n))


