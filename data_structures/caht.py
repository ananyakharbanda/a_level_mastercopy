class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class DLL():
    def __init__(self):
        self.root = None
    
    def insert_back(self, key, value):
        n = Node(key, value)
        curr = self.root
        if curr is None:
            self.root = n
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = n

    def insert_front(self, key, value):  # Insert key-value pair at the front
        n = Node(key, value)
        if self.root is None:
            self.root = n
        else:
            n.next = self.root
            self.root = n

    def delete(self, key):  # Delete a node by its key
        if self.root is not None:
            prev = None
            curr = self.root
            while curr is not None and curr.key != key:
                prev = curr
                curr = curr.next
            if curr is None:
                print('Key not found')
            else:
                if prev is None:
                    self.root = curr.next
                else:
                    prev.next = curr.next

    def search(self, key):  # Search for a node by key
        curr = self.root
        while curr is not None:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return None

    def print_in_order(self):  # Print the list in order
        result = []
        curr = self.root
        while curr is not None:
            result.append(f"({curr.key}, {curr.value})")
            curr = curr.next
        return ' -> '.join(result) if result else "Empty"

class CAHT:
    def __init__(self, maxsize=20):
        self.maxsize = maxsize
        self.caht = [DLL() for _ in range(self.maxsize)]  # Use DLL instead of LinkedList

    def hash(self, key):
        return key % self.maxsize

    def insert(self, key, value):
        hashed = self.hash(key)
        self.caht[hashed].insert_back(key, value)

    def delete(self, key):
        hashed = self.hash(key)
        self.caht[hashed].delete(key)

    def search(self, key):
        hashed = self.hash(key)
        return self.caht[hashed].search(key)

    def display(self):
        for i in range(self.maxsize):
            print(f"Index {i}: {self.caht[i].print_in_order()}")


# Create a hash table with chaining using DLL
hash_table = CAHT(maxsize=10)

# Insert key-value pairs
hash_table.insert(10, "Value10")
hash_table.insert(20, "Value20")
hash_table.insert(15, "Value15")
hash_table.insert(25, "Value25")

# Display the hash table
hash_table.display()

# Search for a key
print("Search for key 15:", hash_table.search(15))  # Output: Value15

# Delete a key
hash_table.delete(20)

# Display the hash table again after deletion
hash_table.display()



