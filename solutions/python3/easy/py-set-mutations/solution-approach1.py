# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true
# Problem     Set Mutations
# Difficulty  Easy
# Subdomain   Sets
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-04, 03:44 p.m.
# ──────────────────────────────────────────────────


# Read the number of elements in the main set
n = int(input())

# Read the main set
A = set(map(int, input().split()))

# Read the number of operations
N = int(input())

# Perform each operation
for i in range(N):

    # Read operation name and number of elements
    operation, length = input().split()

    # Read the other set
    B = set(map(int, input().split()))

    if operation == "update":
        A.update(B)

    elif operation == "intersection_update":
        A.intersection_update(B)

    elif operation == "difference_update":
        A.difference_update(B)

    elif operation == "symmetric_difference_update":
        A.symmetric_difference_update(B)

# Print the sum of all elements in A
print(sum(A))


