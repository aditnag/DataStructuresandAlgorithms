from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # maxsofar = maxend = candidates[0]
        # i = 1
        # count = 1
        # while i < len(candidates):
        #     maxend = maxend & candidates[i]
        #     if maxend > 0:
        #         maxsofar = maxend
        #         count += 1
        #     else:
        #         maxend = maxsofar
        #     i += 1
        # return count

        ans = 0
        for bit in range(32):
            mask = 1 << (31 - bit)
            count = 0
            for i in range(len(candidates)):
                if candidates[i] & mask > 0:
                    count += 1
            ans = max(ans, count)
        return ans
