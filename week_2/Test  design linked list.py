class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None     #當前node的value
        self.next = None    #下一個node

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.val == None:        #self不存在
            return -1
        
        if index == 0:
            return self.val
        
        p = self.next
        i = 1
        while p != None:
            if i == index:
                return p.val
            p = p.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.val == None:
            self.val = val
            return
        
        temp = self.val            #原本self.val存到暫存空間
        self.val = val             #騰出的空間，填入新的值
        
        tempnode = self.next       #原本self.next存到暫存空間
        self.next = MyLinkedList() #原本的self，創造一個node的空間
        
        #將暫存的東西，存入新創的node空間
        self.next.val = temp       
        self.next.next = tempnode
        return
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.val == None:
            self.val = val
            return
        
        p = self
        while p.next != None:      #如果self.next不是最後一個，再往下一個
            p = p.next
        
        p.next = MyLinkedList()    #指向最後一個node後，在他後面再創造一個node
        p.next.val = val
        return
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        
        if index <= 0:                 #向左增加
            self.addAtHead(val)
        return
    
        i = 0                               #先指到要增加的index位置
        p = self
        pre = p
        while i < index:                    #i=index時，停止
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
        i = 0 
        p = self
        if index < 0:              #index invalid
            return
        
        if index == 0 :            #考慮 index=0 的各種情況
            if self.val == None:   #invalid
                return
            if self.next == None:  #valid, no next
                self = None
                return
            self.val = self.next.val
            self.next = self.next.next
            
        #i = 0 
        #p = self
        pre = p
        while i < index:         #指到index
            i += 1
            pre = p 
            if pre == None:
                return
            p = p.next
        
        if p != None:            #根據index作出變化
            pre.next = p.next    #如果index不是None，就將index的前一個的下一個指派給index的下一個
        else:                    #如果index是None，就讓index的前一個的下一個是None
            pre.next = None
        return
