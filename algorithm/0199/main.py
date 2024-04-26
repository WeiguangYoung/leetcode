from typing import List, Optional
from collections import deque
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        queue = deque()
        queue.append([root])
        while queue:
            tmp = []
            nodes = queue.popleft()
            ans.append(nodes[-1].val)
            for node in nodes:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if tmp:
                queue.append(tmp)
        return ans
