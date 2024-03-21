package main

func findRepeatDocument(documents []int) int {
	i := 0

	for i < len(documents) {
		if documents[i] == i {
			i += 1
			continue
		}

		if documents[i] == documents[documents[i]] {
			return documents[i]
		}
		documents[i], documents[documents[i]] = documents[documents[i]], documents[i]
	}
	return -1
}
