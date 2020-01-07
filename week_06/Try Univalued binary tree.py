class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:  
        
        if root:
            if (root.left and root.left.val != root.val) or (root.right and root.right.val != root.val):
                    return False
        else:
            return True
        
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
        
