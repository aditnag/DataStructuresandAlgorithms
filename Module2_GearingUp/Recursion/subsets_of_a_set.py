class SetOperation:
    def subset(self, temp: list, idx, ar):
        if idx == len(ar):
            print(temp)
            return
        # Taking the element at ar[idx]
        temp.append(ar[idx])
        self.subset(temp, idx + 1, ar)
        # The operation is necessary to remove the last element from the temp list after the recursive call to subset.
        temp.pop()

        # Leaving the element at ar[idx]
        self.subset(temp, idx + 1, ar)

    def main(self):
        n = int(input())
        ar = list(map(int, input().strip().split()))[:n]
        idx = 0
        temp = []
        self.subset(temp, idx, ar)


obj = SetOperation()
obj.main()
