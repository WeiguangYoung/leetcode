package main

type Checkout struct {
	Queue    []int
	MaxQueue []int
}

func Constructor() Checkout {
	return Checkout{
		Queue:    []int{},
		MaxQueue: []int{},
	}
}

func (this *Checkout) Get_max() int {
	if len(this.Queue) == 0 {
		return -1
	}
	return this.MaxQueue[0]
}

func (this *Checkout) Add(value int) {
	this.Queue = append(this.Queue, value)

	for len(this.MaxQueue) > 0 && value > this.MaxQueue[len(this.MaxQueue)-1] {
		this.MaxQueue = this.MaxQueue[:len(this.MaxQueue)-1]
	}
	this.MaxQueue = append(this.MaxQueue, value)
}

func (this *Checkout) Remove() int {
	if len(this.Queue) == 0 {
		return -1
	}
	value := this.Queue[0]
	this.Queue = this.Queue[1:]

	if len(this.MaxQueue) > 0 && value == this.MaxQueue[0] {
		this.MaxQueue = this.MaxQueue[1:]
	}

	return value
}
