class Solution:
    def pathTarget(self, root: TreeNode, target: int) -> List[List[int]]:
        res, path = [], []

        def recur(root, tar):
            if not root:
                return
            
            path.append(root.val)
            tar -= root.val

            if tar == 0 and not root.left and not root.right:
                res.append(list(path))
            recur(root.left, tar)
            recur(root.right, tar)

            path.pop()

        recur(root, target)
        return res
