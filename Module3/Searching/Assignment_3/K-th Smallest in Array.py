# cook your dish here
def func(nums, x):
    c = 0
    for num in nums:
        if num <= x:
            c += 1
    return c


def kthsmallestelement(nums, n, k):
    l, h = min(nums), max(nums)
    while l <= h:
        m = (l + h) // 2
        count = func(nums, m)
        if count < k:
            l = m + 1
        else:
            c1 = func(nums, m - 1)
            if c1 < k:
                return m
            else:
                h = m - 1


n = int(input())
arr = list(map(int, input().strip().split()))[:n]
k = int(input())
ele = kthsmallestelement(arr, n, k)
print(ele)
