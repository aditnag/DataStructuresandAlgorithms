class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        idx = 0
        temp = []
        result = []
        self.all_subsets(result, temp, idx, nums)
        return result

    def all_subsets(self, result, temp, idx, nums):
        if idx == len(nums):
            result.append(temp[:])
            return
        temp.append(nums[idx])
        self.all_subsets(result, temp, idx+1, nums)
        temp.pop()

        self.all_subsets(result, temp, idx+1, nums)
