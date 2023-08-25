# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(a, b):
            if not b:
                return True

            if not a or a.val != b.val:
                return False

            return recur(a.left, b.left) and recur(a.right, b.right)

        if not A or not B:
            return False

        return recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)


s = Solution()
n11 = TreeNode(1)
n12 = TreeNode(0)
n13 = TreeNode(1)
n14 = TreeNode(-4)
n15 = TreeNode(-3)

n21 = TreeNode(1)
n22 = TreeNode(-4)

n11.left = n12
n11.right = n13
n12.left = n14
n12.right = n15

n21.left = n22

r = s.isSubStructure(n11, n21)

print(r)
