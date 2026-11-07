# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true
# Problem     Piling Up!
# Difficulty  Medium
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-07, 06:08 p.m.
# Technique   two-pointers-greedy-comparison
# Time        O(n)
# Space       O(n)
# Insight     The algorithm maintains a non-increasing sequence by greedily selecting the larger of the two available end cubes at each step.
# Interview   Before: "I would use a stack to simulate the pile." After: "A two-pointer approach is more efficient at O(n) time and O(n) space, as it directly compares the ends to ensure each chosen block is less than or equal to the previous one."
# Pitfalls    (1) Failing to update the current block size after each selection leads to incorrect validation of the non-increasing constraint.  (2) Incorrectly handling the equality case in the greedy choice prevents valid sequences from being accepted.  (3) Using an improper initial value for the current block size causes the first comparison to fail.
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
