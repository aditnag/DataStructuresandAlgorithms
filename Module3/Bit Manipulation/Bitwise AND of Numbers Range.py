class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        mask = 1 << 31
        ans = 0
        while mask:
            if (left & mask) == (right & mask):
                if (left & mask):
                    ans += mask
                mask >>= 1
            else:
                break
        return ans
