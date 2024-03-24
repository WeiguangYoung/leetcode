package main

func stockManagement(stock []int) int {
	l, r := 0, len(stock)-1

	for l < r {
		m := (l + r) / 2
		if stock[m] < stock[l] {
			r = m
		} else if stock[m] > stock[l] {
			l += 1
		} else {
			r -= 1
		}
	}
	return stock[l]
}
