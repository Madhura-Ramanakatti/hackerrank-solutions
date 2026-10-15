# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true
# Problem     Set .discard(), .remove() & .pop()
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-15, 09:40 p.m.
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

