''' Input goes from Left to Right'''


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


def tree():
    rootData = int(input())
    if rootData == -1:
        return None
    root = Node(rootData)
    leftTree = tree()
    rightTree = tree()
    root.left = leftTree
    root.right = rightTree
    return root


def num(root):
    if root == None:
        return 0
    leftCount = num(root.left)
    rightCount = num(root.right)
    return 1 + leftCount + rightCount


def largestNode(root):
    if root == None:
        return -1
    leftLargest = largestNode(root.left)
    rightLargest = largestNode(root.right)
    largest = max(leftLargest, rightLargest, root.data)
    return largest


root = tree()

PrintTree(root)
print(num(root))
print(largestNode(root))
