class node:
    
    def __init__(self, val, nextnode=None):
        
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
            self.topnode = node(x, self.topnode)
           
                
    def pop(self) -> None:
        self.topnode = self.topnode.next
        

    def top(self) -> int:
        return self.topnode.val

    def getMin(self) -> int:
        
        p = self.topnode
        temp = self.topnode.next
        min = p.val
        
        while p.next != None:
            temp = p.next
            if min > temp.val:
                min = temp.val                
            p = p.next
            
        return min

