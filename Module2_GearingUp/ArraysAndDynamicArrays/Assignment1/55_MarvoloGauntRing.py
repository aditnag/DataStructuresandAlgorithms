# cook your dish here
import sys


class MarvoloGauntRing:
    def main(self):
        n, p, q, r = map(int, input().strip().split())
        ar = list(map(int, input().strip().split()))[:n]

        pmax = ar.copy()
        pmax[0] = p * ar[0]
        for i in range(1, n):
            pmax[i] = max(pmax[i - 1], p * ar[i])

        smax = ar.copy()
        smax[n - 1] = r * ar[n - 1]
        for i in range(n - 2, -1, -1):
            smax[i] = max(smax[i + 1], r * ar[i])

        ans = -sys.maxsize
        for i in range(0, n):
            ans = max(ans, pmax[i] + q * ar[i] + smax[i])

        print(ans)


obj = MarvoloGauntRing()
obj.main()
