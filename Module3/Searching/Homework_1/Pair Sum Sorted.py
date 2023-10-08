# cook your dish here
def pairSum(nums, key):
    nums.sort()
    l, h = 0, len(nums) - 1
    while l <= h:
        localsum = nums[l] + nums[h]
        if localsum == key:
            return l + 1, h + 1
        elif localsum > key:
            h = h - 1
        else:
            l = l + 1


n = int(input())
nums = list(map(int, input().strip().split()))[:n]
key = int(input())
i, j = pairSum(nums, key)
print(f"{i} {j}")
