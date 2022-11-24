# cook your dish here
from math import inf


class OptimizedTime:
    def main(self):
        n = int(input())
        ar = list(map(int, input().strip().split()))[:n]
        smax = ar.copy()
        for i in range(n - 2, - 1, -1):
            smax[i] = max(smax[i + 1], smax[i])
        ans = -inf
        for i in range(n - 1):
            ans = max(ans, smax[i + 1] - ar[i])

        if ans <= 0:
            return 0
        else:
            return ans


obj = OptimizedTime()
print(obj.main())
