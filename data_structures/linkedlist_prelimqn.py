
class LinkedList:

    def __init__(self, data=None):
        self.Data = data
        self.Pointer = None
        
    def insert_rec(self, data):
        if self.Data is None:
            self.Data = data
        elif self.Pointer is None:
            self.Pointer = LinkedList(data)
        else:
            self.Pointer.insert_rec(data)

    def delete_rec(self, data):
        if self.Data and self.Data == data: #Deleting first node
            if self.Pointer:
                self.Data = self.Pointer.Data
                self.Pointer = self.Pointer.Pointer
            else:
                # If the list has only one node, set it to None
                self.Data = None
        elif self.Pointer:
            if self.Pointer.Data == data: #Deleting non-first node
                self.Pointer = self.Pointer.Pointer
            else:
                self.Pointer.delete_rec(data)
        else:
            print(f"Node with ID: {data} not found")
            
    def display_rec(self): 
        if self.Data:
            print(self.Data)
        if self.Pointer:
            self.Pointer.display_rec()


dll = LinkedList()
dll.insert_rec(12)
dll.insert_rec(3243)
dll.insert_rec(34)
dll.insert_rec(100)
dll.display_rec()