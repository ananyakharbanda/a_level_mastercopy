class Node():
    def __init__(self):
        self.data = ''  # Changed to empty string instead of 'zz'
        self.pointer = -1

    def __repr__(self):
        return "pointer: " + str(self.pointer) + ", data: " + self.data
    
class LinkedList():
    def __init__(self, maxsize=5):
        self.maxsize = maxsize
        self.nodes = [Node() for _ in range(self.maxsize)]
        self.start = -1
        self.nextfree = 0
        for i in range(self.maxsize-1):
            self.nodes[i].pointer = i + 1
    
    def insert(self, data):
        if self.nextfree == -1:
            print("list is full")
            return 
        else:
            self.nodes[self.nextfree].data = data
            if self.start == -1:
                temp = self.nodes[self.nextfree].pointer
                self.nodes[self.nextfree].pointer = -1
                self.start = self.nextfree
                self.nextfree = temp
            else:
                prev = -1
                curr = self.start
                while curr != -1 and self.nodes[curr].data < data:
                    prev = curr
                    curr = self.nodes[curr].pointer
                if curr == self.start:
                    temp = self.nodes[self.nextfree].pointer
                    self.nodes[self.nextfree].pointer = curr
                    self.start = self.nextfree
                    self.nextfree = temp
                else:
                    temp = self.nodes[self.nextfree].pointer
                    self.nodes[prev].pointer = self.nextfree
                    self.nodes[self.nextfree].pointer = curr
                    self.nextfree = temp

    def find(self, data, log=True):
        if self.start == -1:
            if log:
                print('list is empty')
            return (-1, -1, False)
        else:
            prev = -1
            curr = self.start
            found = False
            while curr != -1 and self.nodes[curr].data != data:
                prev = curr
                curr = self.nodes[curr].pointer
            if curr == -1 or self.nodes[curr].data != data:  # Add check if curr becomes -1
                if log:
                    print('not found')
                return (-1, -1, False)
            found = True
            if found:
                if log:
                    print("data found at {}".format(curr))
                return (prev, curr, True)
    
    def find_short(self, data):
        curr = self.start
        while curr != -1 and data > self.nodes[curr].data:
            curr = self.nodes[curr].pointer
        if curr == -1 or data != self.nodes[curr].data:
            print('data not found!')
            return False
        else:
            return True

    def find_short_rec(self, data, root):
        if root == -1:  # Base case: empty or end of list
            return False
        if self.nodes[root].data == data:
            return True
        elif self.nodes[root].data > data:
            return False
        else:
            p = self.nodes[root].pointer
            return self.find_short_rec(data, p)  # Return the recursive call result

    def delete(self, data, log=False):
        prev, curr, found = self.find(data, log)
        if found:
            if curr == self.start:
                temp = self.nodes[self.start].pointer
                self.start = temp
            self.nodes[curr].data = ''  # Changed to empty string
            self.nodes[prev].pointer = self.nodes[curr].pointer
            self.nodes[curr].pointer = self.nextfree
            self.nextfree = curr 

    def printlist(self):
        curr = self.start
        while curr != -1:
            print(self.nodes[curr].data)
            curr = self.nodes[curr].pointer
    

# Testing the LinkedList
ll = LinkedList(5)
ll.insert('paras')
ll.insert('ananya')
ll.insert('neha')
ll.insert('hello')
ll.insert('dadi')
ll.insert('aymon')
ll.printlist()

print('---------')
ll.delete('hello')
ll.insert('aymon')
ll.printlist()

print(ll.find_short_rec('asdkfls', ll.start))
