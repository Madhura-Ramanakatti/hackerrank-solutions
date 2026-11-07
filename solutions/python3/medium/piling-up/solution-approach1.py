# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true
# Problem     Piling Up!
# Difficulty  Medium
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-07, 06:10 p.m.
# ──────────────────────────────────────────────────

for _ in range(int(input())):
    n = int(input())
    blocks = list(map(int, input().split()))

    left = 0
    right = n - 1
    current = float('inf')

    while left <= right:

        if blocks[left] >= blocks[right]:
            chosen = blocks[left]
            left += 1
        else:
            chosen = blocks[right]
            right -= 1

        if chosen > current:
            print("No")
            break

        current = chosen

    else:
        print("Yes")
