class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A, self.B = [], []

    def push(self, x: int) -> None:
        self.A.append(x)

        if not self.B or self.B[-1] >= x:
            self.B.append(x)

    def pop(self) -> None:
        value = self.A.pop()

        if self.B[-1] == value:
            self.B.pop()

    def top(self) -> int:
        if self.A:
            return self.A[-1]

    def getMin(self) -> int:
        if self.B:
            return self.B[-1]

        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()
