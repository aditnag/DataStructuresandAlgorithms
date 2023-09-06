from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        mask = 1 << 31 
        for i in range(31, -1, -1):
            count = 0
            for j in range(len(nums)):
                if nums[j] & mask:
                    count += 1
            if count % 3 != 0:
                ans += mask
            mask >>= 1
        return ans


if __name__ == "__main__":
    ar = list(map(int, input().strip().split()))
    obj = Solution()
    print(obj.singleNumber(ar))

# -2,-2,1,1,4,1,4,4,-4,-2
