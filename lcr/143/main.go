package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSubStructure(A *TreeNode, B *TreeNode) bool {
	var recur func(*TreeNode, *TreeNode) bool

	recur = func(x *TreeNode, y *TreeNode) bool {
		if y == nil {
			return true
		}
		if x == nil || x.Val != y.Val {
			return false
		}
		return recur(x.Left, y.Left) && recur(x.Right, y.Right)
	}

	return (A != nil && B != nil) && (recur(A, B) || isSubStructure(A.Left, B) || isSubStructure(A.Right, B))
}
