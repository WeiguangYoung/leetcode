# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            head = head.next
            return head

        cur, pre = head.next, head
        while cur:
            if cur.val == val:
                pre.next = cur.next
                break
            else:
                cur, pre = cur.next, cur

        return head
