from collections import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_nums = []
        cur = l1
        while cur:
            l1_nums.append(cur.val)

        l2_nums = []
        cur = l2
        while cur:
            l2_nums.append(cur.val)

        l1_result = int("".join(l1_nums[::-1]))
        l2_result = int("".join(l2_nums[::-1]))
        result = str(l1_result+l2_result)

        head = ListNode(int(result[0]))
        cur = head
        for i in range(1, len(result)):
            n = ListNode(int(result[i]))
            cur.next = n

        return head


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        head = None
        cur = None
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            s = l1_val + l2_val + carry
            s, carry = s % 10, s // 10
            if head:
                new_head = ListNode(s)
                cur.next = new_head
                cur = new_head
            else:
                head = ListNode(s)
                cur = head

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            new_head = ListNode(carry)
            cur.next = new_head

        return head
