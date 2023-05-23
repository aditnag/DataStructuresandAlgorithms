class Solution:
    def numberOfWays(self, n):
        # code here
        h, v = 1, 2
        for i in range(3, n+1):
            curr = h + v
            h = v
            v = curr
        return v


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.numberOfWays(N))
