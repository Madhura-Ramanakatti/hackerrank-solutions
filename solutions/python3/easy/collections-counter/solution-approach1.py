# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
# Problem     collections.Counter()
# Difficulty  Easy
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-09, 08:16 a.m.
# Technique   hash-map-frequency-counter
# Time        O(X + N)
# Space       O(X)
# Insight     The solution maintains a frequency map of available shoe sizes and decrements the count only when a customer's requested size is available, ensuring each shoe is sold at most once.
# Interview   Before: "I would iterate through the list of shoes for every customer request to check availability." After: "Using a Counter hash map reduces the lookup time to O(1), making the total time complexity O(X + N) where X is the number of shoes and N is the number of customers."
# Pitfalls    (1) Failing to decrement the shoe count after a sale leads to selling the same physical shoe multiple times.  (2) Assuming the Counter object automatically handles zero-count removal without an explicit conditional check.  (3) Neglecting to handle cases where the requested shoe size does not exist in the initial inventory.
# ──────────────────────────────────────────────────


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

X = int(input())
shoe_sizes = Counter(map(int, input().split()))

N = int(input())
money = 0

for i in range(N):
    size, price = map(int, input().split())

    if shoe_sizes[size] > 0:
        money += price
        shoe_sizes[size] -= 1

print(money)
