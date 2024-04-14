# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTargetNode(self, root: TreeNode, cnt: int) -> int:
        def dfs(node):
            if not node:
                return

            dfs(node.right)
            if self.cnt == 0:
                return

            self.cnt -= 1
            if self.cnt == 0:
                self.res = node.val

            dfs(node.left)

        self.cnt = cnt
        dfs(root)
        return self.res
