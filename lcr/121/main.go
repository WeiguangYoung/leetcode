package main

func findTargetIn2DPlants(plants [][]int, target int) bool {
	if len(plants) == 0 {
		return false
	}
	if len(plants[0]) == 0 {
		return false
	}
	i, j := 0, len(plants[0])-1
	for i <= len(plants)-1 && j >= 0 {
		if plants[i][j] > target {
			j--
		} else if plants[i][j] < target {
			i++
		} else {
			return true
		}
	}
	return false
}
