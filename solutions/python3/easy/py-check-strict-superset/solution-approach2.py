# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true
# Problem     Check Strict Superset
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-22, 08:54 a.m.
# Technique   set-issuperset-and-length-check
# Time        O(N * M)
# Space       O(M)
# Insight     The code verifies the strict superset condition by checking if the main set contains all elements of the target set and possesses a strictly greater cardinality.
# Interview   Before: "I would iterate through each set and check if every element exists in the main set." After: "Using the built-in issuperset method combined with a length comparison provides an O(N * M) solution, where N is the number of sets and M is the average set size, ensuring the strict superset requirement is met."
# Pitfalls    (1) Confusing a standard superset with a strict superset by omitting the length comparison.  (2) Failing to account for the requirement that the main set must contain at least one element not present in the subset.  (3) Assuming issuperset alone handles the strict condition, which it does not.
# ──────────────────────────────────────────────────

main_set = set(input().split())
number_of_sets = int(input())

result = True

for _ in range(number_of_sets):
    other_set = set(input().split())

    if not (main_set.issuperset(other_set) and len(main_set) > len(other_set)):
        result = False

print(result)

