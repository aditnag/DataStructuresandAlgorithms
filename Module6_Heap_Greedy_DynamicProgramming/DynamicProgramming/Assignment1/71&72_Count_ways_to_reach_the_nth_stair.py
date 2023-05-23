class Solution:
    # Function to count number of ways to reach the nth stair.
    def bottom_top_approach(self, n):

        # code here
        f, s = 1, 2
        if n == 1 or n == 2:
            return n
        for i in range(3, n + 1):
            curr = f + s
            f = s
            s = curr
        return s

    def top_bottom_approach(self, n, ans):
        if n == 0:
            return 1
        if n < 0:
            return 0
        if ans[n] != -1:
            return ans[n]
        ans[n] = self.top_bottom_approach(n - 1, ans) + self.top_bottom_approach(n - 2, ans)
        return ans[n]


if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        ans = [-1] * (n + 1)
        obj = Solution()
        print(obj.top_bottom_approach(n, ans))
        print(obj.bottom_top_approach(n))
        t -= 1
