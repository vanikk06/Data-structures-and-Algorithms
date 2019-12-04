
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
        
    def Encoding_MD5(self, key:str, capacity:int):
        """
        使用MD5套件編碼、加密
        """
        encoding = MD5.new(key.encode('utf-8'))
        encoding_key = int(encoding.hexdigest(), 16)
        index = int(encoding.hexdigest(), 16) % capacity
        return encoding_key, index
    
    
    def add(self, key):
        """
        增加
        """
        
        capacity = self.capacity
        encoding_key, index = self.Encoding_MD5(key, capacity)  #編碼
        
        if self.data[index] == None:  # index內是空的
            self.data[index] = ListNode(encoding_key)
        else:
            node = self.data[index]   # index內已有node存在
            if node.val == encoding_key:  #遇到重複值只存取一次
                return
            while node.next != None:  #將指針走到最後一個node
                if node.next.val == encoding_key:
                    return
                node = node.next
            node.next = ListNode(encoding_key)     # 在最後一個node後，增加一個node
        return
    
    
    def remove(self, key):
        """
        移除
        """
        
        capacity = self.capacity
        encoding_key, index = self.Encoding_MD5(key, capacity)  #編碼
        
        if self.data[index] == None:  #刪除目標的index是空的
            return
        
        if encoding_key == self.data[index].val: #刪除目標是第一個node
            if self.data[index].next == None:
                self.data[index] = None
            else:
                self.data[index] = self.data[index].next
        else:                                    #刪除目標不是第一個node
            node = self.data[index]
            pre_node = None
            while node.val != encoding_key and node.next != None:  #往下找刪除目標
                pre_node = node
                node = node.next
            if node.val == key:       #找到後，重新建立node連結
                pre_node.next = node.next
        return
    
                
    def contains(self, key):
        """
        搜尋
        """
        
        capacity = self.capacity
        encoding_key, index = self.Encoding_MD5(key, capacity)   #編碼
        
        node = self.data[index]
        while node != None:    #node存在
            if node.val == encoding_key:    #找到搜尋目標就回傳True
                return True
            else:
                node = node.next
        return False                        #沒找到救回False
      
      
      
# 課堂live coding範例
# LeetCode：705. Design HashSet
# https://github.com/vanikk06/Data-structures-and-Algorithms/blob/master/week_11 → 課堂講義
