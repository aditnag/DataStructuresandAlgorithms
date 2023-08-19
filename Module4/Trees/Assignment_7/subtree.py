# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, root, preorder_list):
        if root is None:
            preorder_list.append("N")
            return
        preorder_list.append(root.val)
        if root.left:
            self.traverse(root.left, preorder_list)
        if root.right:
            self.traverse(root.right, preorder_list)
        return preorder_list

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        pre_root = []
        pre_subroot = []

        self.traverse(root, pre_root)
        self.traverse(subRoot, pre_subroot)

        if len(pre_root) < len(pre_subroot):
            return False

        pre_subroot_str = ",".join(map(str, pre_subroot))
        pre_root_str = ",".join(map(str, pre_root))

        return pre_subroot_str in pre_root_str
