package main

import (
	"log"
)

func movingCount(m int, n int, k int) int {
	getCnt := func(x int) int {
		r := 0
		for x > 0 {
			r += x % 10
			x = x / 10
		}
		return r
	}

	type point struct {
		x int
		y int
	}

	start_p := point{x: 0, y: 0}
	q := map[point]bool{
		start_p: true,
	}

	set := []point{
		start_p,
	}

	for len(set) > 0 {
		p := set[0]
		set = set[1:]

		if p.x >= 0 && p.x < m && p.y >= 0 && p.y < n && getCnt(p.x)+getCnt(p.y) <= k {
			q[p] = true
			set = append(set, point{p.x + 1, p.y})
			set = append(set, point{p.x, p.y + 1})
		}
	}

	return len(q)
}

func main() {
	log.Println(movingCount(2, 3, 1))
}
