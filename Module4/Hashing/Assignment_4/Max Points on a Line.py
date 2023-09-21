from math import gcd
from typing import List


class Solution:
    def standardize(self, n, d):
        if n == 0:
            d = 1
        elif d == 0:
            n = 1
        elif (n < 0 and d < 0) or d < 0:
            n *= -1
            d *= -1
        return n, d

    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        ans = 1
        # mp ={}
        for i in range(len(points)):
            mp = {}
            olp = 0
            maxlocal = 0
            for j in range(i + 1, len(points)):
                if points[i] == points[j]:
                    olp += 1
                else:
                    dx = points[j][0] - points[i][0]
                    dy = points[j][1] - points[i][1]
                    g = gcd(dx, dy)
                    slope = (dx // g, dy // g)
                    slope = self.standardize(slope[0], slope[1])
                    if slope in mp:
                        mp[slope] += 1
                    else:
                        mp[slope] = 1
                    maxlocal = max(maxlocal, mp[slope])
            ans = max(ans, maxlocal + olp + 1)
        return ans
