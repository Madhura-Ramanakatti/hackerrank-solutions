# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/decorators-2-name-directory/problem?isFullScreen=true
# Problem     Decorators 2 - Name Directory
# Difficulty  Easy
# Subdomain   Closures and Decorators
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-27, 11:18 a.m.
# ──────────────────────────────────────────────────



def person_lister(f):
    def inner(people):
        people.sort(key=lambda person: int(person[2]))
        return [f(person) for person in people]
    return inner

