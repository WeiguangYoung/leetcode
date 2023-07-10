package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func getIntersectionNode(headA, headB *ListNode) *ListNode {
	mapping := map[*ListNode]bool{}
	for headA != nil {
		mapping[headA] = true
		headA = headA.Next
	}

	for headB != nil {
		if _, ok := mapping[headB]; ok {
			return headB
		}
		headB = headB.Next
	}

	return nil
}
