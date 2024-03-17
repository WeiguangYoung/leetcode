package main

import "strconv"

func crackNumber(ciphertext int) int {
	src := strconv.Itoa(ciphertext)
	a, b := 1, 1

	for i := 2; i <= len(src); i++ {
		tmp := src[i-2 : i]
		var c int
		if tmp >= "10" && tmp <= "25" {
			c = a + b
		} else {
			c = b
		}
		a = b
		b = c
	}
	return b
}
