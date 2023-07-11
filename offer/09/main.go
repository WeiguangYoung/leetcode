package main

import "log"

type CQueue struct {
	inStack, outStack []int
}

func Constructor() CQueue {
	return CQueue{
		inStack:  []int{},
		outStack: []int{},
	}
}

func (this *CQueue) AppendTail(value int) {
	this.inStack = append(this.inStack, value)
}

func (this *CQueue) DeleteHead() int {
	if len(this.outStack) == 0 {
		if len(this.inStack) == 0 {
			return -1
		}

		for len(this.inStack) > 0 {
			this.outStack = append(this.outStack, this.inStack[len(this.inStack)-1])
			this.inStack = this.inStack[:len(this.inStack)-1]
		}
	}
	value := this.outStack[len(this.outStack)-1]
	this.outStack = this.outStack[:len(this.outStack)-1]
	return value
}

func main() {

	obj := Constructor()
	obj.AppendTail(1)
	param_2 := obj.DeleteHead()
	log.Println(param_2)

}
