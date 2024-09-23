class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert_rec(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_rec_helper(data, self.root)

    def _insert_rec_helper(self, data, root):
        if data < root.data:  # Insert in the left subtree
            if root.left is None:
                root.left = Node(data)
            else:
                self._insert_rec_helper(data, root.left)
        else:  # Insert in the right subtree
            if root.right is None:
                root.right = Node(data)
            else:
                self._insert_rec_helper(data, root.right)

    def find(self, data):
        return self._find_helper(data, self.root)

    def _find_helper(self, data, root):
        if root is None:
            return False
        if data == root.data:
            return True
        elif data < root.data:
            return self._find_helper(data, root.left)
        else:
            return self._find_helper(data, root.right)

    # Recursive Traversals
    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.data, end=' ')
            self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        if root:
            print(root.data, end=' ')
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.data, end=' ')

    # Iterative Traversals
    def iterative_inorder(self):
        stack = []
        curr = self.root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            print(curr.data, end=' ')
            curr = curr.right

    def iterative_preorder(self):
        if self.root is None:
            return
        stack = [self.root]
        while stack:
            curr = stack.pop()
            print(curr.data, end=' ')
            if curr.right:  # Push right first so left is processed next
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

    def iterative_postorder(self):
        if self.root is None:
            return
        stack1 = [self.root]
        stack2 = []
        while stack1:
            curr = stack1.pop()
            stack2.append(curr)
            if curr.left:
                stack1.append(curr.left)
            if curr.right:
                stack1.append(curr.right)
        while stack2:
            curr = stack2.pop()
            print(curr.data, end=' ')

# Example usage
bst = BST()
bst.insert_rec(10)
bst.insert_rec(5)
bst.insert_rec(15)
bst.insert_rec(3)
bst.insert_rec(7)

print("Inorder Traversal of BST (Recursive):")
bst.inorder_traversal(bst.root)
print()

print("Preorder Traversal of BST (Recursive):")
bst.preorder_traversal(bst.root)
print()

print("Postorder Traversal of BST (Recursive):")
bst.postorder_traversal(bst.root)
print()

print("Inorder Traversal of BST (Iterative):")
bst.iterative_inorder()
print()

print("Preorder Traversal of BST (Iterative):")
bst.iterative_preorder()
print()

print("Postorder Traversal of BST (Iterative):")
bst.iterative_postorder()
print()

# Finding elements
print("Find 7:", bst.find(7))  # Should return True
print("Find 12:", bst.find(12))  # Should return False
