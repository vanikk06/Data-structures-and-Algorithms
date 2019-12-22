
def _delete_pointer(root, target):
    if root == None:
        return
    
    pointer = root
    pre_pointer = pointer
    i = 0
    delete_node = pointer
    pre_delete_node = pre_pointer

    while pointer.left != None or pointer.right != None:
        if target == pointer.val and pointer.left != None:
            delete_node = pointer
            pre_delete_node = pre_pointer
            i += 1
            pre_pointer = pointer
            pointer = pointer.left

        elif target < pointer.val and pointer.left != None:
            pre_pointer = pointer
            pointer = pointer.left

        elif target > pointer.val and pointer.right != None:
            pre_pointer = pointer
            pointer = pointer.right
        else:
            break
        
    if target == pointer.val:
        delete_node = pointer
        pre_delete_node = pre_pointer
        i += 1
  
    return pre_delete_node, delete_node, i
    
    
def _delete_action(delete_node, pre_delete_node):
    if delete_node.left == None and delete_node.right == None:
        if delete_node.val <= pre_delete_node.val:
            pre_delete_node.left = None
        else:
            pre_delete_node.right = None
        
    if (delete_node.left == None and delete_node.right != None) or (delete_node.left != None and delete_node.right == None):
        if delete_node.left == None:
            pre_delete_node.right = delete_node.right
        else:            
            pre_delete_node.left = delete_node.left
    
    if delete_node.left != None and delete_node.right != None:
        while delete_node.left != None and delete_node.right != None:
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
        
        
def _delete_root(root, target):
    
    Max = root.left
    pre_Max = root
    
    while Max.right != None:
        pre_Max = Max
        Max = Max.right
        
    if Max == root.left:
        root.val = Max.val
        root.left = Max.left
        
    else:
        if Max.left == None:
            root.val = Max.val
            pre_Max.right = None
        else:
            root.val = Max.val
            pre_Max.right = Max.left     
    
    return root
    
def delete(root, target):
    
    pre_delete_node, delete_node, i = _delete_pointer(root, target)
    
    for j in range(i):
        if delete_node == root:
            return _delete_root(root, target)
        else:
            root1 = _delete_action(delete_node, pre_delete_node)
            pre_delete_node, delete_node, i = _delete_pointer(root1, target)

    return root
