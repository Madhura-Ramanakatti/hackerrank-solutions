# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true
# Problem     Set .add() 
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-20, 09:31 p.m.
# Technique   set-insertion-counting
# Time        O(N)
# Space       O(N)
# Insight     The implementation utilizes a set data structure to automatically handle duplicate entries, ensuring that only unique country names are stored before calculating the final count.
# Interview   Before: "I would iterate through the list and check if each item exists in a new list before adding it." After: "Using a set provides O(1) average time complexity for insertions, resulting in an O(N) total time complexity to process all N stamps while automatically filtering duplicates."
# Pitfalls    (1) Attempting to use a list instead of a set would result in O(N^2) time complexity due to repeated membership checks.  (2) Failing to account for the fact that .add() returns None, which might lead to errors if the return value is mistakenly used as the set itself.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())


countries = set()

for i in range(n):
    country = input()
    countries.add(country)
    
    
print(len(countries))


