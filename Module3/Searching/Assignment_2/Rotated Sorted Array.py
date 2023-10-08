# cook your dish here
def rotatedSortedArr(nums, target):
    n = len(nums) - 1
    l, h = 0, n
    while l <= h:
        m = (l + h) // 2
        if nums[m] == target:
            return m
        if nums[l] <= nums[m]:
            if nums[l] <= target < nums[m]:
                h = m - 1
            else:
                l = m + 1
        else:
            if nums[m] < target <= nums[n]:
                l = m + 1
            else:
                h = m - 1
    return -1


n = int(input())
arr = list(map(int, input().strip().split()))[:n]
t = int(input())
for _ in range(t):
    target = int(input())
    print(rotatedSortedArr(arr, target))

# 5 6 7 1 2 3 4
# 0 1 2 3 4 5 6
