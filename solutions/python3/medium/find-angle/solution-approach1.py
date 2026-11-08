# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true
# Problem     Find Angle MBC
# Difficulty  Medium
# Subdomain   Math
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-08, 12:51 p.m.
# Technique   trigonometric-arctan-rounding
# Time        O(1)
# Space       O(1)
# Insight     The median to the hypotenuse of a right triangle creates an isosceles triangle, allowing the angle MBC to be calculated as the arctangent of the ratio of sides AB and BC.
# Interview   Before: "How would you calculate the angle in a right triangle given two legs?" After: "By using the arctangent function from the math library, we compute the angle in O(1) time, then round to the nearest integer as required by the problem constraints."
# Pitfalls    (1) Rounding using standard integer casting instead of adding 0.5 before flooring fails to meet the requirement of rounding to the nearest integer.  (2) Using math.atan2(BC, AB) instead of math.atan(AB / BC) results in the complementary angle rather than the requested angle MBC.
# ──────────────────────────────────────────────────


import math

AB = int(input())
BC = int(input())

angle = math.degrees(math.atan(AB / BC))

result = math.floor(angle + 0.5)

print(str(result) + "\u00b0")
