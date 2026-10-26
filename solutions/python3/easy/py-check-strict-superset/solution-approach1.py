# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true
# Problem     Check Strict Superset
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-26, 10:26 p.m.
# Technique   all-generator-strict-superset
# Time        O(N * M)
# Space       O(M)
# Insight     The code uses the all() function to verify that the primary set A is a strict superset of every input set by leveraging the Python > operator for sets.
# Interview   Before: "How would you check if a set is a strict superset of multiple others?" After: "I would use the all() function with the > operator, which runs in O(N * M) time where N is the number of sets and M is the average set size, ensuring every set is a proper subset."
# Pitfalls    (1) Confusing the > operator for strict superset with the >= operator for subset or superset.  (2) Failing to account for the requirement that a strict superset must contain at least one element not present in the subset.  (3) Assuming the input sets are already provided as sets rather than space-separated strings requiring conversion.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT




A = set(input().split())

n = int(input())

print(all(A > set(input().split()) for _ in range(n)))


