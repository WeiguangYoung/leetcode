from typing import Optional


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 0

        def dfs(node, is_left, length):
            if not node:
                return 0

            nonlocal ans
            ans = max(ans, length)
            if is_left:
                dfs(node.left, True, 0)
                dfs(node.left, False, length+1)
            else:
                dfs(node.right, False, 0)
                dfs(node.right, True, length+1)

        dfs(root, True, 0)
        dfs(root, False, 0)
        return ans
