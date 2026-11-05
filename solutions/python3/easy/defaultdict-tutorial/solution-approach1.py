# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true
# Problem     DefaultDict Tutorial
# Difficulty  Easy
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-05, 09:55 a.m.
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
