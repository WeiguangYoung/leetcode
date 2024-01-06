class CQueue:

    def __init__(self):
        # 模拟两个栈，只能使用append和pop方法
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B:
            return self.B.pop()

        if not self.A:
            return -1

        while self.A:
            self.B.append(self.A.pop())

        return self.B.pop()


# Your CQueue object will be instantiated and called as such:
obj = CQueue()
obj.appendTail(1)
obj.appendTail(2)
obj.appendTail(3)
param_2 = obj.deleteHead()
print(param_2)
param_2 = obj.deleteHead()
print(param_2)
param_2 = obj.deleteHead()
print(param_2)
