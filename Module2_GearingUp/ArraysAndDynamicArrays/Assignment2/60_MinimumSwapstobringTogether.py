# cook your dish here
import sys


class MinimumSwapstobringTogether:
    def main(self):
        n, k = map(int, input().strip().split())
        arr = list(map(int, input().strip().split()))[:n]
        ans = sys.maxsize
        countLegatElements = 0
        max_count = 0
        # count of elements <= k
        for i in range(n):
            if arr[i] <= k:
                countLegatElements += 1

        for i in range(countLegatElements):
            if arr[i] <= k:
                max_count += 1
        if max_count == n:
            print(0)
        else:
            for i in range(countLegatElements, n):
                ans = min(ans, countLegatElements - max_count)
                if arr[i - countLegatElements] <= k:
                    max_count -= 1
                if arr[i] <= k:
                    max_count += 1

            print(ans)


obj = MinimumSwapstobringTogether()
obj.main()
