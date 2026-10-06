# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true
# Problem     String Formatting
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-06, 08:55 p.m.
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

