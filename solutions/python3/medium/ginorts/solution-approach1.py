# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true
# Problem     ginortS
# Difficulty  Medium
# Subdomain   Built-Ins
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-21, 11:17 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT


s = input().strip()


lowercase = sorted(c for c in s if c.islower())
uppercase = sorted(c for c in s if c.isupper())
odd_digits = sorted(c for c in s if c.isdigit() and int(c) % 2 == 1)
even_digits = sorted(c for c in s if c.isdigit() and int(c) % 2 == 0)
print("".join(lowercase + uppercase + odd_digits + even_digits))

