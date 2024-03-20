class MaxQueue:
    def __init__(self):
        self.queue = []
        self.max_queue = []

    def max_value(self) -> int:
        if not self.max_queue:
            return -1
        return self.max_queue[0]

    def push_back(self, value: int) -> None:
        self.queue.append(value)

        while self.max_queue and self.max_queue[-1] < value:
            self.max_queue = self.max_queue[:-1]
        self.max_queue.append(value)

    def pop_front(self) -> int:
        if not self.queue:
            return -1

        while self.max_queue and self.max_queue[0] == self.queue[0]:
            self.max_queue = self.max_queue[1:]

        value = self.queue[0]
        self.queue = self.queue[1:]
        return value