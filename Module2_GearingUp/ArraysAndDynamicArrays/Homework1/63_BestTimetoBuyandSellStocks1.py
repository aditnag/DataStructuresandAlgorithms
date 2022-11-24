# cook your dish here
from math import inf


class OptimizedTime:
    def prefixmax(self, arr: list, a: int):
        maxnum = -inf
        maxarr = arr.copy()
        for i in range(a, len(arr)):
            maxnum = max(maxnum, maxarr[i])
        return maxnum

    def main(self):
        n = int(input())
        ar = list(map(int, input().strip().split()))[:n]
        ans = ar[1] - ar[0]
        for i in range(n - 1):
            ans = max(ans, self.prefixmax(ar, i + 1) - ar[i])

        if ans <= 0:
            return 0
        else:
            return ans


obj = OptimizedTime()
print(obj.main())
