class LexicographicSubset:
    def lexisubset(self, temp: list, idx: int, ar, n):
        print(temp, end=" ")
        if idx == n:
            return
        for j in range(idx, n):
            temp.append(ar[j])
            self.lexisubset(temp, j + 1, ar, n)
            temp.pop()

    def main(self):
        n = int(input())
        ar = list(map(int, input().strip().split()))[:n]
        idx = 0
        temp = []
        self.lexisubset(temp, idx, ar, n)


obj = LexicographicSubset()
obj.main()
