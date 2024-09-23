class Node:
    def __init__(self):
        self.data = ''
        self.left = -1
        self.right = -1

class BST:
    def __init__(self, maxsize=20):
        self.maxsize = maxsize
        self.root = -1
        self.free = 0
        self.tree = [Node() for _ in range(self.maxsize)]
        for i in range(self.maxsize - 1):
            self.tree[i].left = i + 1

    def insert(self, item):
        if self.free != -1:  # not empty
            newnode = self.free
            self.free = self.tree[self.free].left
            self.tree[newnode].data = item
            self.tree[newnode].left = -1
            self.tree[newnode].right = -1
        else:
            print("Tree is full, cannot insert")
            return

        turnedleft = False
        prev = -1
        if self.root == -1:
            self.root = newnode
        else:
            curr = self.root
            while curr != -1:
                prev = curr
                if item < self.tree[curr].data:
                    turnedleft = True
                    curr = self.tree[curr].left
                else:
                    turnedleft = False
                    curr = self.tree[curr].right
            if turnedleft:
                self.tree[prev].left = newnode
            else:
                self.tree[prev].right = newnode

    def iterative_inorder(self):
        stack = []
        curr = self.root

        while stack or curr != -1:
            while curr != -1:
                stack.append(curr)
                curr = self.tree[curr].left

            curr = stack.pop()
            print(self.tree[curr].data, end=" ")
            curr = self.tree[curr].right

    def iterative_preorder(self):
        if self.root == -1:
            return
        
        stack = [self.root]
        
        while stack:
            curr = stack.pop()
            print(self.tree[curr].data, end=" ")

            # Push right first so left is processed next
            if self.tree[curr].right != -1:
                stack.append(self.tree[curr].right)
            if self.tree[curr].left != -1:
                stack.append(self.tree[curr].left)

    def iterative_postorder(self):
        if self.root == -1:
            return

        stack1 = [self.root]
        stack2 = []

        while stack1:
            curr = stack1.pop()
            stack2.append(curr)

            # Push left first, so right is processed next
            if self.tree[curr].left != -1:
                stack1.append(self.tree[curr].left)
            if self.tree[curr].right != -1:
                stack1.append(self.tree[curr].right)

        # Reverse process: Stack2 will have elements in reverse post-order
        while stack2:
            curr = stack2.pop()
            print(self.tree[curr].data, end=" ")

    # Recursive Inorder Traversal
    def recursive_inorder(self, root):
        if root == -1:
            return
        self.recursive_inorder(self.tree[root].left)
        print(self.tree[root].data, end=" ")
        self.recursive_inorder(self.tree[root].right)

    # Recursive Preorder Traversal
    def recursive_preorder(self, root):
        if root == -1:
            return
        print(self.tree[root].data, end=" ")
        self.recursive_preorder(self.tree[root].left)
        self.recursive_preorder(self.tree[root].right)

    # Recursive Postorder Traversal
    def recursive_postorder(self, root):
        if root == -1:
            return
        self.recursive_postorder(self.tree[root].left)
        self.recursive_postorder(self.tree[root].right)
        print(self.tree[root].data, end=" ")

# Testing the BST with iterative and recursive traversals
bst = BST()
bst.insert(22)
bst.insert(1)
bst.insert(23)
bst.insert(3)
bst.insert(5)

print("Iterative Inorder Traversal:")
bst.iterative_inorder()  # Should print: 1 3 5 22 23
print()

print("Recursive Inorder Traversal:")
bst.recursive_inorder(bst.root)  # Should print: 1 3 5 22 23
print()

print("Iterative Preorder Traversal:")
bst.iterative_preorder()  # Should print: 22 1 3 5 23
print()

print("Recursive Preorder Traversal:")
bst.recursive_preorder(bst.root)  # Should print: 22 1 3 5 23
print()

print("Iterative Postorder Traversal:")
bst.iterative_postorder()  # Should print: 5 3 1 23 22
print()

print("Recursive Postorder Traversal:")
bst.recursive_postorder(bst.root)  # Should print: 5 3 1 23 22
print()
