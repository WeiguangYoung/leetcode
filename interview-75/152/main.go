package main

import "math"

func verifyTreeOrder(postorder []int) bool {
	root := math.Inf(1)
	stack := []float64{}

	for i := len(postorder) - 1; i >= 0; i-- {
		if float64(postorder[i]) > root {
			return false
		}
		for len(stack) != 0 && float64(postorder[i]) < stack[len(stack)-1] {
			root = stack[len(stack)-1]
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, float64(postorder[i]))
	}
	return true
}

func main() {
	values := []int{4,9,6,5,8}

	verifyTreeOrder((values))

}
