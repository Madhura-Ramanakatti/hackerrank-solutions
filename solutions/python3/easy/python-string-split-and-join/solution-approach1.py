# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
# Problem     String Split and Join
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-02, 12:44 p.m.
# Technique   string-split-and-join
# Time        O(N)
# Space       O(N)
# Insight     The implementation utilizes Python's built-in string methods to tokenize the input string by spaces and reconstruct it using a hyphen delimiter.
# Interview   Before: "How would you replace spaces with hyphens in a string?" After: "I would use the split and join methods, which operate in O(N) time and space, where N is the length of the string, to efficiently transform the delimiter."
# Pitfalls    (1) Using split() without the explicit space argument would cause the method to split on any whitespace, including tabs and multiple spaces, violating the specific space delimiter requirement.  (2) Assuming the input string contains no spaces will result in a single-element list, which join() will return unchanged.
# ──────────────────────────────────────────────────

def split_and_join(line):
    words = line.split(" ") #step1: split at each space 
    result = "-".join(words) #step2: join words by hypen 
    return result            #step3: print the result    
    
    

