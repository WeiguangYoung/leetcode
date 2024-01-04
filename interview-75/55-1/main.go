package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	depth := 1
	nodes := []*TreeNode{root}

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
