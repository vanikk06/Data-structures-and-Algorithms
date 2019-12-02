from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        """
        :type val: int
        :type next: ListNode
        :rtype: None        
        """
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        """
        :type capacity: int
        :rtype: None
        """
    def add(self, key):
        """
        :type key: str
        :rtype: None
        """
        
        capacity = self.capacity
        encoding_key, index = self.Encoding_MD5(key, capacity)
        
        if self.data[index] == None:
            self.data[index] = ListNode(encoding_key)
        else:
            node = self.data[index]
            if node.val == encoding_key:
                return
            while node.next != None:
                if node.next.val == encoding_key:
                    return
                node = node.next
            node.next = ListNode(encoding_key)            
        return
    
        
    def Encoding_MD5(self, key:str, capacity:int):
        encoding = MD5.new(key.encode('utf-8'))
        encoding_key = int(encoding.hexdigest(), 16)
        index = int(encoding.hexdigest(), 16) % capacity
        return encoding_key, index
    
    
    def remove(self, key):
        """
        :type key: str
        :rtype: None
        """
        
        capacity = self.capacity
        encoding_key, index = self.Encoding_MD5(key, capacity)
        
        if encoding_key == self.data[index].val:
            if self.data[index].next == None:
                self.data[index] = None
            else:
                self.data[index] = self.data[index].next
        else:
            node = self.data[index]
            pre_node = node
            while node.val != encoding_key:
                pre_node = node
                node = node.next

            pre_node.next = node.next
        return
    
                
    def contains(self, key):
        """
        :type key: str
        :rtype: bool(True or False)
        """
        
        capacity = self.capacity
        encoding_key, index = self.Encoding_MD5(key, capacity)
        
        node = self.data[index]
        while node != None:
            if node.val == encoding_key:
                return True
            else:
                node = node.next
        return False
       
        
