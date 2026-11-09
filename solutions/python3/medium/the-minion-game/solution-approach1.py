# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
# Problem     The Minion Game
# Difficulty  Medium
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-09, 10:29 a.m.
# ──────────────────────────────────────────────────

def minion_game(string):
    n = len(string)
    kevin = 0
    stuart = 0
    
    
    for i in range(n):
        if string[i] in "AEIOU":
            kevin += n - i
            
        else:
            stuart += n - i
            
    if kevin > stuart:
        print("Kevin", kevin)
        
    elif stuart > kevin:
        print("Stuart", stuart)
        
    else:
        print("Draw")
        
            
            
            



