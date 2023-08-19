import sys
from collections import deque


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:

    # Function to return a list of nodes visible from the top view
    # from left to right in Binary Tree.
    def topView(self, root):
        queue = deque([(root, 0)])
        mp = {}
        minn = sys.maxsize
        maxx = -sys.maxsize

        while queue:
            node, hd = queue.popleft()
            maxx = max(maxx, hd)
            minn = min(minn, hd)

            if hd not in mp:
                mp[hd] = node.data

            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))

        result = []
        for i in range(minn, maxx + 1):
            result.append(mp[i])

        return result
