from typing import List


class Solution:
    def backtrack(self, nums, idx, ans):
        if idx == len(nums):
            ans.append(nums[:])
            return
        mp = {}
        for i in range(idx, len(nums)):
            if nums[i] not in mp:
                nums[idx], nums[i] = nums[i], nums[idx]
                self.backtrack(nums, idx + 1, ans)
                nums[idx], nums[i] = nums[i], nums[idx]
            mp[nums[i]] = 1

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        idx = 0
        ans = []
        self.backtrack(nums, idx, ans)
        return ans
