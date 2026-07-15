class MinStack:

    def __init__(self):
        self.stack = []
    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((val, val))
        else:
            minVal = min(self.stack[-1][0], val)
            self.stack.append((minVal, val))

    def pop(self) -> None:
        popValue = self.stack.pop()
        return popValue
        
    def top(self) -> int:
        return self.stack[-1][1]

    def getMin(self) -> int:
        return self.stack[-1][0]
        
