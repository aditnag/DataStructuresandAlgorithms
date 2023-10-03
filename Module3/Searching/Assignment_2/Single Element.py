# cook your dish here
def singleElement(nums, n):
    l, h = 0, n - 1
    while l <= h:
        if l == h:
            return nums[l]

        m = (l + h) // 2
        if m == 0:
            if nums[m] != nums[m + 1]:
                return nums[m]
            else:
                l = m + 1
        elif m == n - 1:
            if nums[m - 1] != nums[m]:
                return nums[m]
            else:
                h = m - 1
        else:
            if nums[m] != nums[m + 1] and nums[m] != nums[m - 1]:
                return nums[m]
            if nums[m] == nums[m + 1]:
                fo, so = m, m + 1
            else:
                fo, so = m - 1, m
            if fo % 2 == 0:
                l = m + 1
            else:
                h = m - 1


n = int(input())
arr = list(map(int, input().strip().split()))[:n]
print(singleElement(arr, n))

#
# def singleElement(nums, n):
#     if n == 1:
#         return nums[0]
#
#     l, h = 0, n - 1
#
#     while l < h:
#         m = (l + h) // 2
#
#         if m % 2 == 1:
#             m -= 1  # Ensure m is an even index
#
#         if nums[m] != nums[m + 1]:
#             h = m
#         else:
#             l = m + 2  # Skip the pair
#
#     return nums[l]
#
#
# n = int(input())
# arr = list(map(int, input().strip().split()))[:n]
# idx = singleElement(arr, n)
# print(idx)

