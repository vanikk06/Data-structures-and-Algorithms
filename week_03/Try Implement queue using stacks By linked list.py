class node:
    def __init__(self, val, nextnode=None):
        self.val = val
        self.next = nextnode
    
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = None
        self.stack2 = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self.stack1 == None:
            self.stack1 = node(x, None)
        
        if self.stack1 != None:
            while self.stack1 != None and self.stack1.val != None:
                temp = self.stack1.val
                tempnode = self.stack1.next
                self.stack2 = node(temp, tempnode)
                self.stack1 = self.stack1.next
                
            self.stack1 = node(x, None)
            while self.stack2 != None:
                temp = self.stack2.val
                tempnode = self.stack2.next
                self.stack1 = node(temp, tempnode)
                self.stack2 = self.stack2.next
        return
            

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
