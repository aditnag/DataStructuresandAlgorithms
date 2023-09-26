from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                for j in range(i + 1, len(nums) - 2):
                    if j > i + 1 and nums[j] == nums[j - 1]:
                        continue
                    else:
                        rem = target - nums[i] - nums[j]
                        p1, p2 = j + 1, len(nums) - 1
                        while p1 < p2:
                            s = nums[p1] + nums[p2]
                            if s > rem:
                                p2 -= 1
                            elif s < rem:
                                p1 += 1
                            else:
                                ans.append([nums[i], nums[j], nums[p1], nums[p2]])
                                if nums[p1] == nums[p2]:
                                    break
                                x, y = nums[p1], nums[p2]
                                while p1 < p2 and nums[p1] == x:
                                    p1 += 1
                                while p1 < p2 and nums[p2] == y:
                                    p2 -= 1
        return ans
