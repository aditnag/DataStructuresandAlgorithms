from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        opn = ["(", "{", "["]
        close = [")", "}", "]"]
        stack = deque()
        for chr in s:
            if chr in opn:
                stack.append(chr)
            elif chr in close:
                if not stack or stack[-1] != opn[close.index(chr)]:
                    return False
                stack.pop()
        return not stack


# if __name__ == "__main__":
#     solution = Solution()
#     s = input()
#     length = solution.isValid(s)
#     print(length)
