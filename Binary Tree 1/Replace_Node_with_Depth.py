from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def changeToDepthTree(root, level=0):
    if root is None:
        return
    if root.data is not None:
        root.data = level
    left = changeToDepthTree(root.left, level + 1)
    right = changeToDepthTree(root.right, level + 1)


def inOrder(root):
    if root == None:
        return
    inOrder(root.left)
    print(root.data)
    inOrder(root.right)
    # Your code goes here

    # Taking level-order input using fast I/O method


def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

    if length == 1:
        return None

    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root


def inOrder(root):
    if root is None:
        return

    inOrder(root.left)
    print(root.data, end=" ")
    inOrder(root.right)


# Main
root = takeInput()

changeToDepthTree(root)
inOrder(root)
