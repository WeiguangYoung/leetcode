package main

import "strings"

func reverseLeftWords(s string, n int) string {
	length := len(s)
	s2 := make([]string, length)

	for i, v := range s {
		if i < n {
			s2[i+length-n] = string(v)
		} else {
			s2[i-n] = string(v)
		}
	}
	return strings.Join(s2, "")
}

func main() {

}
