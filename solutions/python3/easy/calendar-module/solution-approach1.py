# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true
# Problem     Calendar Module
# Difficulty  Easy
# Subdomain   Date and Time
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-14, 08:22 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT



import calendar

month, day, year = map(int, input().split())

result = calendar.weekday(year, month, day)

print(calendar.day_name[result].upper())
