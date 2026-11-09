# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
# Problem     The Minion Game
# Difficulty  Medium
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-09, 10:29 a.m.
# Technique   linear-scan-substring-counting
# Time        O(n)
# Space       O(1)
# Insight     The number of substrings starting at index i is equal to the remaining length of the string, n minus i, which is added to the respective player's score based on the character type.
# Interview   Before: "I should generate all possible substrings and count their occurrences." After: "Generating all substrings is O(n^2) or worse. Instead, I can iterate once in O(n) time, noting that every character at index i starts exactly n-i substrings, allowing me to calculate scores in linear time."
# Pitfalls    (1) Failing to recognize that the number of substrings starting at index i is exactly n-i, leading to an inefficient O(n^2) nested loop approach.  (2) Incorrectly identifying vowels by omitting 'AEIOU' or misinterpreting the rule that only 'AEIOU' are vowels.
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
        
            
            
            



