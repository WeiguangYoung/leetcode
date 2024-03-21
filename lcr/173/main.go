package main

func takeAttendance(records []int) int {
	l, r := 0, len(records)-1

	for l < r {
		mid := (l + r) / 2
		if records[mid] == mid {
			l = mid
		} else {
			r = mid
		}
	}
	return l
}
