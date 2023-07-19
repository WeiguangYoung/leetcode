package main

func spiralOrder(matrix [][]int) []int {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return []int{}
	}
	row, column := len(matrix), len(matrix[0])
	visited := make([][]bool, row)
	for i := range visited {
		visited[i] = make([]bool, column)
	}

	total := row * column
	directions := [][]int{
		[]int{0, 1},
		[]int{1, 0},
		[]int{0, -1},
		[]int{-1, 0},
	}
	directIdx := 0
	r, c := 0, 0
	result := make([]int, total)

	for i := 0; i < total; i++ {
		result[i] = matrix[r][c]
		visited[r][c] = true
		nextRow, nextCol := r+directions[directIdx][0], c+directions[directIdx][1]
		if (nextCol < 0 || nextCol >= column || nextRow < 0 || nextRow >= row) || (visited[nextRow][nextCol]) {
			directIdx = (directIdx + 1) % 4
		}
		r += directions[directIdx][0]
		c += directions[directIdx][1]
	}

	return result
}

func main() {
	m := [][]int{}
	spiralOrder(m)
}
