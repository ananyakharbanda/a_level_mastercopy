class BST:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert_rec(self, data):
        if self.data is None:
            self.data = data  # Set the root value
        elif data < self.data:
            if self.left is None:
                self.left = BST(data)
            else:
                self.left.insert_rec(data)
        else:
            if self.right is None:
                self.right = BST(data)
            else:
                self.right.insert_rec(data)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        if self.data is not None:  # Avoid printing None
            print(self.data, end=' ')
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        if self.data is not None:
            print(self.data, end=' ')
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        if self.data is not None:
            print(self.data, end=' ')

# Example usage
bst = BST()
bst.insert_rec(10)
bst.insert_rec(5)
bst.insert_rec(15)
bst.insert_rec(3)
bst.insert_rec(7)

print("Inorder Traversal of BST:")
bst.inorder_traversal()
print()

print("Preorder Traversal of BST:")
bst.preorder_traversal()
print()

print("Postorder Traversal of BST:")
bst.postorder_traversal()
print()
