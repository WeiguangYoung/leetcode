# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node: TreeNode, path_max: int):
            if not node:
                return 0
            ans = 0
            if node.val >= path_max:
                ans += 1
                path_max = node.val

            ans += dfs(node.left, path_max) + dfs(node.right, path_max)
            return ans

        return dfs(root, root.val)
