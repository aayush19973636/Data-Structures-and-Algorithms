import queue


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def PrintTree(root):
    if root == None:
        return
    print(root.data, end=':')

    if root.left != None:
        print('L', root.left.data, end=',')

    if root.right != None:
        print('R', root.right.data, end='')

    print()

    PrintTree(root.left)
    PrintTree(root.right)

def level():
    q = queue.Queue()
    rootData = int(input())

    if rootData == -1:
        return None
    root = Node(rootData)
    q.put(root)

    while not q.empty():
        cNode = q.get()

        print('Enter left child of', cNode.data)
        leftChildData = int(input())

        if leftChildData != -1:
            leftChild = Node(leftChildData)
            cNode.left = leftChild
            q.put(leftChild)
        
        print('Enter right child of', cNode.data)
        rightChildData = int(input())

        if rightChildData != -1:
            rightChild = Node(rightChildData)
            cNode.right = rightChild
            q.put(rightChild)
    return root

root = level()
PrintTree(root)
