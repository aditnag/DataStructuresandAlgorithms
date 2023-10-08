# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def get(self, index: int) -> int:
        pass

    def length(self) -> int:
        pass


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        l, h = 1, n - 2
        while l != h:
            m = (l + h) // 2
            if mountain_arr.get(m) < mountain_arr.get(m + 1):
                l = m + 1
            else:
                h = m
        peak = l

        # target in increasing monotonic fn
        l, h = 0, peak
        while l != h:
            m = (l + h) // 2
            if mountain_arr.get(m) < target:
                l = m + 1
            else:
                h = m
        if mountain_arr.get(l) == target:
            return l

        # target in decreasing monotonic fn
        l, h = peak + 1, n - 1
        while l != h:
            m = (l + h) // 2
            if mountain_arr.get(m) > target:
                l = m + 1
            else:
                h = m
        if mountain_arr.get(l) == target:
            return l

        return -1
