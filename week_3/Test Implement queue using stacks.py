class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_stack = []
        self.stack_queue = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack_queue:
            return self.stack_queue.pop()
        
        while len(self.stack_stack) is not 0:
            self.stack_queue.append(self.stack_stack.pop())
        return self.stack_queue.pop()
            

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack_queue:
            return self.stack_queue[-1]
        
        while len(self.stack_stack) is not 0:
            self.stack_queue.append(self.stack_stack.pop())
        return self.stack_queue[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack_stack) == 0 and len(self.stack_queue) == 0


