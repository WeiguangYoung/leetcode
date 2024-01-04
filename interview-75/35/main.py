class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return

        cur = head
        node_map = {}
        while cur:
            node_map[cur] = Node(
                x=cur.val,
            )
            cur = cur.next

        cur = head
        while cur:
            this_node = node_map.get(cur)

            new_next = node_map.get(cur.next)
            this_node.next = new_next

            new_random = node_map.get(cur.random)
            this_node.random = new_random

            cur = cur.next

        return node_map.get(head)
