# cook your dish here

class FirstMissingPositive:
    def find_num(self, ar, n):
        for i in range(n):
            while 1 <= ar[i] <= n and ar[i] != ar[ar[i] - 1]:
                temp = ar[i]
                ar[i] = ar[ar[i] - 1]
                ar[temp - 1] = temp

        for i in range(len(ar)):
            if ar[i] != i + 1:
                return i + 1

        return n + 1


if __name__ == '__main__':
    obj = FirstMissingPositive()
    t = int(input())
    while t:
        n = int(input())
        ar = list(map(int, input().strip().split()))[:n]
        print(obj.find_num(ar, n))
        t -= 1
