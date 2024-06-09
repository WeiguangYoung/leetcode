from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy_head = ListNode(0)
        n1, n2 = head, head.next
        pre_head = dummy_head
        while n1 and n2:
            tmp = n2.next
            n2.next = n1
            n1.next = tmp
            pre_head.next = n2

            if tmp and tmp.next:
                pre_head = n1
                n1 = tmp
                n2 = n1.next
            else:
                break

        return dummy_head.next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        new_head = head.next
        head.next = self.swapPairs(new_head.next)
        new_head.next = head
        return new_head