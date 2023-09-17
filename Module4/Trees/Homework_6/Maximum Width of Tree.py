# User function Template for python3
from collections import deque


# Node Class:
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    # Function to get the maximum width of a binary tree.
    def getMaxWidth(self, root):

        if root is None:
            return 0

        q = deque()
        q.append(root)
        maxwidth = 0

        while q:
            size = len(q)
            maxwidth = max(maxwidth, size)
            for _ in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return maxwidth
