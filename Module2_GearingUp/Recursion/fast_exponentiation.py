# T.C = O(log K)
#            2
# S.C = O(log K)
#            2

class FastExponentiation:
    def fastexp(self, n: int, k: int):
        if k == 0:
            return 1
        x = self.fastexp(n, k // 2)
        if k % 2 == 0:
            return x * x
        return x * x * n

    def main(self):
        n, k = map(int, input().strip().split())
        result = self.fastexp(n, k)
        print(result)


obj = FastExponentiation()
obj.main()
