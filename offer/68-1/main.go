package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	if p.Val < root.Val && q.Val < root.Val {
		return lowestCommonAncestor(root.Left, p, q)
	}
	if p.Val > root.Val && q.Val > root.Val {
		return lowestCommonAncestor(root.Right, p, q)
	}
	return root
}
func lowestCommonAncestor2(root, p, q *TreeNode) *TreeNode {
	var getPath func(node *TreeNode) []*TreeNode

	getPath = func(node *TreeNode) []*TreeNode {
		cur := root
		path := []*TreeNode{}
		for cur != nil {
			path = append(path, cur)
			if node.Val > cur.Val {
				cur = cur.Right
			} else if node.Val < cur.Val {
				cur = cur.Left
			} else {
				break
			}
		}
		return path
	}
	pPath := getPath(p)
	qPath := getPath(q)

	target := root
	for i := 0; i < len(pPath) && i < len(qPath); i++ {
		if pPath[i].Val == qPath[i].Val {
			target = pPath[i]
		}
	}
	return target
}