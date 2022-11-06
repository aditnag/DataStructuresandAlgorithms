# cook your dish here

class RainWaterTrapping:
    def main(self):
        n = int(input())
        h = list(map(int, input().strip().split()))[:n]

        pmax = h.copy()
        for i in range(1, n):
            pmax[i] = max(pmax[i - 1], h[i])

        smax = h.copy()
        for i in range(n - 2, -1, -1):
            smax[i] = max(smax[i + 1], h[i])

        amount = 0
        for i in range(1, n - 1):
            decidingFactor = min(pmax[i - 1], smax[i + 1])
            if h[i] < decidingFactor:
                amount += decidingFactor - h[i]

        print(amount)


obj = RainWaterTrapping()
obj.main()
