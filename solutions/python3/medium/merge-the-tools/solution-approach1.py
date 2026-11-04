# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
# Problem     Merge the Tools!
# Difficulty  Medium
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-04, 04:02 p.m.
# Technique   linear-scan-with-string-accumulation
# Time        O(n * k)
# Space       O(k)
# Insight     The algorithm iterates through the string in chunks of size k and maintains a result string that only appends characters not already present in the current chunk.
# Interview   Before: "How would you process substrings of length k to remove duplicates while preserving order?" After: "I iterate through the string in steps of k, using a result string to track seen characters. This approach runs in O(n * k) time, where n is the string length, ensuring each character is processed exactly once per chunk."
# Pitfalls    (1) Failing to maintain the original character order when filtering duplicates.  (2) Assuming the input string length is not a multiple of k, which violates the problem constraints.  (3) Using a set for lookups without preserving the original sequence order required by the problem.
# ──────────────────────────────────────────────────

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        part = string[i:i+k]
        
        
        result = ""

        for char in part:
            if char not in result:
                result += char
                
        print(result)
        
        
