# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/reduce-function/problem?isFullScreen=true
# Problem     Reduce Function
# Difficulty  Medium
# Subdomain   Python Functionals
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-17, 08:45 a.m.
# Technique   fraction-reduction-via-reduce
# Time        O(N * log(max(numerator, denominator)))
# Space       O(N)
# Insight     The implementation uses the reduce function to cumulatively multiply a sequence of Fraction objects, leveraging the Fraction class's internal logic to maintain the product in its simplest form.
# Interview   Before: "How would you multiply a list of fractions while ensuring the result is always simplified?" After: "I used Python's fractions.Fraction and functools.reduce to handle the arithmetic. This approach runs in O(N * log(M)) time, where N is the number of fractions and M is the magnitude of the values, ensuring the result is automatically reduced."
# Pitfalls    (1) Failing to import the Fraction class from the fractions module will cause a NameError.  (2) Forgetting to import reduce from the functools module in Python 3 will result in a NameError.  (3) Assuming the input list is empty without handling the initial value of Fraction(1, 1) could lead to unexpected results.
# ──────────────────────────────────────────────────



def product(fracs):
    t = reduce(lambda x, y: x * y,fracs,Fraction(1,1))
    return t.numerator, t.denominator

