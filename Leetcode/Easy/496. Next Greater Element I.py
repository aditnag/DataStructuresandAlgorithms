from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        for i in range(len(nums1)):
            p1, p2 = i, 0
            while nums1[p1] != nums2[p2]:
                p2 += 1
            p3 = p2 + 1
            while p3 < len(nums2):
                if nums2[p3] > nums2[p2]:
                    ans[i] = nums2[p3]
                    break
                p3 += 1
        return ans
