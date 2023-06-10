class LCMChallenge:
    def findlcm(self, a, b):
        minm = max(a, b)
        maxm = min(a, b)
        while maxm % minm != 0:
            temp = maxm
            maxm = minm
            minm = temp % minm
        return (a * b) // minm

    def findMaxLCM(self, n):
        ar = []
        for i in range(n, 0, -1):
            if n % 2 == 0:
                ar.append(n)
                ar.append(n - 1)
                ar.append(n - 3)
            else:
                ar.append(n)
                ar.append(n - 1)
                ar.append(n - 2)

        lcm = self.findlcm(ar[0], ar[1])
        lcm = self.findlcm(lcm, ar[2])
        print(lcm)


if __name__ == '__main__':
    obj = LCMChallenge()
    n = int(input())
    obj.findMaxLCM(n)
