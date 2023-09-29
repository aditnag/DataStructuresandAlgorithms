# cook your dish here
def first(nums, n, key):
    l, h = 0, n - 1
    while l <= h:
        m = (l + h) // 2
        if nums[m] == key:
            if m == 0 or nums[m - 1] != key:
                return m
            else:
                h = m - 1
        elif nums[m] < key:
            l = m + 1
        else:
            h = m - 1
    return -1


def last(nums, n, key):
    l, h = 0, n - 1
    while l <= h:
        m = (l + h) // 2
        if nums[m] == key:
            if m == n - 1 or nums[m + 1] != key:
                return m
            else:
                l = m + 1
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
    first_index = first(nums, n, target)
    if first_index != -1:
        last_index = last(nums, n, target)
        print(f"{last_index - first_index + 1}")
    else:
        print(0)
