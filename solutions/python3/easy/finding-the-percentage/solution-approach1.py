# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
# Problem     Finding the percentage
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-06, 07:20 p.m.
# Technique   hash-map-average-calculation
# Time        O(N + M)
# Space       O(N * M)
# Insight     The implementation maps student names to lists of floating-point scores in a dictionary, then computes the arithmetic mean of the queried list using Python's sum and len functions.
# Interview   Before: "How would you store and retrieve student records efficiently?" After: "I used a dictionary for O(1) average-case lookup time. By mapping names to lists, I can calculate the mean in O(M) time, where M is the number of scores, resulting in an overall O(N + M) complexity."
# Pitfalls    (1) Failing to format the output to exactly two decimal places using f-string syntax, which is required by the problem statement.  (2) Assuming the input scores are integers when the problem requires floating-point precision for accurate averaging.  (3) Neglecting to handle the case where the query_name might not exist in the dictionary, though the problem constraints imply valid inputs.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    
    average = sum(student_marks[query_name]) / len(student_marks[query_name])
    
    print(f"{average:.2f}")
    
