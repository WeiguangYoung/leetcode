package main

func validateBookSequences(putIn []int, takeOut []int) bool {
	i := 0
	stack := []int{}

	for _, num := range putIn {
		stack = append(stack, num)

		for len(stack) > 0 && stack[len(stack)-1] == takeOut[i] {
			stack = stack[:len(stack)-1]
			i += 1
		}
	}
	return len(stack) == 0
}
