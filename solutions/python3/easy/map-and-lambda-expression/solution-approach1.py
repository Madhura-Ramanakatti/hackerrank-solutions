# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true
# Problem     Map and Lambda Function
# Difficulty  Easy
# Subdomain   Python Functionals
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-24, 10:47 a.m.
# ──────────────────────────────────────────────────


cube = lambda x: x ** 3



def fibonacci(n):
    numbers = []
    a, b = 0,1
    
    
    for _ in range(n):
        numbers.append(a)
        a,b = b,a + b
        
    return numbers

