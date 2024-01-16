import collections

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def rserialize(self, node: TreeNode, results: list):
        if node is None:
            results.append(None)
        else:
            results.append(node.val)

            self.rserialize(node.left, results)
            self.rserialize(node.right, results)

    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        results = []
        self.rserialize(root, results)
        return results

    def rdeserialize(self, data):
        if not data:
            return None

        node_val = data.popleft()
        if node_val is None:
            return None

        node = TreeNode(node_val)
        node.left = self.rdeserialize(data)
        node.right = self.rdeserialize(data)
        return node

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        queue = collections.deque()
        for i in data:
            queue.append(i)
        return self.rdeserialize(queue)


# Your Codec object will be instantiated and called as such:
codec = Codec()
ret = codec.deserialize([1, 2, None, None, 3, 4, None, None, 5, None, None])
print(ret.val)
