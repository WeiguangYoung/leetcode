class TreeNode:
    """AVL 树节点类"""

    def __init__(self, val: int):
        self.val: int = val          # 节点值
        self.left: TreeNode = None   # 左子节点引用
        self.right: TreeNode = None  # 右子节点引用


def dfs(
    preorder: list,
    inorder_map: dict,
    i: int,
    l: int,
    r: int,
) -> TreeNode:
    """构建二叉树：分治"""
    # 子树区间为空时终止
    if l > r:
        return
    root = preorder[i]
    m = inorder_map[preorder[i]]
    root.left = dfs(preorder, inorder_map, i+1, l, m-1)
    root.right = dfs(preorder, inorder_map, i+m-l+1, m+1, r)
    return root


def build_tree(preorder: list, inorder: list) -> TreeNode:
    """构建二叉树"""
    # 初始化哈希表，存储 inorder 元素到索引的映射
    inorder_map = {inorder[i]: i for i in range(len(inorder))}
    root = dfs(preorder, inorder_map, 0, 0, len(inorder)-1)
    return root
