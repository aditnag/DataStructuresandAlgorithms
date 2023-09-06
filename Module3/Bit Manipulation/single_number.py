from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            count = 0
            for num in nums:
                # Count the number of set bits at position i in all numbers
                count += (num >> i) & 1

            # If the count is not a multiple of 3, set the ith bit in the answer
            if count % 3 != 0:
                ans |= (1 << i)

        # If the result is negative (i.e., the most significant bit is set),
        # convert it to a 32-bit signed integer
        if ans >= 2 ** 31:
            ans -= 2 ** 32

        return ans
