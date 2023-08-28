# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def recur(x:TreeNode,y:TreeNode):
            if not x and not y:
                return True
            if x and not y:
                return False
            if y and not x:
                return False
            
            return x.val == y.val and recur(x.left,y.right) and recur(x.right,y.left)
        
        return recur(root,root)
        
        