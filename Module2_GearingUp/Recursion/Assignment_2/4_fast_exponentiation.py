class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        val = float(self.myPow(x, n // 2))
        if n % 2 == 0:
            return val * val
        else:
            return val * val * x


obj = Solution()
x = float(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))
result = obj.myPow(x, n)
print(result)
