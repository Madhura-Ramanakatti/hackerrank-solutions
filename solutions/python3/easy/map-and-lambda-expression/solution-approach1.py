# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true
# Problem     Map and Lambda Function
# Difficulty  Easy
# Subdomain   Python Functionals
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-24, 10:49 a.m.
# Technique   iterative-fibonacci-map-lambda
# Time        O(n)
# Space       O(n)
# Insight     The implementation iteratively generates the first n Fibonacci numbers using a tuple-unpacking swap and then applies a lambda function to cube each element via map.
# Interview   Before: "How would you generate and transform a sequence?" After: "I generate the Fibonacci sequence iteratively in O(n) time and O(n) space, then use map with a lambda to cube each value, ensuring the sequence starts with 0 as required by the problem constraints."
# Pitfalls    (1) The loop range(n) correctly handles n=0 by returning an empty list, but failing to account for n=0 might cause errors in other implementations.  (2) The Fibonacci sequence must start with 0 and 1; starting with 1 and 1 would produce an incorrect sequence for this specific problem.
# ──────────────────────────────────────────────────


cube = lambda x: x ** 3



def fibonacci(n):
    numbers = []
    a, b = 0,1
    
    
    for _ in range(n):
        numbers.append(a)
        a,b = b,a + b
        
    return numbers

