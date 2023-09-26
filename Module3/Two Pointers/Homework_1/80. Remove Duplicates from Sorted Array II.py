from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert_ptr = count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            if count <= 2:
                nums[insert_ptr] = nums[i]
                insert_ptr += 1
        return insert_ptr
