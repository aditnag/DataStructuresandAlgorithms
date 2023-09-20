from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = {}
        ans = 0
        for i in range(len(nums)):
            if nums[i] not in mp:
                ls = 0
                rs = 0
                if nums[i] - 1 in mp:
                    ls = mp[nums[i] - 1]
                if nums[i] + 1 in mp:
                    rs = mp[nums[i] + 1]
                ans = max(ans, 1 + ls + rs)
                mp[nums[i]] = 1 + ls + rs
                mp[nums[i] - ls] = 1 + ls + rs
                mp[nums[i] + rs] = 1 + ls + rs
            else:
                continue
        return ans
