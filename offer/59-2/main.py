class MaxQueue:
    def __init__(self):
        self.queue = []
        self.max_queue = []

    def max_value(self) -> int:
        if self.max_queue:
            return self.max_queue[-1]
        return -1

    def push_back(self, value: int) -> None:
        self.queue.append(value)

        if not self.max_queue:
            self.max_queue.append(value)
        elif self.max_queue[-1] <= value:
            self.max_queue.append(value)

    def pop_front(self) -> int:
        if not self.queue:
            return -1

        if self.max_queue and self.max_queue[-1] == self.queue[0]:
            self.max_queue = self.max_queue[:-1]

        value = self.queue[0]
        self.queue = self.queue[1:]
        return value


# Your MaxQueue object will be instantiated and called as such:
obj = MaxQueue()
obj.push_back(96)
obj.push_back(16)
obj.push_back(89)
param_2 = obj.pop_front()
print(param_2)
param_1 = obj.push_back(22)
param_3 = obj.pop_front()
print(param_3)
