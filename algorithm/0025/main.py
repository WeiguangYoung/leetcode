from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        dummy_head.next = head
        pre_head = dummy_head

        while True:
            cur_nodes = []
            tmp = pre_head
            end = False
            for _ in range(k):
                if tmp.next:
                    cur_nodes.append(tmp.next)
                    tmp = tmp.next
                else:
                    end = True
                    break
            if end:
                break

            tmp = pre_head
            next_head = cur_nodes[-1].next
            for i in range(len(cur_nodes) - 1, -1, -1):
                tmp.next = cur_nodes[i]
                tmp = tmp.next
            tmp.next = next_head
            pre_head = tmp

        return dummy_head.next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        dummy_head.next = head
        pre_node = dummy_head

        while head:
            tail = pre_node
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy_head.next

            tail_next = tail.next

            # 翻转head到tail
            pre = tail.next
            cur = head
            while pre != tail:
                next = cur.next
                cur.next = pre

                pre = cur
                cur = next

            pre_node.next = tail
            head.next = tail_next

            pre_node = head
            head = head.next

        return dummy_head.next
