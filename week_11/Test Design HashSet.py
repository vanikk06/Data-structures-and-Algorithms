class Mynode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self, capacity=5):
        """
        Initialize your data structure here.
        """
        self.capacity = capacity
        self.data = [None] * capacity
        

    def add(self, key: int) -> None:
        
        idx = key % self.capacity
        node = self.data[idx]
        
        while node:
            if node.val == key:
                return
            node = node.next
        
        new_node = ListNode(key)
        new_node.next = self.data[idx]
        self.data[idx] = new_node
            
        
        

    def remove(self, key: int) -> None:
        
        idx = key % self.capacity
        node = self.data[idx]
        
        if node and node.val == key:
            self.data[idx] = node.next
            return
        
        pre = None
        while node:
            if node.val == key:
                pre.next = node.next
                return
            pre = node
            node = node.next
        
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        
        idx = key % self.capacity
        node = self.data[idx]
        
        while node:
            if node.val == key:
                return True
            node = node.next
            
        return False
