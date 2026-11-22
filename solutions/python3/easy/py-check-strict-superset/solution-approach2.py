# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true
# Problem     Check Strict Superset
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-22, 08:54 a.m.
# ──────────────────────────────────────────────────

main_set = set(input().split())
number_of_sets = int(input())

result = True

for _ in range(number_of_sets):
    other_set = set(input().split())

    if not (main_set.issuperset(other_set) and len(main_set) > len(other_set)):
        result = False

print(result)

