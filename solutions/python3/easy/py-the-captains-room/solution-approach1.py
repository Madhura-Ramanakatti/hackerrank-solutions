# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true
# Problem     The Captain's Room 
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-16, 08:23 a.m.
# Technique   hash-map-frequency-counting
# Time        O(N)
# Space       O(N)
# Insight     The Captain's room is the unique element in the list because all other room numbers appear exactly K times.
# Interview   Before: "I could sort the list and check for gaps, but that takes O(N log N)." After: "Using a hash map to count frequencies allows identifying the unique room in O(N) time and O(N) space, which is optimal given the unordered input."
# Pitfalls    (1) Assuming the Captain's room must be the smallest or largest number in the list.  (2) Failing to account for the O(N) space complexity when the number of unique rooms is large.  (3) Misinterpreting the problem by assuming the list is sorted or contains consecutive integers.
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
        
        
        
