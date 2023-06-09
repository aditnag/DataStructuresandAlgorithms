# cook your dish here

class ArrayNesting:
    def findCount(self, nums, n):
        count = 0
        ar = []
        index = 0
        for i in range(n):
            if nums[index] not in ar:
                ar.append(nums[index])
                index = nums[index]
                count += 1
        print(count)


if __name__ == '__main__':
    obj = ArrayNesting()
    n = int(input())
    nums = list(map(int, input().strip().split()))[:n]
    obj.findCount(nums, n)
