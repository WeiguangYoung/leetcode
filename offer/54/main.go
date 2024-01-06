package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func kthLargest(root *TreeNode, k int) int {
	var result int
	var dfs func(*TreeNode)
	dfs = func(root *TreeNode) {
		if root == nil {
			return
		}

		dfs(root.Right)

		if k == 0 {
			return
		}
		k--
		if k == 0 {
			result = root.Val
			return
		}
		dfs(root.Left)
	}
	dfs(root)
	return result
}
