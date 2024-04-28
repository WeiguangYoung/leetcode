from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = [root]
        results = []
        i = 1
        while queue:
            tmp = []
            result = 0
            for node in queue:
                result += node.val
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)

            queue = tmp
            results.append([i, result])
            i += 1

        results.sort(key=lambda x: x[1], reverse=True)
        return results[0][0]

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        results = []

        def dfs(node, level):
            if not node:
                return
            if level == len(results):
                results.append([level, node.val])
            else:
                results[level][1] += node.val

            if node.left:
                dfs(node.left, level+1)
            if node.right:
                dfs(node.right, level+1)

        dfs(root, 0)
        results.sort(key=lambda x: x[1], reverse=True)
        return results[0][0]
