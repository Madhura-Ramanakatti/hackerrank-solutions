# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-eval/problem?isFullScreen=true
# Problem     Python Evaluation
# Difficulty  Easy
# Subdomain   Built-Ins
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-20, 09:35 p.m.
# Technique   dynamic-expression-evaluation
# Time        O(N)
# Space       O(N)
# Insight     The program reads a string from standard input and executes it as a Python expression using the built-in eval function.
# Interview   Before: "How do I execute a string as code?" After: "You can use the eval() function, which parses and executes the string as a Python expression in O(N) time, where N is the length of the input string."
# Pitfalls    (1) Using eval() on untrusted input introduces arbitrary code execution vulnerabilities.  (2) The eval() function only evaluates expressions and will raise a SyntaxError if provided with complex statements like multi-line definitions.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT


var = input()
eval(var)


