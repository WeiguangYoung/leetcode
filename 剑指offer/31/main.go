package main

func validateStackSequences(pushed []int, popped []int) bool {

	tmp := []int{}
	x := 0
	for _, value := range pushed {
		tmp = append(tmp, value)

		for len(tmp) > 0 && tmp[len(tmp)-1] == popped[x] {
			tmp = tmp[:len(tmp)-1]
			x += 1
		}
	}
	return len(tmp) == 0
}
