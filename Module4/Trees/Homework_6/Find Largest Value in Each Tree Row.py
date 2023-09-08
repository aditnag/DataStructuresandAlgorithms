from collections import deque
from sys import maxsize
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        ans = []
        while len(q):
            max_ele = []
            size = len(q)
            while size:
                if not root:
                    return None
                node = q.popleft()
                max_ele.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                size -= 1
            maxe = -maxsize
            for i in range(len(max_ele)):
                maxe = max(maxe, max_ele[i])
            ans.append(maxe)
        return ans
