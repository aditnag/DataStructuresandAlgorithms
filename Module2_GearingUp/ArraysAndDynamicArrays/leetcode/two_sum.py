from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # approch 1
        # mp = {}
        # for idx, num in enumerate(nums):
        #     mp[num] = idx
        # for i in range(len(nums)):
        #     compliment = target - nums[i]
        #     if compliment in mp and mp[compliment] != i:
        #         return [mp[compliment], i]

        # return []

        # approch 2
        mp = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in mp:
                return [mp[compliment], i]
            mp[num] = i

        return []


if __name__ == "__main__":
    solution = Solution()
    nums = list(map(int, input().strip().split()))
    target = int(input())
    result = solution.twoSum(nums, target)
    print(result)  # Output: [0, 1]
