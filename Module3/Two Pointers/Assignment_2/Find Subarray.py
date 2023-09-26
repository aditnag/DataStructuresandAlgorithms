# cook your dish here
def findSubarrSum(nums, s):
    ptri = ptrj = 0
    curr = nums[0]
    while ptrj < len(nums):
        if curr > s:
            curr -= nums[ptri]
            ptri += 1
            if ptri > ptrj:
                ptrj += 1
                if ptrj < len(nums):
                    curr = nums[ptrj]
        elif curr < s:
            ptrj += 1
            if ptrj < len(nums):
                curr += nums[ptrj]
        else:
            return ptri + 1, ptrj + 1
    return -1


t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    arr = list(map(int, input().strip().split()))[:n]
    res = findSubarrSum(arr, s)
    if res != -1:
        print(f"{res[0]} {res[1]}")
    else:
        print(res)
