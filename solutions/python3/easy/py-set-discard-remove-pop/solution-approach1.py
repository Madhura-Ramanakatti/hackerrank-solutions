# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true
# Problem     Set .discard(), .remove() & .pop()
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-15, 09:40 p.m.
# Technique   set-command-dispatch
# Time        O(N + M)
# Space       O(N)
# Insight     The implementation processes a sequence of set operations by mapping command strings to their corresponding set methods and calculating the final sum of the remaining elements.
# Interview   Before: "How would you handle multiple set operations efficiently?" After: "I use a set for O(1) average time complexity per operation, resulting in O(N + M) total time, where N is the initial set size and M is the number of commands, while carefully handling KeyError exceptions for remove and pop."
# Pitfalls    (1) Calling remove or pop on an empty set or non-existent element triggers a KeyError.  (2) The pop method removes an arbitrary element, which may lead to non-deterministic results if the specific element removed matters.  (3) Failing to convert command arguments to integers causes type errors during set operations.
# ──────────────────────────────────────────────────

n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    command = input().split()
    
    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        s.remove(int(command[1]))
    elif command[0] == "discard":
        s.discard(int(command[1]))
        
        
print(sum(s))

