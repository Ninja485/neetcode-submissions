class DynamicArray:
    list = []
    max_size = 0
    def __init__(self, capacity: int):
        self.list = []
        self.max_size = capacity

    def get(self, i: int) -> int:
        return self.list[i]

    def set(self, i: int, n: int) -> None:
        self.list[i] = n

    def pushback(self, n: int) -> None:
        if len(self.list) == self.max_size:
            self.resize()
        self.list.append(n)

    def popback(self) -> int:
        return self.list.pop()

    def resize(self) -> None:
        self.max_size = 2*self.max_size

    def getSize(self) -> int:
        return len(self.list)
    
    def getCapacity(self) -> int:
        return self.max_size
