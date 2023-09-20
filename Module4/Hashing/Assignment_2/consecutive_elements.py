from sys import maxsize


def consecutive(arr):
    low = min(arr)
    high = max(arr)

    for num in range(low, high + 1):
        if num not in arr:
            return "No"

    if len(set(arr)) == len(arr):
        return "Yes"
    else:
        return "No"


t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))[:n]
    result = consecutive(arr)
    print(result)
