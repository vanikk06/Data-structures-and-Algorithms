class node:
    
    def __init__(self, val, nextnode=None):
        
        self.val = val
        self.next = nextnode
        self.min = val

class MinStack:

    def __init__(self):
            
        self.topnode = None

    def push(self, x: int) -> None:
        if self.topnode == None:
            self.topnode = node(x, None)
        else:
            temp = self.topnode.min
            self.topnode = node(x, self.topnode)
            if temp < self.topnode.min:
                self.topnode.min = temp

    def pop(self) -> None:
        self.topnode = self.topnode.next

    def top(self) -> int:
        return self.topnode.val

    def getMin(self) -> int:
        return self.topnode.min
