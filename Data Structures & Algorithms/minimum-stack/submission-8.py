class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            if val < self.minStack[-1]:
                new_mini = val
            else:
                new_mini = self.minStack[-1]
        else: 
            new_mini = val
        self.minStack.append(new_mini)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
