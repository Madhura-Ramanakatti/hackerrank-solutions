# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
# Problem     Merge the Tools!
# Difficulty  Medium
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-04, 04:02 p.m.
# ──────────────────────────────────────────────────

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        part = string[i:i+k]
        
        
        result = ""

        for char in part:
            if char not in result:
                result += char
                
        print(result)
        
        
