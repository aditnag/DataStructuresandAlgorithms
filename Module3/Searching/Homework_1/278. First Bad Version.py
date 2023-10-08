# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, h = 1, n
        while l <= h:
            m = (l + h) // 2
            if isBadVersion(l):
                return l
            elif isBadVersion(m):
                if not isBadVersion(m - 1):
                    return m
                else:
                    h = m - 1
            else:
                l = m + 1
