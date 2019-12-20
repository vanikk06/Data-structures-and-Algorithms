#利用pointer的移動，來達成insert

def insert(root, val):
    if root == None:
        return
    
    pointer = root
    node = None
    
    if val != None:
        while not node:
            if val <= pointer.val:
                if pointer.left == None:
                    pointer.left = TreeNode(val)
                    node = pointer.left
                else:
                    pointer = pointer.left
            else:
                if pointer.right == None:
                    pointer.right = TreeNode(val)
                    node = pointer.right
                else:
                    pointer = pointer.right
    
        return node
        
       
