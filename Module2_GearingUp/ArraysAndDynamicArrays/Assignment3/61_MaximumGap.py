# cook your dish here
from math import ceil
from sys import maxsize


class MaximumGap:
    def main(self):
        t = int(input())
        while t:
            n = int(input())
            ar = list(map(int, input().strip().split()))[:n]

            min_num = ar[0]
            max_num = ar[0]

            for i in range(n):
                min_num = min(min_num, ar[i])
                max_num = max(max_num, ar[i])

            if n < 2:
                print(0)

            elif min_num == max_num:
                print(0)

            else:
                gap = ceil((max_num - min_num) / (n - 1))

                ar_min = [maxsize] * n
                ar_max = [-maxsize] * n

                for i in range(n):
                    bucket = ceil((ar[i] - min_num) / gap)
                    ar_min[bucket] = min(ar_min[bucket], ar[i])
                    ar_max[bucket] = max(ar_max[bucket], ar[i])

                ans = -maxsize
                prev = -maxsize
                for i in range(n):
                    if ar_min[i] == maxsize:
                        continue
                    if prev == -maxsize:
                        prev = ar_max[i]
                    else:
                        ans = max(ans, ar_min[i] - prev)
                        prev = ar_max[i]

                print(ans)
            t -= 1


obj = MaximumGap()
obj.main()
