class Mynode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self, capacity=6):
        """
        Initialize your data structure here.
        """
        self.capacity = capacity
        self.data = [None] * capacity
        

    def add(self, key: int) -> None:
        
        index = key % self.capacity
        node = self.data[index]
        pre = None
        
        while node:
            if node.val == key:
                return
            pre = node
            node = node.next
        
        if  pre == None:
            self.data[index] = Mynode(key)
        else:
            pre.next = Mynode(key)
        
        return
      
    def remove(self, key: int) -> None:

      index = key % self.capacity
      node = self.data[index]
      pre_node = None

      if node != None and node.val == key:
          self.data[index] = node.next
          return


      while node:
          if node.val == key:
              pre_node.next = node.next
              return
          pre_node = node
          node = node.next

      return
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = key % self.capacity
        
        node = self.data[index]
        while node != None:
            if node.val == key:
                return True
            else:
                node = node.next
        return False
      
