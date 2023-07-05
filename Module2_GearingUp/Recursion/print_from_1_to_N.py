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

    def func_reverse_straight(self, n):
        if n < 1:
            return 0
        self.func_reverse_straight(n - 1)
        print(n)

    def main(self):
        n = int(input())
        i = 1
        self.func(i, n)
        print()
        self.func_reverse(n)
        print()
        self.func_reverse_straight(n)


obj = Display()
obj.main()
