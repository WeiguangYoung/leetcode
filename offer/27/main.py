# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def swap(node: TreeNode):
            if not node:
                return

            node.left, node.right = node.right, node.left
            swap(root.left)
            swap(root.right)

        swap(root)
        return root
