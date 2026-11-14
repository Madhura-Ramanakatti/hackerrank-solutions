# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/xml-1-find-the-score/problem?isFullScreen=true
# Problem     XML 1 - Find the Score
# Difficulty  Easy
# Subdomain   XML
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-14, 08:38 a.m.
# ──────────────────────────────────────────────────




def get_attr_number(node):
      return sum(len(element.attrib) for element in node.iter())

   

