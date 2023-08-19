# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isPerfect(self, root: Optional[TreeNode]):
        temp = root
        height_left = 0
        while temp:
            height_left += 1
            temp = temp.left

        height_right = 0
        temp = root
        while temp:
            height_right += 1
            temp = temp.right
        return height_left == height_right, height_left

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        count = 1
        lst, height_left = self.isPerfect(root.left)
        rst, height_right = self.isPerfect(root.right)

        if lst:
            count += 2 ** height_left - 1
        else:
            count += self.countNodes(root.left)

        if rst:
            count += 2 ** height_right - 1
        else:
            count += self.countNodes(root.right)
        return count
