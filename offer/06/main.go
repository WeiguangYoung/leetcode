package main

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func reversePrint(head *ListNode) []int {
	var l []int

	for head != nil {
		l = append(l, head.Val)
		head = head.Next
	}
	reverse := func(a []int) {
		left := 0
		right := len(a) - 1
		for left < right {
			a[left], a[right] = a[right], a[left]
			left++
			right--
		}
	}
	reverse(l)
	return l
}

func main() {
	first := &ListNode{
		Val: 1,
	}
	second := &ListNode{
		Val: 3,
	}

	third := &ListNode{
		Val: 2,
	}
	first.Next = second
	second.Next = third

	res := reversePrint(first)
	for _, i := range res {
		println(i)
	}
}
