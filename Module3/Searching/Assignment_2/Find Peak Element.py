from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, h = 0, n - 1
        while l <= h:
            m = (l + h) // 2
            if l == h:
                return l
            if m == 0:
                if nums[m] > nums[m + 1]:
                    return m
                else:
                    l = m + 1
            elif m == n - 1:
                if nums[m] > nums[m - 1]:
                    return m
                else:
                    h = m - 1
            else:
                if nums[m - 1] < nums[m] > nums[m + 1]:
                    return m
                elif nums[m] < nums[m - 1]:
                    h = m - 1
                else:
                    l = m + 1
