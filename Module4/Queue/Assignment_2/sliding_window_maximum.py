from typing import List
from collections import deque


class Solution:
    def insert_at_back(self, d, idx, nums):
        while len(d) != 0 and nums[idx] > nums[d[-1]]:
            d.pop()
        d.append(idx)

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        ans = []

        for i in range(0, k):
            self.insert_at_back(d, i, nums)

        for i in range(k, len(nums)):
            ans.append(nums[d[0]])

            if d[0] == i - k:
                d.popleft()
            self.insert_at_back(d, i, nums)
        ans.append(nums[d[0]])
        return ans
