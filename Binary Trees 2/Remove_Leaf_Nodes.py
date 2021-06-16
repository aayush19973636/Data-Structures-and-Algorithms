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

def remove(root):
    if root is None:
        return None
    if root.left is None and root.right is None:
        return None
    root.left = remove(root.left)
    root.right = remove(root.right)
    return root


root = tree()
PrintTree(root)
print(remove(root))
PrintTree(root)