import sys
from typing import List
from collections import deque


class Solution:
    def nextSmaller(self, ht, s):
        nse = [0] * len(ht)
        s.append(0)
        for i in range(1, len(ht)):
            while len(s) != 0 and ht[i] < ht[s[-1]]:
                nse[s.pop()] = i
            s.append(i)

        while len(s) != 0:
            nse[s.pop()] = len(ht)

        return nse

    def previousSmaller(self, ht, s):
        pse = [0] * len(ht)
        s.append(len(ht) - 1)
        for i in range(len(ht) - 2, -1, -1):
            while len(s) != 0 and ht[i] < ht[s[-1]]:
                pse[s.pop()] = i
            s.append(i)

        while len(s) != 0:
            pse[s.pop()] = -1

        return pse

    def largestRectangleArea(self, heights: List[int]) -> int:
        maximum = -sys.maxsize
        nse = self.nextSmaller(heights, deque())
        pse = self.previousSmaller(heights, deque())
        for i in range(len(heights)):
            maximum = max(maximum, (nse[i] - pse[i] - 1) * heights[i])

        return maximum
