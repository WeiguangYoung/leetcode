package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isBalanced(root *TreeNode) bool {
	if root == nil {
		return true
	}

	maxDepth := func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		depth := 1
		nodes := []*TreeNode{node}

		for len(nodes) > 0 {
			length := len(nodes)
			for _, node := range nodes {
				if node.Left != nil {
					nodes = append(nodes, node.Left)
				}
				if node.Right != nil {
					nodes = append(nodes, node.Right)
				}
			}
			if len(nodes) > length {
				depth += 1
			}
			nodes = nodes[length:]

		}

		return depth
	}

	s := maxDepth(root.Left) - maxDepth(root.Right)
	return (s <= 1 && s >= -1) && isBalanced(root.Left) && isBalanced(root.Right)
}
