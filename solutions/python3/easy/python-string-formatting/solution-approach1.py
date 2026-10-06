# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true
# Problem     String Formatting
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-06, 08:55 p.m.
# Technique   formatted-string-padding
# Time        O(n * log n)
# Space       O(log n)
# Insight     The implementation calculates the binary width of the maximum integer n to ensure uniform right-alignment for all formatted representations across the range from 1 to n.
# Interview   Before: "How would you format these four bases with consistent padding?" After: "I calculate the binary length of n to determine the required width, then use f-string alignment specifiers to print each base in O(n log n) time, where log n is the number of bits."
# Pitfalls    (1) Failing to use the binary length of n as the padding width for all columns.  (2) Using lowercase 'x' in the format specifier instead of 'X' for capitalized hexadecimal output.  (3) Incorrectly using range(n) instead of range(1, n + 1), which misses the final value n.
# ──────────────────────────────────────────────────

def print_formatted(n):
    width = len(format(n, 'b'))
    
    
    # your code goes here
    
    for value in range(1, n + 1):
        decimal = str(value)
        octal = format(value, 'o')
        hexadecimal = format(value, 'X')
        binary = format(value ,'b')
        
        print(
            f"{decimal:>{width}} "
            f"{octal:>{width}} "
            f"{hexadecimal:>{width}} "
            f"{binary:>{width}}"
                    )

