class Solution:
    def countBits(self, n: int) -> List[int]:
        # mask = 1 << 31
        # ans = [0]
        # for i in range(31, -1, -1):
        #     count = 0
        #     for j in range(n+1):
        #         if mask & j:
        #             count += 1
        #     ans.append(count)
        #     mask >>= 1
        # return ans

        # ans = []
        # for i in range(n+1):
        #     mask = 1
        #     count = 0
        #     while mask <= i:
        #         if (i & mask):
        #             count += 1
        #         mask <<= 1
        #     ans.append(count)
        # return ans
        ans = [0]
        for i in range(1, n + 1):
            prev = i >> 1
            ans.append(ans[prev] + (i & 1))
        return ans







