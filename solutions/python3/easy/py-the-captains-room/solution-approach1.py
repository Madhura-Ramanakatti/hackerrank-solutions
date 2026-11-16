# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true
# Problem     The Captain's Room 
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-16, 08:23 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT



from collections import Counter 

k = int(input())

rooms  = list(map(int, input().split()))

room_counts = Counter(rooms)

for room_number, count in room_counts.items():
    if count == 1:
        print(room_number)
        break
        
        
        
