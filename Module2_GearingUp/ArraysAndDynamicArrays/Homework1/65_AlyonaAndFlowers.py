# cook your dish here
from math import inf


class AlyonaandFlowers:
    def main(self):
        n, m = map(int, input().strip().split())
        ar = list(map(int, input().strip().split()))[:n]
        psum = ar.copy()
        for i in range(1, n):
            psum[i] = psum[i - 1] + ar[i]

        max_score = 0
        while m:
            l, r = map(int, input().strip().split())
            if l - 1 <= 0:
                ans = psum[r - 1]
            else:
                ans = psum[r - 1] - psum[l - 2]
            if ans > 0:
                max_score += ans
            m -= 1

        print(max_score)


obj = AlyonaandFlowers()
obj.main()
