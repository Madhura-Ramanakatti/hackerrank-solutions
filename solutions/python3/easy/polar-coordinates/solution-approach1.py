# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true
# Problem     Polar Coordinates
# Difficulty  Easy
# Subdomain   Math
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-08, 08:45 a.m.
# Technique   cmath-module-conversion
# Time        O(1)
# Space       O(1)
# Insight     The implementation utilizes the built-in cmath module to directly compute the modulus and phase angle of a complex number.
# Interview   Before: "How would you convert a complex number to polar coordinates?" After: "I would use the cmath module's phase function and the built-in abs function, which operate in O(1) time, to extract the modulus and phase angle respectively."
# Pitfalls    (1) Failing to use the cmath module for the phase angle calculation.  (2) Assuming the input string format requires manual parsing instead of using the complex() constructor.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT

import cmath

z =complex(input().strip())

print(abs(z))
print(cmath.phase(z))
