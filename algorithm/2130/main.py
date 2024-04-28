from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next


class Solution:
    # def pairSum(self, head: Optional[ListNode]) -> int:
    #     cur = head

    #     nums = []
    #     while cur:
    #         nums.append(cur.val)
    #         cur = cur.next

    #     ans = 0
    #     n = len(nums)
    #     for i in range(n//2):
    #         ans = max(ans, nums[i]+nums[n-1-i])
    #     return ans

    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head.next
        while fast.next:
            slow = slow.next
            fast = fast.next.next

        pre = None
        cur = slow.next
        while cur:
            next = cur.next
            cur.next = pre

            pre = cur
            cur = next

        ans = 0
        x, y = head, pre
        while y:
            ans = max(ans, x.val+y.val)
            x = x.next
            y = y.next

        return ans
