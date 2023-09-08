from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque()
        q.append(root)
        result = []
        while len(q) > 0:
            size = len(q)
            result = []
            while size:
                if root is None:
                    return root

                node = q.popleft()
                result.append(node)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                size -= 1

            for i in range(len(result) - 1):
                result[i].next = result[i + 1]
        return root
