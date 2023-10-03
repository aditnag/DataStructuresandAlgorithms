# cook your dish here
def reapeatedElements(nums, n):
    l, h = 0, n - 1
    while l <= h:
        m = (l + h) // 2
        if nums[m] == m:
            h = m - 1
        else:
            if nums[m] == nums[m + 1]:
                return nums[m]
            else:
                l = m + 1


n = int(input())
arr = list(map(int, input().strip().split()))[:n]
print(reapeatedElements(arr, n))
