import sys
from collections import deque, defaultdict


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:

    # Function to find the vertical order traversal of Binary Tree.
    def verticalOrder(self, root):
        if root is None:
            return []

        queue = deque([(root, 0)])
        mp = defaultdict(list)
        maxx = -sys.maxsize
        minn = sys.maxsize

        while queue:
            node, hd = queue.popleft()
            mp[hd].append(node.data)
            maxx = max(maxx, hd)
            minn = min(minn, hd)

            if node.left:
                queue.append((node.left, hd - 1))

            if node.right:
                queue.append((node.right, hd + 1))

        result = []
        for i in range(minn, maxx + 1):
            result.extend(mp[i])
        return result
