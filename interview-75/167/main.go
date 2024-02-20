package main

func dismantlingAction(arr string) int {
	m := map[byte]int{}
	res := 0
	i := -1

	for j := 0; j < len(arr); j++ {
		if _, ok := m[arr[j]]; ok && m[arr[j]] > i {
			i = m[arr[j]]
		}

		m[arr[j]] = j
		if j-i > res {
			res = j - i
		}
	}
	return res
}
