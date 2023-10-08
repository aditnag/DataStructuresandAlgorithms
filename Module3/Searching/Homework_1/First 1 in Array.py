# cook your dish here
def findOne(nums):
    n = len(nums) - 1
    l, h = 0, n
    while l <= h:
        if nums[l] == 1:
            return l + 1
        m = (l + h) // 2
        if nums[m] == 1 and nums[m - 1] == 0:
            return m + 1
        else:
            if nums[m] == 0:
                l = m + 1
            else:
                h = m - 1
    return -1


n = int(input())
arr = list(map(int, input().strip().split()))[:n]
print(findOne(arr))
