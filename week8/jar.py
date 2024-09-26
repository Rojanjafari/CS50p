class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return '🍪' * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError('number of cookies more than capacity')
        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError('n more than number of cookies')
        self.size -= n
        
    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if type(capacity) != int:
            raise ValueError('Invalid capacity')
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError('Size more than capacity')
        self._size = size