# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true
# Problem     Set .add() 
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-20, 09:31 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())


countries = set()

for i in range(n):
    country = input()
    countries.add(country)
    
    
print(len(countries))


