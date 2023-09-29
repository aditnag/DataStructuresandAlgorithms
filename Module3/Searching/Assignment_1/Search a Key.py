# cook your dish here
def bs(nums, n, key):
    l, h = 0, n - 1
    while l <= h:
        m = (l + h) // 2
        if nums[m] == key:
            return m
        elif nums[m] < key:
            l = m + 1
        else:
            h = m - 1
    return -1


n = int(input())
nums = list(map(int, input().strip().split()))[:n]
t = int(input())
for _ in range(t):
    target = int(input())
    print(bs(nums, n, target))
