

class CircularQueue():
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.cq = ['' for _ in range(self.maxsize)]
        self.front = 0
        self.size = 0
        self.rear = self.maxsize - 1
    
    def isEmpty(self):
        return self.size == 0  
    
    def isFull(self):
        return self.size == self.maxsize
    
    def enqueue(self, data):
        if not self.isFull():
            if self.rear == self.maxsize - 1:
                self.rear = 0
            else:
                self.rear += 1
            self.cq[self.rear] = data
            self.size += 1

    def dequeue(self):
        if not self.isEmpty():
            data = self.cq[self.front]
            self.size -= 1
            if self.front == self.maxsize - 1:
                self.front = 0
            else:
                self.front += 1
            return data
        return None

# Test Cases for CircularQueue

cq = CircularQueue(5)

# Test case 1: Enqueue elements
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
assert cq.isFull() == True  # Queue should be full
print("Enqueue Test Passed")

# Test case 2: Dequeue elements
assert cq.dequeue() == 1  # Dequeue 1
assert cq.dequeue() == 2  # Dequeue 2
print("Dequeue Test Passed")

# Test case 3: Enqueue after dequeue
cq.enqueue(6)
cq.enqueue(7)
assert cq.isFull() == True  # Queue should be full again
print("Re-enqueue Test Passed")

# Test case 4: Dequeue until empty
while not cq.isEmpty():
    cq.dequeue()
assert cq.isEmpty() == True  # Queue should be empty
print("Empty Queue Test Passed")
