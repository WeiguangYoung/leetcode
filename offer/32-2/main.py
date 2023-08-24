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
        while q:
            l2 = []
            i = 0
            length = len(q)
            while i < length:
                node = q.popleft()
                l2.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                i += 1

            res.append(l2)

        return res


# [3,9,20,null,null,15,7]
n1 = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(15)
n5 = TreeNode(7)
n1.left = n2
n1.right = n3

n3.left = n4
n3.right = n5

s = Solution()
r = s.levelOrder(n1)
print(r)
