package main

import (
	"fmt"
)

type Node struct {
	Val    int
	Next   *Node
	Random *Node
}

func copyRandomList(head *Node) *Node {
	if head == nil {
		return nil
	}

	cur := head
	for cur != nil {
		newNode := &Node{
			Val: cur.Val,
		}

		newNode.Next = cur.Next
		cur.Next = newNode

		cur = cur.Next.Next
	}

	cur = head
	for cur != nil {
		if cur.Random != nil {
			cur.Next.Random = cur.Random.Next
		}
		cur = cur.Next.Next
	}

	res := head.Next
	newCur := res
	originCur := head
	for newCur.Next != nil {
		originCur.Next = newCur.Next
		newCur.Next = newCur.Next.Next

		newCur = newCur.Next
		originCur = originCur.Next
	}
	originCur.Next = nil

	return res
}

func printLinkNode(head *Node) {
	node := head
	for node != nil {
		fmt.Printf("value %d, random: %v \n", node.Val, node.Random)
		node = node.Next
	}

}

func main() {
	// [[7,null],[13,0],[11,4],[10,2],[1,0]]
	n0 := &Node{
		Val: 7,
	}
	n1 := &Node{
		Val: 13,
	}
	n2 := &Node{
		Val: 11,
	}
	n3 := &Node{
		Val: 10,
	}
	n4 := &Node{
		Val: 1,
	}

	n0.Next = n1

	n1.Next = n2
	n1.Random = n0

	n2.Next = n3
	n2.Random = n4

	n3.Next = n4
	n3.Random = n2

	n4.Random = n0

	fmt.Println("-------------")
	printLinkNode(n0)
	fmt.Println("-------------")

	newHead := copyRandomList(n0)

	fmt.Println("-------------")
	printLinkNode(newHead)
	fmt.Println("-------------")
	printLinkNode(n0)

}
