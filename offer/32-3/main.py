from typing import List
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = collections.deque()
        q.append(root)

        reverse = False
        while q:
            l2 = []

            i = 0
            length = len(q)
            while i < length:
                node = q.popleft()

                if reverse:
                    l2.insert(0, node.val)
                else:
                    l2.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                i += 1

            res.append(l2)
            reverse = not reverse

        return res
