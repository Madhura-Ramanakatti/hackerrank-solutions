# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem?isFullScreen=true
# Problem     Class 2 - Find the Torsional Angle
# Difficulty  Easy
# Subdomain   Classes
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-25, 10:06 p.m.
# ──────────────────────────────────────────────────



class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)
        

    def dot(self, no):
        return self.x * no.x + self.y * no.y +self.z * no.z

    def cross(self, no):
        
        return Points(
            self.y * no.z - self.z * no.y,
            self.z * no.x - self.x * no.z,
            self.x * no.y - self.y * no.x
            
        )
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

