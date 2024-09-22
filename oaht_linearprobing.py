

class OAHT():
    def __init__(self, maxsize=20):
        self.maxsize = maxsize
        self.oaht = [[None, None] for _ in range(self.maxsize)]

    def hash(self, key):
        hashed = key % self.maxsize
        return hashed

    def rehash(self, key):
        rehashed = (key+1) % self.maxsize
        return rehashed
 
    def insert(self, key, value):
        hashed = self.hash(key)
        count = 0
        tempkey = key
        while count < self.maxsize:
            if self.oaht[hashed] == [None, None]:
                self.oaht[hashed][0] = key
                self.oaht[hashed][1] = value
                return
            else:
                hashed = self.rehash(tempkey)
                count += 1
                tempkey += 1
    
    def delete(self, key):
        hashed = self.hash(key)
        count = 0
        tempkey = key
        while count < self.maxsize:
            if self.oaht[hashed][0] == key:
                print('key {} value {} deleted'.format(self.oaht[hashed][0], self.oaht[hashed][1]))
                self.oaht[hashed][0] = None
                self.oaht[hashed][1] = None
                return
            else:
                hashed = self.rehash(tempkey)
                count += 1
                tempkey += 1
        print('key value pair not found')

    def find(self, key):
        hashed = self.hash(key)
        count = 0
        tempkey = key
        while count < self.maxsize:
            if self.oaht[hashed][0] == key:
                print('key: {}, value {}'.format(self.oaht[hashed][0], self.oaht[hashed][1]))
                return self.oaht[hashed][1]
            else:
                hashed = self.rehash(tempkey)
                count += 1
                tempkey += 1
        print('key value not found')
        return None
    

oaht = OAHT(3)
oaht.insert(1, 'ananya')
oaht.insert(2, 'neha')
oaht.insert(4, 'paras')
print(oaht.oaht)
