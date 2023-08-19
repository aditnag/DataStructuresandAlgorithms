import sys
from collections import deque


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def bottomView(self, root):
        queue = deque([(root, 0)])
        mp = {}
        maxx = -sys.maxsize
        minn = sys.maxsize

        while queue:
            node, hd = queue.popleft()
            mp[hd] = node.data
            maxx = max(maxx, hd)
            minn = min(minn, hd)

            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))

        result = []
        for i in range(minn, maxx+1):
            result.append(mp[i])
        return result
