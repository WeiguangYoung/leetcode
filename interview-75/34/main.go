package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type pair struct {
	node *TreeNode
	rest int
}

func pathSum(root *TreeNode, target int) [][]int {
	results := [][]int{}
	if root == nil {
		return results
	}
	parent := map[*TreeNode]*TreeNode{}
	getPath := func(node *TreeNode) (path []int) {
		for ; node != nil; node = parent[node] {
			path = append(path, node.Val)
		}
		for i, j := 0, len(path)-1; i < j; {
			path[i], path[j] = path[j], path[i]
			j--
			i++
		}
		return path
	}

	queue := []pair{{root, target}}
	for len(queue) > 0 {
		p := queue[0]
		queue = queue[1:]

		rest := p.rest - p.node.Val
		if p.node.Left == nil && p.node.Right == nil {
			if rest == 0 {
				results = append(results, getPath(p.node))
			}
		} else {
			if p.node.Left != nil {
				parent[p.node.Left] = p.node
				queue = append(queue, pair{p.node.Left, rest})
			}
			if p.node.Right != nil {
				parent[p.node.Right] = p.node
				queue = append(queue, pair{p.node.Right, rest})
			}
		}
	}

	return results
}
