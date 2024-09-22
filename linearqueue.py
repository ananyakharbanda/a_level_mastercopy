
class Queue():
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.queue = ['' for _ in range(self.maxsize)]
        self.front = 0
        self.rear = -1
    
    def isEmpty(self):
        return self.front > self.rear
    
    def isFull(self):
        return self.rear - self.front + 1 == self.maxsize
    
    def enqueue(self, data):
        if not self.isFull():
            self.rear += 1
            self.queue[self.rear] = data
       
    def dequeue(self):
        if not self.isEmpty():
            temp = self.queue[self.front]
            self.front += 1
            return temp
        return None
    
    def size(self):
        if not self.isEmpty():
            return self.rear - self.front + 1
        else:
            return 0
    
    def display(self):
        if not self.isEmpty():
            return self.queue[self.front:self.rear + 1]


# Test Cases for Queue Class

# Initialize a Queue with a maximum size of 5
queue = Queue(5)

# Test isEmpty() - should be True
print("Is the queue empty?", queue.isEmpty())  # Expected: True

# Enqueue elements
queue.enqueue("Task 1")
queue.enqueue("Task 2")
queue.enqueue("Task 3")

# Test isEmpty() - should be False
print("Is the queue empty?", queue.isEmpty())  # Expected: False

# Test size() - should be 3
print("Current size of the queue:", queue.size())  # Expected: 3

# Display the queue
print("Current queue:", queue.display())  # Expected: ['Task 1', 'Task 2', 'Task 3']

# Enqueue more elements
queue.enqueue("Task 4")
queue.enqueue("Task 5")

# Test isFull() - should be True
print("Is the queue full?", queue.isFull())  # Expected: True

# Try to enqueue another element (should not be added)
queue.enqueue("Task 6")
print("Current queue after trying to enqueue another task:", queue.display())  # Expected: ['Task 1', 'Task 2', 'Task 3', 'Task 4', 'Task 5']

# Dequeue elements
print("Dequeued:", queue.dequeue())  # Expected: 'Task 1'
print("Dequeued:", queue.dequeue())  # Expected: 'Task 2'

# Display the queue
print("Current queue after dequeuing:", queue.display())  # Expected: ['Task 3', 'Task 4', 'Task 5']

# Check the size after dequeuing
print("Current size of the queue:", queue.size())  # Expected: 3

# Dequeue until the queue is empty
print("Dequeued:", queue.dequeue())  # Expected: 'Task 3'
print("Dequeued:", queue.dequeue())  # Expected: 'Task 4'
print("Dequeued:", queue.dequeue())  # Expected: 'Task 5'

# Test isEmpty() - should be True
print("Is the queue empty?", queue.isEmpty())  # Expected: True

# Test dequeue on an empty queue (should return None)
print("Dequeued from empty queue:", queue.dequeue())  # Expected: None
