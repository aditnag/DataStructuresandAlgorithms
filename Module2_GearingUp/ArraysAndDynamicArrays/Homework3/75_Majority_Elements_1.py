# cook your dish here

class MajorityElement1:
    def find(self, ar, n):
        s = set(ar)
        for i in s:
            if ar.count(i) > n / 2:
                return i


if __name__ == '__main__':
    obj = MajorityElement1()
    n = int(input())
    ar = list(map(int, input().strip().split()))[:n]
    print(obj.find(ar, n))