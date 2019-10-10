class MinStack:

    def __init__(self):
       
        self.min_stack = []

    def push(self, x: int) -> None:
        if self.min_stack:
            self.min_stack.append((x, min(x, self.min_stack[-1][1])))
        else:
            self.min_stack.append((x, x))
        

    def pop(self) -> None:
        if self.min_stack:
            self.min_stack.pop()

    def top(self) -> int:
        if self.min_stack:
            return self.min_stack[-1][0]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1][1]
