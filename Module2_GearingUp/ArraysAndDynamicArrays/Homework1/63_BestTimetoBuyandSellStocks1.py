# cook your dish here
from math import inf


class OptimizedTime:
    def suffixmax(self, arr: list, a: int):
        for i in range(len(arr) - 2, a - 1, -1):
            arr[i] = max(arr[i + 1], arr[i])

        for i in range(a, len(arr)):
            return arr[i]

    def main(self):
        n = int(input())
        ar = list(map(int, input().strip().split()))[:n]
        smax = ar.copy()
        ans = -inf
        for i in range(n - 1):
            ans = max(ans, self.suffixmax(smax, i + 1) - ar[i])

        if ans <= 0:
            return 0
        else:
            return ans


obj = OptimizedTime()
print(obj.main())
