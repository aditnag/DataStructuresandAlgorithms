from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                p1, p2 = i + 1, len(nums) - 1
                rem = -1 * nums[i]
                while p1 < p2:
                    if nums[p1] + nums[p2] < rem:
                        p1 += 1
                    elif nums[p1] + nums[p2] > rem:
                        p2 -= 1
                    else:
                        res.append([nums[i], nums[p1], nums[p2]])
                        if nums[p1] == nums[p2]:
                            break
                        else:
                            x, y = nums[p1], nums[p2]
                            while p1 < p2 and x == nums[p1]:
                                p1 += 1
                            while p1 < p2 and y == nums[p2]:
                                p2 -= 1
        return res


# Create an instance of the Solution class
sol = Solution()

# Example input
nums = list(map(int, input().strip().split()))

# Call the threeSum method to find triplets and store the result
result = sol.threeSum(nums)

# Print the result
print(result)
