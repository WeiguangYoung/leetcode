
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        root.left, root.right = self.mirrorTree(
            root.right), self.mirrorTree(root.left)
        return root
