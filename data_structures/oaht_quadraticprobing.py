class OAHTQuadratic():
    def __init__(self, maxsize=20, c1=1, c2=3):
        self.maxsize = maxsize
        self.oaht = [[None, None] for _ in range(self.maxsize)]  # Table to store key-value pairs
        self.deleted = ["DELETED", "DELETED"]  # Marker for deleted items
        self.c1 = c1  # Coefficient for the linear term
        self.c2 = c2  # Coefficient for the quadratic term

    def hash(self, key):
        return key % self.maxsize

    def rehash(self, key, step):
        return (key + self.c1 * step + self.c2 * (step ** 2)) % self.maxsize

    def insert(self, key, value):
        hashed = self.hash(key)
        step = 0
        while step < self.maxsize:
            if self.oaht[hashed] == [None, None] or self.oaht[hashed] == self.deleted:
                self.oaht[hashed] = [key, value]  # Insert key-value pair
                return
            else:
                step += 1
                hashed = self.rehash(key, step)  # Quadratic probing
        print("Table is full, cannot insert more items")

    def delete(self, key):
        hashed = self.hash(key)
        step = 0
        while step < self.maxsize:
            if self.oaht[hashed][0] == key:
                print(f'Key {self.oaht[hashed][0]} with value {self.oaht[hashed][1]} deleted')
                self.oaht[hashed] = self.deleted  # Mark the slot as deleted
                return
            else:
                step += 1
                hashed = self.rehash(key, step)
        print('Key not found')

    def find(self, key):
        hashed = self.hash(key)
        step = 0
        while step < self.maxsize:
            if self.oaht[hashed][0] == key:
                print(f'Key: {self.oaht[hashed][0]}, Value: {self.oaht[hashed][1]}')
                return self.oaht[hashed][1]
            elif self.oaht[hashed] == [None, None]:
                break  # Stop searching if we hit an empty slot (key not present)
            else:
                step += 1
                hashed = self.rehash(key, step)
        print('Key not found')
        return None

# Example usage
oaht = OAHTQuadratic(5)  # Small table size to demonstrate collisions
oaht.insert(1, 'ananya')
oaht.insert(6, 'neha')  # Causes a collision, will use quadratic probing
oaht.insert(11, 'paras')  # Another collision, will use quadratic probing

print("Table after insertion:", oaht.oaht)

# Test find
oaht.find(1)
oaht.find(6)
oaht.find(11)

# Test delete
oaht.delete(6)
print("Table after deletion:", oaht.oaht)

# Insert after delete
oaht.insert(16, 'reshma')  # Will probe using quadratic probing
print("Table after new insertion:", oaht.oaht)
