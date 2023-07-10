# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(None)
        tmp = head
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next

        if l1:
            tmp.next = l1
        if l2:
            tmp.next = l2
        return head.next


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(4)
n1.next = n2
n2.next = n3

l1 = ListNode(1)
l2 = ListNode(3)
l3 = ListNode(4)
l1.next = l2
l2.next = l3

s = Solution()
s.mergeTwoLists(n1, l1)
