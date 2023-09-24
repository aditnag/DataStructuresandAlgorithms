class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i2 = i3 = i5 = 0
        for _ in range(1, n):
            ugly2, ugly3, ugly5 = nums[i2] * 2, nums[i3] * 3, nums[i5] * 5
            ugly = min(ugly2, ugly3, ugly5)
            nums.append(ugly)
            if ugly == ugly2:
                i2 += 1
            if ugly == ugly3:
                i3 += 1
            if ugly == ugly5:
                i5 += 1
        return nums[-1]
