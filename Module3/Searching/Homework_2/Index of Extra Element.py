# cook your dish here
def findDiff(num1, num2):
    l, h = 0, len(num2) - 1
    idx = len(num2)
    while l <= h:
        m = (l + h) // 2
        if num1[m] == num2[m]:
            l = m + 1
        else:
            idx = m
            h = m - 1
    return idx


n = int(input())
arr1 = list(map(int, input().strip().split()))[:n]
arr2 = list(map(int, input().strip().split()))[:n - 1]
print(findDiff(arr1, arr2))
