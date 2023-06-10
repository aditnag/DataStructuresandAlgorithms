# cook your dish here

class EquallyDistributedGroups:
    def gcd(self, a, b):
        maxm = max(a, b)
        minm = min(a, b)
        while maxm % minm != 0:
            temp = maxm
            maxm = minm
            minm = temp % minm
        return minm

    def find(self, ar):
        dic = {}
        for i in range(len(ar)):
            if ar[i] not in dic.keys():
                dic[ar[i]] = 1
            else:
                dic[ar[i]] += 1
        value_list = list(dic.values())
        if len(value_list) == 1 and value_list[0] >= 2:
            print("true")
        else:
            hcf = self.gcd(value_list[0], value_list[1])
            for i in range(2, len(value_list)):
                hcf = self.gcd(hcf, value_list[i])

            if hcf > 1:
                print("true")
            else:
                print("false")


if __name__ == '__main__':
    obj = EquallyDistributedGroups()
    t = int(input())
    while t:
        n = int(input())
        arr_num = list(map(int, input().strip().split()))[:n]
        obj.find(arr_num)
        t -= 1
