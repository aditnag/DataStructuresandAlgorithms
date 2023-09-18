from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        psum = 0
        mp = {}
        mp[0] = 1
        count = 0
        for i in range(len(nums)):
            psum += nums[i]
            modulus = (psum % k + k) % k
            if modulus in mp:
                count += mp[modulus]
                mp[modulus] += 1
            else:
                mp[modulus] = 1

        return count
