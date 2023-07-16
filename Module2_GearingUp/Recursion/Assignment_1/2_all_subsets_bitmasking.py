class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        total_subsets = 2**n
        result = []
        for i in range(total_subsets):
            subset = []
            for j in range(n):
                if i>>j & 1:
                    subset.append(nums[j])
            result.append(subset)
        return result
