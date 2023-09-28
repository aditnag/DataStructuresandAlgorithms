class Solution:
    def backtrack(self, idx, nums, res):
        if idx == len(nums) - 1:
            res.append("".join(nums))
            return
        for i in range(idx, len(nums)):
            # right rotate
            nums[idx], nums[i] = nums[i], nums[idx]
            self.backtrack(idx + 1, nums, res)
            # left rotate
            nums[idx], nums[i] = nums[i], nums[idx]

    def getPermutation(self, n: int, k: int) -> str:
        ans = []
        idx = 0
        nums = [str(i) for i in range(1, n + 1)]
        self.backtrack(idx, nums, ans)
        ans.sort()
        return ans[k - 1]
