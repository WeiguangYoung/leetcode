package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSymmetric(root *TreeNode) bool {
	queue := []*TreeNode{
		root,
		root,
	}
	for len(queue) > 0 {
		a, b := queue[0], queue[1]
		queue = queue[2:]

		if a == nil && b == nil {
			continue
		}
		if a == nil || b == nil {
			return false
		}
		if a.Val != b.Val {
			return false
		}

		queue = append(queue, a.Left, b.Right, b.Left, a.Right)
	}
	return true
}

func main() {
	isSymmetric(nil)
}
