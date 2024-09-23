

class Node():
    def __init__(self, data):
        self.next = None
        self.data = data

class DLL():
    def __init__(self):
        self.root = None
    
    def insert_back(self, data):
        n = Node(data)
        curr = self.root
        if curr == None:
            self.root = n
        
        else:
            while curr.next != None:
                curr = curr.next
            curr.next = n

    
    def insert_front(self, data): # push from stack
        n = Node(data)
        if self.root == None:
            self.root = n
        else:
            n.next = self.root
            self.root = n

    def pop_front(self):
        if self.root is not None:
            n = self.root
            self.root = n.next
            return n.data
    
    def pop_back(self):
        if self.root is not None:
            prev = None
            curr = self.root
            while curr.next is not None:
                prev = curr
                curr = curr.next
            prev.next = None
            return curr.data

    def delete(self, data):
        if self.root is not None:
            prev = None
            curr = self.root
            while curr != None and curr.data != data:
                prev = curr
                curr = curr.next
            if curr == None:
                print('data not found')
            else:
                if prev == None:
                    self.root = curr.next
                else:
                    prev.next = curr.next

    def print(self):
        curr = self.root
        while curr != None:
            print(curr.data)
            curr = curr.next

x = DLL()
x.insert_front(1)
x.insert_front('a')
x.insert_front(4) 
x.insert_front('ff')
x.print()
x.delete('ff')
print('-----------')
x.print()
# print('-----------')
# print(x.pop_back())
# print('+++++++++')
# x.print() 
# print('+++++++++')
# print(x.pop_front())
# print('+++++++++')
# x.print()           