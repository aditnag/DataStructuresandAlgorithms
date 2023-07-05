class Display:
    def func(self, i, n):
        if i > n:
            return 0
        print(i)
        i += 1
        self.func(i, n)

    def func_reverse(self, n):
        if n < 1:
            return 0
        print(n)
        self.func_reverse(n - 1)

    def main(self):
        n = int(input())
        i = 1
        self.func(i, n)
        print()
        self.func_reverse(n)


obj = Display()
obj.main()
