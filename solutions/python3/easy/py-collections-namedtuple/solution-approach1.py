# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true
# Problem     Collections.namedtuple()
# Difficulty  Easy
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-17, 09:21 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple
n = int(input())
Student = namedtuple('Student', input().split())
print("{:.2f}".format(sum(int(Student(*input().split()).MARKS)for _ in range(n))/n))


