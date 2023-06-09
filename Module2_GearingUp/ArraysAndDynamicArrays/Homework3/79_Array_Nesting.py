# cook your dish here

class ArrayNesting:
    def findCount(self, nums):
        ans = 0
        for num in nums:
            count = 0
            while nums[num] != -1:
                count += 1
                temp = num
                num = nums[num]
                nums[temp] = -1
            ans = max(ans, count)
        print(ans)


if __name__ == '__main__':
    obj = ArrayNesting()
    n = int(input())
    nums = list(map(int, input().strip().split()))[:n]
    obj.findCount(nums)
