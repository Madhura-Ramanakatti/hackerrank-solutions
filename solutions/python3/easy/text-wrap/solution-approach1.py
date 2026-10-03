# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
# Problem     Text Wrap
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-03, 08:28 p.m.
# ──────────────────────────────────────────────────



def wrap(string, max_width):
    
    lines = []
    for start in range(0,len(string), max_width):
        lines.append(string[start:start + max_width])
    return "\n".join(lines)
    

