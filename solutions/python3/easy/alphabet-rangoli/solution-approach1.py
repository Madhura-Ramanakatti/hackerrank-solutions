# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true
# Problem     Alphabet Rangoli
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-19, 09:42 a.m.
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


