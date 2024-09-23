
class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class MemoryPool():
    def __init__(self, size):
        self.size = size
        self.nodes = [Node() for _ in range(size)]
        self.free_list = list(range(size))
    
    def allocate_node(self, data):
        index = self.free_list.pop(0)
        node = self.node[index]
        node.data = data
        node.next = None
        return index
    
    def deallocate_node(self, index):
        self.nodes[index].data = None
        self.nodes[index].next = None
        self.free_list.insert(0, index)
    

class LinkedList:
    def __init__(self, memory_pool):
        self.memory_pool = memory_pool # aggregation, a property of OOP
        self.head_index = None
    
    def insert(self, data):
        index = self.memory_pool.allocate_node(data)
        if self.head_index is not None:
            self.memory_pool.nodes[index].next = self.head_index
        self.head_index = index
    
    def delete(self, data):
        prev_index = None
        current_index = self.head_index
        while current_index is not None:
            current_node = self.memory_pool.nodes[current_index]
            if current_node.data == data:
                if prev_index is not None:
                    self.memory_pool.nodes[prev_index].next = current_node.next
                else:
                    self.head_index = current_node.next
                self.memory_pool.deallocate_node(current_index)
                return True
            prev_index = current_index
            current_index = current_node.next
        return False
    

def display(self):
    elements = []
    current_index = self.head_index
    while current_index is not None:
        current_node = self.memory_pool.nodes[current_index]
        elements.append(current_node.data)
        current_index = current_node.next
    print("Linkedlist: ", elements)


pool_size = 5
memory_pool = MemoryPool(pool_size)
linked_list = LinkedList(memory_pool)
linked_list.insert(10)
linked_list.insert(2)



