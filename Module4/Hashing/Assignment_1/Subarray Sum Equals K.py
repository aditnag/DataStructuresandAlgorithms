from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        psum = 0
        count = 0
        mp = {}
        mp[0] = 1
        for i in range(len(nums)):
            psum += nums[i]

            if psum - k in mp:
                count += mp[psum - k]

            if psum in mp:
                mp[psum] += 1
            else:
                mp[psum] = 1
        return count
