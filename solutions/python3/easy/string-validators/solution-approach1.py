# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
# Problem     String Validators
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-04, 08:50 p.m.
# Technique   generator-expression-any-check
# Time        O(N)
# Space       O(1)
# Insight     The solution utilizes generator expressions with the any() function to perform short-circuit evaluation across the string for each specified character property.
# Interview   Before: "I would iterate through the string five times and maintain boolean flags for each condition." After: "Using any() with generator expressions is more idiomatic and efficient, achieving O(N) time complexity by stopping as soon as a match is found for each of the five required character types."
# Pitfalls    (1) Confusing the any() function with all(), which would incorrectly require every character in the string to satisfy the condition.  (2) Assuming the methods check the entire string rather than searching for at least one occurrence as required by the problem.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    s = input()
    print(any(ch.isalnum()for ch in s))
    print(any(ch.isalpha() for ch in s))
    print(any(ch.isdigit() for ch in s))
    print(any(ch.islower()for ch in s ))
    print(any(ch.isupper() for ch in s))
    
    
