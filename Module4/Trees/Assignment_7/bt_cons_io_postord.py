# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def build(self, i1, j1, i2, j2):
        if i1 > j1:
            return None
        root = TreeNode(self.postorder[j1])
        i = 0
        for i in range(i2, j2 + 1):
            if self.inorder[i] == self.postorder[j1]:
                break
        root.left = self.build(i1, i1 + i - 1 - i2, i2, i - 1)
        root.right = self.build(i1+i-i2, j1-1,i+1, j2)
        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.inorder = inorder
        self.postorder = postorder
        i1 = 0
        j1 = len(postorder) - 1
        i2 = 0
        j2 = len(inorder) - 1
        return self.build(i1, j1, i2, j2)
