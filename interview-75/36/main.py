class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        nodes = []
        
        def dfs(node: Node):
            if not node:
                return
            
            nodes.append(node)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        
        if not nodes:
            return 
        
        for i in range(len(nodes)-1):
            nodes[i].right = nodes[i+1]
            nodes[i+1].left = nodes[i]
        
        nodes[0].left = nodes[-1]
        nodes[-1].right = nodes[0]
        
        head = Node()
        head.right = nodes[0]
        
        return head
        