# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true
# Problem     Collections.OrderedDict()
# Difficulty  Easy
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-10, 10:00 a.m.
# Technique   ordered-dictionary-aggregation
# Time        O(N)
# Space       O(K)
# Insight     The implementation uses an OrderedDict to maintain the insertion order of unique item names while aggregating their net prices in linear time.
# Interview   Before: "I would use a standard dictionary and then sort the keys by their first appearance index." After: "Using an OrderedDict simplifies this to O(N) time and O(K) space, as it natively preserves the insertion order of keys during the aggregation process."
# Pitfalls    (1) Splitting the input string incorrectly when item names contain spaces, which requires joining the list of name parts before parsing the price.  (2) Assuming standard dictionaries preserve insertion order, which is only guaranteed in Python 3.7+ but explicitly handled here using OrderedDict for clarity.  (3) Failing to convert the price string to an integer before performing arithmetic operations.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import  OrderedDict

n = int(input())
items = OrderedDict()

for _ in range(n):
    *item_name, price = input().split()
    item_name = " ".join(item_name)
    price = int(price)
    
    if item_name in items:
        items[item_name] += price
    else:
        items[item_name] = price
        
for item_name, net_price in items.items():
    print(item_name, net_price)
    
    
            
