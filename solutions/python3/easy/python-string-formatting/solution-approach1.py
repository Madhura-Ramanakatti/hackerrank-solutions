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
# Insight     The code calculates the binary representation of the maximum value to determine the required padding width, then uses f-string alignment to format each integer from one to n.
# Interview   Before: "How would you align multiple number bases with specific padding?" After: "I calculate the binary length of n to set the width, then use f-string right-alignment. This runs in O(n log n) time, as each of the n numbers requires O(log n) operations for base conversion and formatting."
# Pitfalls    (1) Failing to use the binary length of n as the padding width for all columns.  (2) Using lowercase 'x' in the format specifier instead of the required uppercase 'X' for hexadecimal.  (3) Incorrectly using range(n) instead of range(1, n + 1), which misses the final value.
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

