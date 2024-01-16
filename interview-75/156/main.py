import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        results = []
        if not root:
            return results

        queue = collections.deque()
        queue.append(root)

        while queue:
            node = queue.popleft()

            if node:
                results.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                results.append(None)

        return results

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return

        root = TreeNode(data[0])
        queue = collections.deque()
        queue.append(root)

        i = 1
        while queue:
            node = queue.popleft()

            if data[i] is not None:
                node.left = TreeNode(data[i])
                queue.append(node.left)
            else:
                node.left = None

            i += 1

            if data[i] is not None:
                node.right = TreeNode(data[i])
                queue.append(node.right)
            else:
                node.right = None

            i += 1

        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
