class MyQueue:
    def __init__(self):
        self.queue = []
        self.back = 0
        self.front = 0

    # Function to push an element x in a queue.
    def push(self, x):
        if self.back == len(self.queue) - 1:
            print("Overflow")
        else:
            self.queue.append(x)
            self.back += 1

    # Function to pop an element from queue and return that element.
    def pop(self):
        if self.front == self.back:
            print("Underflow")
        ele = self.queue.pop(0)
        self.front += 1
        return ele


# add code here

