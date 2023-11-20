from collections import deque


class Solution:
    def removeDuplicates(self, s: str) -> str:
        if not s:
            return ""
        queue = deque()
        queue.append(s[0])
        for i in range(1, len(s)):
            if queue and s[i] == queue[-1]:
                queue.pop()
            else:
                queue.append(s[i])
        return "".join(queue)
