# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(node: TreeNode):
            if not node:
                return
            dfs(node.right)
            self.k -= 1
            if self.k == 0:
                self.result = node.val
                return
            
            dfs(node.left)
        
        self.k = k
        dfs(root)
        return self.result

node1= TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 =TreeNode(4)
node3.left = node1
node3.right = node4
node1.right = node2

s = Solution()
result = s.kthLargest()