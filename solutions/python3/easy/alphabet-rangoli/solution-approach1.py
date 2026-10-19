# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true
# Problem     Alphabet Rangoli
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-19, 09:42 a.m.
# Technique   string-centering-and-slicing
# Time        O(N^2)
# Space       O(N^2)
# Insight     The algorithm constructs each row by generating a decreasing sequence of characters from the boundary letter to the current depth, then mirrors this sequence to form a symmetric line centered with hyphens.
# Interview   Before: "I would use nested loops to build the character sequences." After: "I implemented it by generating the left half of each row and mirroring it, resulting in O(N^2) time and space complexity, which is optimal given the output size for a given N."
# Pitfalls    (1) Incorrectly calculating the total width as 4*N-3, which is required to ensure proper hyphen padding for all rows.  (2) Failing to handle the mirror sequence correctly by using the slice [-2::-1] to exclude the middle character during reversal.  (3) Miscalculating the range of the inner loop, which must iterate up to i+1 to include the correct number of characters for each row.
# ──────────────────────────────────────────────────


def print_rangoli(size):
    width = 4 * size - 3
    lines = []

    for i in range(size):
        left = []

        for j in range(i + 1):
            letter = chr(ord('a') + size - 1 - j)
            left.append(letter)

        letters = left + left[-2::-1]
        line = "-".join(letters)
        lines.append(line.center(width, "-"))

    print("\n".join(lines + lines[-2::-1]))


