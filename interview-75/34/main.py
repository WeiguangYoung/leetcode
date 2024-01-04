from typing import List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        results, path = [], []
        
        def dfs(node, s):
            if not node:
                return
            path.append(node.val)
            s += node.val
            # 判断叶子节点？
            if s == target and not node.right and not node.right:
                results.append(list(path))
            
            dfs(node.left, s)
            dfs(node.right, s)
            path.pop()
            
            
        
        dfs(root, 0)
        return results
        
            