# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true
# Problem     itertools.combinations_with_replacement()
# Difficulty  Easy
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-18, 09:01 a.m.
# Technique   itertools-combinations-with-replacement
# Time        O(N^k)
# Space       O(k)
# Insight     The implementation sorts the input string to ensure that combinations_with_replacement produces results in lexicographic order as required by the problem statement.
# Interview   Before: "How do I generate combinations with replacement in Python?" After: "Use itertools.combinations_with_replacement on a sorted list. The time complexity is O(N^k) where N is the string length and k is the combination size, ensuring lexicographic output."
# Pitfalls    (1) Failing to sort the input string before passing it to combinations_with_replacement, which violates the requirement for lexicographic sorted order.  (2) Forgetting to convert the input k from a string to an integer, which causes a TypeError in the itertools function.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

s,k = input().split()

s = sorted(s)

for combination in combinations_with_replacement(s,int(k)):
    print("".join(combination))
    
    
