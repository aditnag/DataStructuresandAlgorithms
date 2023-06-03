# # cook your dish here

class MajorityElement2:
    def find(self, nums, n):
        s = set(nums)
        ar = []
        for i in s:
            if nums.count(i) > n / 3:
                ar.append(i)
        ar.sort()
        if len(ar) == 0:
            print("-1")
        else:
            for i in ar:
                print(i, end=" ")
            print(" ")


if __name__ == '__main__':
    obj = MajorityElement2()
    t = int(input())
    while t:
        n = int(input())
        nums = list(map(int, input().strip().split()))[:n]
        obj.find(nums, n)
        t -= 1
