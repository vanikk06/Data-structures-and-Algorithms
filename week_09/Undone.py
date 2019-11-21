#Undone
##利用Search的方式嘗試用Insert

def insert(root, val):
    if root == None:
        return
    
    pointer = root
    add_node = 0
    
    if val != None:
        while add_node == 0:
            if val <= pointer.val and pointer.left == None:
                pointer.left = TreeNode(val)
                add_node = 1
            else:
                pointer = pointer.left

            while pointer.right == None:
                pointer.right = TreeNode(val)
        
        
