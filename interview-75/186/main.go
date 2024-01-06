package main

import "sort"

func checkDynasty(places []int) bool {
	sort.Ints(places)

	idx := -1
	for i, place := range places {
		if place == 0 {
			idx = i
			continue
		}
		if i < 4 && places[i] == places[i+1] {
			return false
		}
	}
	if idx == 4 {
		return true
	}
	return places[4]-places[idx+1] < 5
}
