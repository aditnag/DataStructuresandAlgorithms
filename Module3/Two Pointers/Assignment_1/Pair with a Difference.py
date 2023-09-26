# cook your dish here
def pairDiff(nums, k):
    nums.sort()
    n = len(nums)
    i = 0
    j = 1
    while j < n:
        diff = nums[j] - nums[i]
        if diff == k:
            return True
        elif diff < k:
            j += 1
        else:
            i += 1
        if i == j:
            j += 1


n, k = map(int, input().split())
arr = list(map(int, input().strip().split()))[:n]
if pairDiff(arr, k):
    print("Yes")
else:
    print("No")
