# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
# Problem     String Split and Join
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-02, 12:44 p.m.
# ──────────────────────────────────────────────────

def split_and_join(line):
    words = line.split(" ") #step1: split at each space 
    result = "-".join(words) #step2: join words by hypen 
    return result            #step3: print the result    
    
    

