from typing import List


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        i, j = 0, 0
        ans = [-1, -1]

        while i < len(nums) and j < len(nums):
            if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                ans = [i, j]
                break
            j += 1
            if j == n:
                i += 1
                j = i + 1

        return ans


obj = Solution()
arr = list(map(int, input().strip().split()))
indexDifference = int(input())
valueDifference = int(input())
print(obj.findIndices(arr, indexDifference, valueDifference))
