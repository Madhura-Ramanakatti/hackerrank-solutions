# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true
# Problem     Collections.OrderedDict()
# Difficulty  Easy
# Subdomain   Collections
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-10, 10:00 a.m.
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
    
    
            
