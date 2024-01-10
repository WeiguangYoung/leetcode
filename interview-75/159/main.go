package main

import (
	"container/heap"
)

type IntHeap []int

func (h IntHeap) Len() int {
	return len(h)
}

func (h IntHeap) Less(i, j int) bool {
	return h[i] < h[j]
}

func (h IntHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)

	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func (h *IntHeap) Push(x interface{}) { // 绑定push方法，插入新元素
	*h = append(*h, x.(int))
}

func inventoryManagement(stock []int, cnt int) []int {
	if cnt == 0 {
		return []int{}
	}

	h := &IntHeap{}
	for _, s := range stock[:cnt] {
		heap.Push(h, -s)
	}

	heap.Init(h)

	for _, s := range stock[cnt:] {
		v := heap.Pop(h)
		if v.(int) < (-s) {
			heap.Push(h, -s)
		} else {
			heap.Push(h, v)
		}
	}

	results := make([]int, cnt)
	for i, s := range *h {
		results[i] = -s
	}
	return results
}
