class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insert(self, root, val:int):
        if root == None:
            return

        if val != None:
            if val <= root.val:
                if root.left == None:
                    root.left = TreeNode(val)                 #建立node
                    node = root.left
                else:
                    node = self.insert(root.left, val)               #以新的parent進行判斷      
            else:
                if root.right == None:
                    root.right = TreeNode(val)                #建立node
                    node = root.right
                else:
                    node = self.insert(root.right, val)              #以新的parent進行判斷

        return node
       
        
    def delete(self, root, target:int):
        
        pre_delete_node, delete_node, i = self._delete_pointer(root, target)
    
        if i != 0:
            if delete_node == root:                    #刪除root
                return self._delete_root(root, target)
            else:
                for j in range(i):                     #刪除node
                    root1 = self._delete_action(delete_node, pre_delete_node)
                    pre_delete_node, delete_node, i = self._delete_pointer(root1, target)

        return root
    
    def _delete_pointer(self, root, target:int):
        """
        找到要刪除的node
        """
        if root == None:
            return

        pointer = root                      #移動指標
        pre_pointer = pointer               #輔助刪除
        i = 0
        delete_node = pointer               #刪除指標
        pre_delete_node = pre_pointer       #輔助刪除

        while pointer.left != None or pointer.right != None:
            if target == pointer.val:                               #等於
                delete_node = pointer
                pre_delete_node = pre_pointer
                i += 1                      #存在於leaf以外的次數
                pre_pointer = pointer
                pointer = pointer.left

            elif target < pointer.val and pointer.left != None:     #小於，判斷存在再移動
                pre_pointer = pointer
                pointer = pointer.left

            elif target > pointer.val and pointer.right != None:    #大於，判斷存在再動
                pre_pointer = pointer
                pointer = pointer.right
            else:                                                   #不存在，跳出迴圈
                break

        if target == pointer.val:      #leaf node
            delete_node = pointer
            pre_delete_node = pre_pointer
            i += 1

        return pre_delete_node, delete_node, i
    
    def _delete_action(self, delete_node, pre_delete_node):
        """
        刪除node
        """
        if delete_node.left == None and delete_node.right == None:   #沒有孩子
            if delete_node.val <= pre_delete_node.val:
                pre_delete_node.left = None
            else:
                pre_delete_node.right = None

        if (delete_node.left == None and delete_node.right != None) or (delete_node.left != None and delete_node.right == None):   #一個孩子
            if delete_node.left == None:
                if delete_node.right.val <= pre_delete_node.val:
                    pre_delete_node.left = delete_node.right
                else:
                    pre_delete_node.right = delete_node.right
            else:
                if delete_node.left.val <= pre_delete_node.val:
                    pre_delete_node.left = delete_node.left
                else:
                    pre_delete_node.right = delete_node.left

        if delete_node.left != None and delete_node.right != None:   #兩個孩子
            while delete_node.left != None and delete_node.right != None: #往後移動僅有一個孩子或無孩子的情形
                if delete_node.val <= root.val:
                    delete_node.val = delete_node.left.val
                    pre_delete_node = delete_node
                    delete_node = delete_node.left
                else:
                    delete_node.val = delete_node.right.val
                    pre_delete_node = delete_node
                    delete_node = delete_node.right

            if delete_node.left == None and delete_node.right == None:
                if delete_node == pre_delete_node.left:
                    pre_delete_node.left = None            
                else:
                    pre_delete_node.right = None
            else:
                if delete_node == pre_delete_node.left:
                    if delete_node.right == None:
                        pre_delete_node.left = delete_node.left
                    else:
                        pre_delete_node.left = delete_node.right
                else:
                    if delete_node.right == None:
                        pre_delete_node.right = delete_node.left
                    else:
                        pre_delete_node.right = delete_node.right

        return root
    
    
    def _delete_root(self, root, target:int):
        """
        刪除root
        """
    
        Max = root.left          #採子樹左邊最大值
        pre_Max = root

        while Max.right != None:    #移動到最大值位置
            pre_Max = Max
            Max = Max.right

        if Max == root.left:        #最大值為root的左邊
            root.val = Max.val
            root.left = Max.left

        else:
            if Max.left == None:    #最大值沒有孩子
                root.val = Max.val
                pre_Max.right = None
            else:                   #最大值有一個孩子
                root.val = Max.val
                pre_Max.right = Max.left     

        return root
    
    def search(self, root, target:int):
        if root == None:
            return
    
        pointer = root        #指標
    
        while pointer.val != target:    #尋找目標位置
            if target < pointer.val and pointer.left != None:
                pointer = pointer.left
            elif target > pointer.val and pointer.right != None:
                pointer = pointer.right
            else:
                return
    
        return pointer
        
    def modify(self, root, target:int, new_val:int):
        """
        修改
        """
        if target > root.val and new_val == root.val:   #情況3
            root, i = self._modify_method(root, target)

            for k in range(i):
                self.insert(root, new_val)

            return root


        pre_modify_node, modify_node, i = self._delete_pointer(root, target)

        if modify_node != root:     #情況1
            root, i = self._modify_method(root, target)
            
            for k in range(i):
                self.insert(root, new_val)

            return root


        else:    #修改值為root(情況2)
            if new_val > modify_node.left.val and new_val < modify_node.right.val:   #修改值仍介於root.left與root.right之間，就直接修改
                temp_val = root.val
                root.val = new_val

                if temp_val < new_val:          #如果直接修改的值大於原本的root，要把右邊與修改後值相同的值刪除             
                    if self.search(root.right, new_val) != None:
                        root1, i = self._modify_root_delete(root, new_val)
                        root.right = root1

                        for k in range(i):      #重新插入
                            self.insert(root, new_val)

                return root

            else:
                root1 = self._delete_root(root, target)
                self.insert(root1, new_val)
                return root1
    
    def _modify_method(self, root, target:int):
        """
        刪除、刪除次數
        """

        pre_delete_node, delete_node, i = self._delete_pointer(root, target)
        k = i     #另存，好回傳

        if delete_node == root:
            return self._delete_root(root, target)
        else:
            for j in range(i):
                root1 = self._delete_action(delete_node, pre_delete_node)
                pre_delete_node, delete_node, i = self._delete_pointer(root1, target)

        return root, k

    
    def _modify_root_delete(self, root, targetLint):
        """
        root修改
        """
    
        if root.right != None:  #在root.right存在下才可移動
            root1 = root.right
        else:
            return root

        pre_delete_node, delete_node, i = self._delete_pointer(root1, target)
        k = i

        if k != 0:
            if delete_node == root1:
                return self._delete_root(root1, target), k
            else:
                for j in range(i):
                    root2 = self._delete_action(delete_node, pre_delete_node)
                    pre_delete_node, delete_node, i = self._delete_pointer(root2, target)


        return root1, k
