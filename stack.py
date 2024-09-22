class Stack:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.top = -1
        self.stack = [None] * self.maxsize  # Use None instead of an empty string

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.maxsize - 1

    def pop(self):
        if not self.is_empty():
            element = self.stack[self.top]
            self.top -= 1
            return element  # Return the popped element
        return None  # Return None if the stack is empty

    def push(self, element):
        if not self.is_full():
            self.top += 1
            self.stack[self.top] = element

    def peek(self):
        if not self.is_empty():
            return self.stack[self.top]
        return None  # Return None if the stack is empty

    def size(self):
        return self.top + 1

    def remaining(self):
        return self.maxsize - self.size()  # Remaining capacity

# Test Cases
def test_stack():
    stack = Stack(5)

    # Test push and size
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack after pushing 1, 2, 3:")
    print("Top element:", stack.peek())  # Output: 3
    print("Stack size:", stack.size())    # Output: 3
    print("Remaining capacity:", stack.remaining())  # Output: 2

    # Test pop
    print("Popped element:", stack.pop())  # Output: 3
    print("Stack size after pop:", stack.size())  # Output: 2

    # Test peek
    print("Top element after pop:", stack.peek())  # Output: 2

    # Test popping all elements
    print("Popped element:", stack.pop())  # Output: 2
    print("Popped element:", stack.pop())  # Output: 1
    print("Stack size after popping all:", stack.size())  # Output: 0
    print("Top element after popping all:", stack.peek())  # Output: None

    # Test push to full stack
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    print("Stack after pushing 4, 5, 6, 7:")
    print("Top element:", stack.peek())  # Output: 7
    print("Stack size:", stack.size())    # Output: 4
    print("Remaining capacity:", stack.remaining())  # Output: 1

    # Pop until empty
    while not stack.is_empty():
        print("Popped element:", stack.pop())  # Output: 7, 6, 5, 4
    print("Stack size after popping all:", stack.size())  # Output: 0

test_stack()
