class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0   # write position
        self.tail = 0   # read position
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def write(self, item):
        self.buffer[self.head] = item
        self.head = (self.head + 1) % self.capacity

        if self.size < self.capacity:
            self.size += 1
        else:
            # overwrite oldest -> move tail forward
            self.tail = (self.tail + 1) % self.capacity

    def read(self):
        if self.is_empty():
            raise IndexError("read from empty buffer")

        item = self.buffer[self.tail]
        self.tail = (self.tail + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.buffer[self.tail]
