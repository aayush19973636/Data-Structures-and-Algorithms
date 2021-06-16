from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLevelWise(root):
    q = queue.Queue()

    if root is None:
        return None
    q.put(root)

    while not q.empty():
        a = q.get()
        print(a.data, end=":")

        leftChild = a.left
        if leftChild != None:
            print('L:', end='')
            print(leftChild.data, end=',')
            q.put(leftChild)
        else:
            print('L:', end= '')
            print(-1 , end= ',')

        rightChild = a.right
        if rightChild != None:
            print('R:', end='')
            print(rightChild.data)
            q.put(rightChild)
        else:
            print('R:', end='')
            print(-1)
    return root
    # Your code goes here


#Taking level-order input using fast I/O method
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


# Main
root = takeInput()
printLevelWise(root)
