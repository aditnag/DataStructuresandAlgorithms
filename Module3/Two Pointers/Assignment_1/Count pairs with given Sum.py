# cook your dish here
def countSum(nums, k):
    nums.sort()
    n = len(nums)
    if n < 1:
        return 0
    i = 0
    j = n - 1
    ans = 0
    while i < j:
        curr = nums[i] + nums[j]
        if curr > k:
            j -= 1
        elif curr < k:
            i -= 1
        else:
            if nums[i] == nums[j]:
                l = j - i + 1
                ans += (l * (l - 1)) // 2
                break
            v1 = nums[i]
            v2 = nums[j]
            c1 = c2 = 0
            while v1 == nums[i]:
                c1 += 1
                i += 1
            while v2 == nums[j]:
                c2 += 1
                j -= 1
            ans += c1 * c2
    return ans


n, k = map(int, input().split())
arr = list(map(int, input().strip().split()))[:n]
print(countSum(arr, k))
