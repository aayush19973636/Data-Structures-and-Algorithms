class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None
        self.numNodes = 0

    def printTreeHelper(self, root):
        if root == None:
            return
        print(root.data, end = ":")
        if root.left != None:
            print("L:",end='')
            print(root.left.data,end=',')
        if root.right != None:
            print("R:",end='')
            print(root.right.data,end='')
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)


    def printTree(self):
        return self.printTreeHelper(self.root)

    def isPresentHelper(self, root, data):
        if root == None or root.data == data:
            return root

        if root.data > data:
            self.isPresentHelper(root.left, data)
        else:
            self.isPresentHelper(root.right, data)

    def isPresent(self, data):
        return self.isPresentHelper(self.root, data)

    def insertHelper(self, root, data):
        if root == None:
            node = BinaryTreeNode(data)
            return node

        if root.data > data:
            root.left = self.insertHelper(root.left, data)
            return root
        else:
            root.right = self.insertHelper(root.right, data)
            return root

    def insert(self, data):
        self.numNodes += 1
        self.root = self.insertHelper(self.root, data)
    
    def minVal(self, root):
        if root == None:
            return 10000
        if root.left is None:
            return root.data
        return self.minVal(root.left)


    def deleteHelper(self, root, data):
        if root is None:
            return False, None
        
        if root.data < data:
            deleted, newRightNode = self.deleteHelper(root.right, data)
            root.right = newRightNode
            return deleted, root
        
        if root.data > data:
            deleted, newLeftNode = self.deleteHelper(root.left, data)
            root.left = newLeftNode
            return deleted, root
        
        if root.left == None and root.right == None:
            return True, None
        if root.right == None:
            return True, root.left
        if root.left == None:
            return True, root.right
        
        replacement = self.minVal(root.right)
        root.data = replacement
        deleted, newRightNode = self.deleteHelper(root.right, replacement)
        root.right = newRightNode
        return True, root

    def delete(self, data):
        deleted, newRoot = self.deleteHelper(self.root, data)

        if deleted:
            self.numNodes -= 1
        self.root = newRoot
        return deleted

    def count(self):
        return self.numNodes


b = BST()
b.insert(10)
b.insert(5)
b.insert(7)
b.insert(6)
b.insert(8)
b.insert(12)
b.insert(11)
b.insert(15)
b.printTree()
print(b.count())

