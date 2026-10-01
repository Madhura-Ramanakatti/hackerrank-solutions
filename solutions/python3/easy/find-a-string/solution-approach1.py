# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
# Problem     Find a string
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-01, 08:31 a.m.
# Technique   sliding-window-substring-matching
# Time        O(N*M)
# Space       O(M)
# Insight     The algorithm iterates through all possible starting positions of the substring within the main string, comparing each slice of length M to the target substring.
# Interview   Before: "I could use the built-in count method." After: "Using a sliding window approach with slicing ensures we handle overlapping occurrences correctly, resulting in O(N*M) time complexity where N is the string length and M is the substring length."
# Pitfalls    (1) Failing to include the +1 in the range function causes the loop to miss the final possible substring position.  (2) Miscalculating the slice end index as i + len(sub_string) - 1 would result in an incomplete comparison.
# ──────────────────────────────────────────────────

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)- len(sub_string) + 1):
        if string [i:i +len(sub_string)] == sub_string:
            count += 1
            
            
    return count

