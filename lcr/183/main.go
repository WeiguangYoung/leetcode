package main

func maxAltitude(heights []int, limit int) []int {
	if len(heights) == 0 && limit == 0 {
		return []int{}
	}
	deque := []int{}
	var i int
	for ; i < limit; i++ {
		for len(deque) > 0 && heights[i] > deque[len(deque)-1] {
			deque = deque[:len(deque)-1]
		}
		deque = append(deque, heights[i])
	}
	results := []int{deque[0]}
	for ; i < len(heights); i++ {
		if heights[i-limit] == deque[0] {
			deque = deque[1:]
		}

		for len(deque) > 0 && heights[i] > deque[len(deque)-1] {
			deque = deque[:len(deque)-1]
		}

		deque = append(deque, heights[i])
		results = append(results, deque[0])
	}

	return results
}

func main() {

}
