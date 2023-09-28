from typing import List


class Solution:
    def backtrack(self, nums, i, ans):
        if i == len(nums) - 1:
            ans.append(nums[:])
            return
        for idx in range(i, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.backtrack(nums, i + 1, ans)
            nums[idx], nums[i] = nums[i], nums[idx]

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        i = 0
        self.backtrack(nums, i, ans)
        return ans

