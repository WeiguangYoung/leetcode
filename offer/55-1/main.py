# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if not node:
                return
            self.depth += 1
            if self.depth > self.max_depth:
                self.max_depth = self.depth
            
            dfs(node.left)
            dfs(node.right)
            
            self.depth -= 1
            
        self.max_depth = 0
        self.depth = 0
        dfs(root)
        return self.max_depth