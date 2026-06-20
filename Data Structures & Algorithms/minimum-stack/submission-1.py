class MinStack:
    stack = []
    minimum = 0
    prefix = []

    def __init__(self):
        self.stack = []
        self.minimum = 0
        self.prefix = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.prefix.append(val)
        elif self.prefix[-1] < val:
            self.prefix.append(self.prefix[-1])
        elif self.prefix[-1] >= val:
            self.prefix.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.prefix.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefix[-1]
