# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/decorators-2-name-directory/problem?isFullScreen=true
# Problem     Decorators 2 - Name Directory
# Difficulty  Easy
# Subdomain   Closures and Decorators
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-27, 11:18 a.m.
# Technique   decorator-with-lambda-sort
# Time        O(N log N)
# Space       O(N)
# Insight     The decorator wraps the input list of people, sorts them by the age index using a stable sort, and applies the formatting function to each element.
# Interview   Before: "How would you apply a formatting rule to a list of objects while maintaining a specific sort order?" After: "I used a decorator to encapsulate the sorting logic, ensuring O(N log N) time complexity while preserving the original input order for identical ages."
# Pitfalls    (1) Failing to convert the age string to an integer, which causes lexicographical sorting instead of numerical sorting.  (2) Assuming the sort is unstable, though Python's Timsort guarantees the original input order for equal keys.
# ──────────────────────────────────────────────────



def person_lister(f):
    def inner(people):
        people.sort(key=lambda person: int(person[2]))
        return [f(person) for person in people]
    return inner

