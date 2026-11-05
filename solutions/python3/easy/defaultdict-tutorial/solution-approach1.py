# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true
# Problem     DefaultDict Tutorial
# Difficulty  Easy
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-05, 09:55 a.m.
# Technique   defaultdict-list-mapping
# Time        O(n + m)
# Space       O(n)
# Insight     The implementation maps each unique word in group A to a list of its 1-indexed positions using a defaultdict, allowing O(1) average time lookup for each word in group B.
# Interview   Before: "I would use a standard dictionary and check for key existence before appending." After: "Using a defaultdict(list) simplifies the logic by automatically initializing empty lists, resulting in O(n + m) time complexity and O(n) space complexity to store all indices for group A words."
# Pitfalls    (1) Forgetting that the problem requires 1-indexed positions, which necessitates adding 1 to the loop index i.  (2) Using a standard dictionary instead of defaultdict, which requires explicit key existence checks before appending to the list.  (3) Failing to handle the case where a word from group B is not present in group A by printing -1.
# ──────────────────────────────────────────────────


from collections import defaultdict

n, m = map(int, input().split())

d = defaultdict(list)

# Group A
for i in range(n):
    word = input()
    d[word].append(i + 1)

# Group B
for j in range(m):
    word = input()

    if word in d:
        print(*d[word])
    else:
        print(-1)
