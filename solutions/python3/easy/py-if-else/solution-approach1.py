# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
# Problem     Python If-Else
# Difficulty  Easy
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-14, 06:59 p.m.
# ──────────────────────────────────────────────────



if __name__ == '__main__':
    n = int(input().strip())
if n % 2 != 0 or 6<=n<=20:
    print("Weird")
else:
    if 2<=n<=5 or n>20: 
        print("Not Weird")
