# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true
# Problem     Compress the String! 
# Difficulty  Medium
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-06, 08:31 a.m.
# Technique   itertools-groupby-aggregation
# Time        O(N)
# Space       O(N)
# Insight     The groupby function partitions the input string into contiguous segments of identical characters, allowing the length of each segment to be calculated and formatted as a tuple.
# Interview   Before: "How would you count consecutive character occurrences?" After: "I used itertools.groupby to group identical characters, which runs in O(N) time and O(N) space, effectively handling the 10^4 constraint by iterating through the string once."
# Pitfalls    (1) Converting the groupby iterator to a list is necessary to determine the count, which consumes O(N) space.  (2) The groupby function treats each character as a string, requiring an explicit cast to int to match the required output format.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT



from itertools import groupby


s = input()


for key, group in groupby(s):
    count = len(list(group))
    
    print((count, int(key)),end = " ")
    
    
