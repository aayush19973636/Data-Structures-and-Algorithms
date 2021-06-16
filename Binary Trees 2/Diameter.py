from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def diameterOfBinaryTree(root):
    if root == None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    
    ld = diameterOfBinaryTree(root.left)
    rd = diameterOfBinaryTree(root.right)
    
    return max(lh+rh+1,ld,rd)
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


def printLevelWise(root):
    if root == None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)

    while not inputQ.empty():

        while not inputQ.empty():

            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left != None:
                outputQ.put(curr.left)
            if curr.right != None:
                outputQ.put(curr.right)

        print()
        inputQ, outputQ = outputQ, inputQ


# Main
root = takeInput()

print(diameterOfBinaryTree(root))

'''def diameter_height(node):
    if node is None:
        return 0, 0
    ld, lh = diameter_height(node.left)
    rd, rh = diameter_height(node.right)
    return max(lh + rh + 1, ld, rd), 1 + max(lh, rh)

def find_tree_diameter(node):
    d, _ = diameter_height(node)
    return d
    The function diameter_height returns the diameter and the height of the tree, 
    and find_tree_diameter uses it to just compute the diameter (by discarding the height).
'''
