package leetcode

import "sort"

func arrayRankTransform(arr []int) []int {
	a := make([]int, len(arr))
	copy(a, arr)
	sort.Ints(a)

	ranks := map[int]int{}
	for _, i := range a {
		if _, ok := ranks[i]; !ok {
			ranks[i] = len(ranks)+1
		}
	}
	for i, value := range arr {
		arr[i] = ranks[value]
	}

	return arr
}

