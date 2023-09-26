from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        itr = 0
        jtr = len(height) - 1
        area = 0
        while itr < jtr:
            area = max(area, min(height[itr], height[jtr]) * (jtr - itr))
            if height[itr] <= height[jtr]:
                itr += 1
            else:
                jtr -= 1
        return area
