class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None                  #value
        self.next = None                 #下一個
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.val == None:             #第一個是空的
            return -1
        
        if index == 0 :                  #取第一個值(index=0)
            return self.val
       
        p = self.next
        i = 1
        while p != None:                 #先指到index的位置，再取值
            if i == index:
                return p.val
            p = p.next
            i += 1
        return -1
            

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.val == None:            #第一個是空的，直接存到第一個位置
            self.val = val
            return
        
        temp = self.val                 #第一個已經存在
        self.val = val
        tempnode = self.next
        self.next = MyLinkedList()
        self.next.val = temp
        self.next.next = tempnode
        return
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.val == None:           #第一個是空的，直接存到第一個位置
            self.val = val
            return
        
        p = self                       #先指到最後一個，再在後面創造一個node
        while p.next != None:
            p = p.next
        p.next = MyLinkedList()
        p.next.val = val
        return

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index <= 0:                 #向左增加 = 增加在最前面
            self.addAtHead(val)
            return
        
        i = 0 
        p = self
        pre = p 
        while i < index:               #指到index位置，在他的前一個後面創造一個node
            i += 1
            pre = p
            if p != None and p.val != None:
                p = p.next
            else:
                return
        pre.next = MyLinkedList()
        pre.next.val = val
        pre.next.next = p
        return
                
            

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """                
        if index < 0:                 #index<0 不存在
            return
        if index == 0:                #刪掉第一個
            if self.val == None:         #第一個是空值
                return
            if self.next == None:        #第一個不是空的，但下一個不存在
                self = None
                return
            self.val = self.next.val
            self.next = self.next.next
            
        i = 0
        p = self
        pre = p 
        while i < index:              #指到要刪掉的位置
            i += 1
            pre = p
            if pre == None:
                return
            p = p.next
        if p != None:                    #要刪除值的下一個不是空的，上一個的下一個變成要刪除值的下一個
            pre.next = p.next
        else:
            pre.next = None              #是空的，上一個的下一個變None
        return
