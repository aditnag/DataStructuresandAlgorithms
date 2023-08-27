# Construct Binary Tree from Preorder and Inorder Traversal
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def build(self, i1, j1, i2, j2):
    #     if i1 > j1:
    #         return None
    #     root = TreeNode(self.preorder[i1])
    #     i = 0
    #     for i in range(i2, j2 + 1):
    #         if self.inorder[i] == self.preorder[i1]:
    #             break
    #     root.left = self.build(i1 + 1, i1 - i2 + i, i2, i - 1)
    #     root.right = self.build(i1 + i - i2 + 1, j1, i + 1, j2)
    #
    #     return root

    def build(self, i1, j1, i2, j2):
        if i1 > j1:
            return None
        root = TreeNode(self.preorder[i1])
        mp = {val: idx for idx, val in enumerate(self.inorder)}
        i = mp[self.preorder[i1]]
        root.left = self.build(i1 + 1, i1 - i2 + i, i2, i - 1)
        root.right = self.build(i1 + i - i2 + 1, j1, i + 1, j2)

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        self.inorder = inorder
        i1 = 0
        j1 = len(preorder) - 1
        i2 = 0
        j2 = len(inorder) - 1
        return self.build(i1, j1, i2, j2)
