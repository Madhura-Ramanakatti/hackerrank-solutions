# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/xml-1-find-the-score/problem?isFullScreen=true
# Problem     XML 1 - Find the Score
# Difficulty  Easy
# Subdomain   XML
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-14, 08:38 a.m.
# Technique   element-tree-recursive-sum
# Time        O(N)
# Space       O(N)
# Insight     The total score is calculated by summing the length of the attribute dictionary for every node in the XML tree using the iter method.
# Interview   Before: "How do I count attributes across nested XML tags?" After: "Use the ElementTree iter method to traverse all nodes, summing the length of each node's attribute dictionary. This approach runs in O(N) time, where N is the total number of elements in the XML tree."
# Pitfalls    (1) Failing to account for the fact that node.iter() includes the root node itself in the traversal.  (2) Assuming that the score is only calculated for leaf nodes rather than every element in the hierarchy.
# ──────────────────────────────────────────────────




def get_attr_number(node):
      return sum(len(element.attrib) for element in node.iter())

   

