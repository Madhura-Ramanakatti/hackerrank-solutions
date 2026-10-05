# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
# Problem     Find the Runner-Up Score!  
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-05, 08:39 a.m.
# Technique   set-max-removal
# Time        O(n)
# Space       O(n)
# Insight     The algorithm identifies the runner-up by converting the input list into a set to eliminate duplicates, removing the maximum value, and then finding the maximum of the remaining elements.
# Interview   Before: "I would sort the list and pick the second element." After: "Sorting takes O(n log n), but using a set to remove duplicates and finding the max takes O(n) time, which is more efficient for large inputs."
# Pitfalls    (1) The code assumes the input contains at least two distinct scores, as calling max() on an empty set after removal will raise a KeyError.  (2) Using set() removes all duplicate scores, which is necessary to correctly identify the runner-up when the maximum score appears multiple times.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    scores = map(int, input().split())
    
    unique_scores = set(scores)
    unique_scores.remove(max(unique_scores))
    
    
    print(max(unique_scores))
    
    
    
    
    
