class MaxHeap:
    def __init__(self, nums: list):
        """构造方法，根据输入列表建堆"""
        # 将列表元素原封不动添加进堆
        self.max_heap = nums
        # 堆化除叶节点以外的其他所有节点
        for i in range(self.parent(self.size() - 1), -1, -1):
            self.sift_down(i)

    def left(self, i: int) -> int:
        """获取左子节点的索引"""
        return 2 * i + 1

    def right(self, i: int) -> int:
        """获取右子节点的索引"""
        return 2 * i + 2

    def parent(self, i: int) -> int:
        """获取父节点的索引"""
        return (i - 1) // 2  # 向下整除

    def peek(self) -> int:
        """访问堆顶元素"""
        return self.max_heap[0]

    def is_empty(self) -> bool:
        """访问堆顶元素"""
        return self.size() == 0

    def size(self) -> int:
        """获取堆栈长度"""
        return len(self.max_heap)

    def push(self, val: int):
        """元素入堆"""
        # 添加节点
        self.max_heap.append(val)
        # 从底至顶堆化
        self.sift_up(self.size()-1)

    def swap(self, i: int, j: int):
        self.max_heap[i], self.max_heap[j] = self.max_heap[j], self.max_heap[i]

    def sift_up(self, i: int):
        """从节点 i 开始，从底至顶堆化"""
        while True:
            p = self.parent(i)
            if p < 0 or self.max_heap[i] <= self.max_heap[p]:
                break

            self.swap(i, p)
            i = p

    def pop(self) -> int:
        """元素出堆"""
        # 判空处理
        if self.is_empty():
            raise IndexError("堆为空")

        self.swap(0, self.size() - 1)

        val = self.max_heap.pop()
        self.sift_down(0)
        return val

    def sift_down(self, i: int):
        while True:
            l, r, m = self.left(i), self.right(i), i

            if l < self.size() and self.max_heap[l] > self.max_heap[i]:
                m = l
            if l < self.size() and self.max_heap[r] > self.max_heap[i]:
                m = r

            if m == i:
                break

            self.swap(i, m)
            i = m
