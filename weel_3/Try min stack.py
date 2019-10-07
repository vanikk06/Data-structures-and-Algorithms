class node:
    
    def__init__(self, val, nextnode=None):
        
        self.val = val
        self.next = nextnode

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
    
        self.topnode = None

    def push(self, x: int) -> None:
        if self.topnode == None:
            self.topnode = node(x, None)
        else:
            temp = self.topnode
            self.topnode.next = temp
            self.topnode = node(x, self.topnode.next)

    def pop(self) -> None:
        return self.topnode = slef.topnode.next

    def top(self) -> int:
        return slef.topnode.val

    def getMin(self) -> int:
