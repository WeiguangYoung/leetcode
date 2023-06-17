package main

import "strings"

func replaceSpace(s string) string {
	var s2 []string
	for _, i := range s {
		if i == ' ' {
			s2 = append(s2, "%20")
		} else {
			s2 = append(s2, string(i))
		}
	}

	return strings.Join(s2, "")
}

func main() {

}
