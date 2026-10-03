# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
# Problem     Text Wrap
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-03, 08:28 p.m.
# Technique   string-slicing-step-iteration
# Time        O(N)
# Space       O(N)
# Insight     The implementation iterates through the string using a fixed step size equal to the maximum width, slicing segments and joining them with newline characters.
# Interview   Before: "I would use a loop to manually track indices and build the string." After: "Using Python's range with a step parameter allows for an O(N) solution that cleanly handles the string slicing and joining in a single pass."
# Pitfalls    (1) The implementation assumes max_width is a positive integer, as a zero or negative step in range() would raise a ValueError.  (2) The final segment may be shorter than max_width, which is correctly handled by Python's slice notation.
# ──────────────────────────────────────────────────



def wrap(string, max_width):
    
    lines = []
    for start in range(0,len(string), max_width):
        lines.append(string[start:start + max_width])
    return "\n".join(lines)
    

