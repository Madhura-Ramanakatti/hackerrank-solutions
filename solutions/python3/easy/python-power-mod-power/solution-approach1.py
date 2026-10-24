# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-power-mod-power/problem?isFullScreen=true
# Problem     Power - Mod Power
# Difficulty  Easy
# Subdomain   Math
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-24, 08:18 p.m.
# Technique   built-in-modular-exponentiation
# Time        O(log b)
# Space       O(1)
# Insight     The implementation utilizes Python's built-in pow function to perform standard exponentiation and efficient modular exponentiation.
# Interview   Before: "I would use a loop to multiply a by itself b times." After: "Using the three-argument pow(a, b, m) is more efficient, operating in O(log b) time, which is critical for large exponents where standard multiplication would overflow or be too slow."
# Pitfalls    (1) Using math.pow instead of the built-in pow function, which returns a float and may cause precision issues.  (2) Providing a negative exponent when using the three-argument pow(a, b, m) function, which violates the constraint that b cannot be negative.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(input())
b = int(input())
m = int(input())

print(pow(a,b))
print(pow(a,b,m))
