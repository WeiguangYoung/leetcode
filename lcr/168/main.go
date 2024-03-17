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

func nthUglyNumber(n int) int {
	factors := []int{2, 3, 5}
	seen := map[int]bool{}
	h := &IntHeap{}
	heap.Push(h, 1)
	heap.Init(h)

	for i := 0; i < n-1; i++ {
		cur := heap.Pop(h)
		for _, f := range factors {
			curNum := cur.(int)
			if _, ok := seen[curNum*f]; !ok {
				seen[curNum*f] = true
				heap.Push(h, curNum*f)
			}
		}
	}
	res := heap.Pop(h)
	return res.(int)
}
