# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true
# Problem     Company Logo
# Difficulty  Medium
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-02, 08:15 a.m.
# Technique   counter-frequency-sorting
# Time        O(N log N)
# Space       O(N)
# Insight     The implementation uses a frequency map to count character occurrences and sorts the items using a custom key that negates the count for descending order while maintaining alphabetical order for ties.
# Interview   Before: "How would you find the top three characters?" After: "I would use a frequency map to count occurrences, then sort the items by count descending and character ascending. This approach runs in O(N log N) time, where N is the string length, effectively handling the tie-breaking rules specified."
# Pitfalls    (1) Failing to handle the tie-breaking rule where characters must be sorted alphabetically when counts are identical.  (2) Neglecting to sort the frequency map correctly by using a custom key that handles both descending counts and ascending alphabetical order simultaneously.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter  


if __name__ == '__main__':
    s = input()
    
    count = Counter(s)
    result = sorted(count.items(), key=lambda x: (-x[1],x[0]))
    
    for char, frequency in result[:3]:
        print(char, frequency)
        
        
        
