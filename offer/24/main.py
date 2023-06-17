# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None

        while head:
            temp = head.next
            head.next = pre

            pre = head
            head = temp

        return pre


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)

n1.next = n2
n2.next = n3

s = Solution()
r = s.reverseList(n1)

while r:
    print(r.val)
    r = r.next
