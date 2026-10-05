# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
# Problem     Find the Runner-Up Score!  
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-05, 08:39 a.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    scores = map(int, input().split())
    
    unique_scores = set(scores)
    unique_scores.remove(max(unique_scores))
    
    
    print(max(unique_scores))
    
    
    
    
    
