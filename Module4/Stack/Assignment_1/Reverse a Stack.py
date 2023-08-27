# cook your dish here
class ReverseStack:
    def pushBottom(self, l, x):
        if len(l) == 0:
            l.append(x)
            return
        y = l.pop()
        self.pushBottom(l, x)
        l.append(y)

    def reverseStack(self, l):
        if len(l) == 0:
            return l
        y = l.pop()
        self.reverseStack(l)
        self.pushBottom(l, y)


if __name__ == "__main__":
    n = int(input())
    l = list(map(int, input().strip().split()))[:n]
    obj = ReverseStack()
    obj.reverseStack(l)
    print(l)
