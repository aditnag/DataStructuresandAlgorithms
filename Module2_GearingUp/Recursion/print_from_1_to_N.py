class Display:
    def func(self, i, n):
        if i > n:
            return 0
        print(i)
        i += 1
        self.func(i, n)

    def main(self):
        n = int(input())
        i = 1
        self.func(i, n)


obj = Display()
obj.main()
