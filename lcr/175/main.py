class Solution:
    def calculateDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return max(self.calculateDepth(root.left), self.calculateDepth(root.right)) + 1
