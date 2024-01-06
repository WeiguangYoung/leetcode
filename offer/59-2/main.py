import collections

class MaxQueue:
    def __init__(self):
        self.queue = collections.deque()
        self.max_queue = collections.deque()

    def max_value(self) -> int:
        if not self.max_queue:
            return -1
        return self.max_queue[0]

    def push_back(self, value: int) -> None:
        self.queue.append(value)

        while self.max_queue and self.max_queue[-1] < value:
            self.max_queue.pop()
        self.max_queue.append(value)

    def pop_front(self) -> int:
        if not self.queue:
            return -1

        if self.max_queue and self.max_queue[0] == self.queue[0]:
            self.max_queue.popleft()

        value = self.queue.popleft()
        return value


# Your MaxQueue object will be instantiated and called as such:
obj = MaxQueue()
obj.push_back(1)
obj.push_back(2)
obj.push_back(2)
print(obj.max_value())
param_2 = obj.pop_front()
print(param_2)
# param_1 = obj.push_back(22)
param_3 = obj.pop_front()
print(param_3)
print(obj.max_value())