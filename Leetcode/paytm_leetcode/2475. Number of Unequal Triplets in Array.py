from collections import Counter
from typing import List


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        # count = 0
        # for i in range(len(nums)-2):
        #     for j in range(i, len(nums)-1):
        #         for k in range(j, len(nums)):
        #             if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
        #                 count += 1
        # return count

        res = 0
        c = Counter(nums)

        left, right = 0, len(nums)

        for _, freq in c.items():
            right -= freq
            res += left * freq * right
            left += freq

        return res
