from collections import deque


class MyQueue:
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()
        self.front = 0
        self.bottom_of_s1 = 0

    def push(self, x: int) -> None:
        if len(self.s1) == 0 and len(self.s2) == 0:
            self.front = x
        if len(self.s1) == 0:
            self.bottom_of_s1 = x
        self.s1.append(x)

    def pop(self) -> int:
        if len(self.s2) == 0:
            while len(self.s1) != 0:
                self.s2.append(self.s1.pop())
        ans = self.s2.pop()
        if len(self.s2) != 0:
            self.front = self.s2[-1]
        if len(self.s1) != 0:
            self.front = self.bottom_of_s1
        return ans

    def peek(self) -> int:
        return self.front

    def empty(self) -> bool:
        return len(self.s1) == 0 and len(self.s2) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
