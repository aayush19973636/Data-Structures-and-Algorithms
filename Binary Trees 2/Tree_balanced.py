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

def height(root):
    if root is None:
        return 0 
    return 1 + max(height(root.left), height(root.right))

def balanced(root):
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if lh - rh > 1 or rh - lh > 1:
        return
    lb = balanced(root.left)
    rb = balanced(root.right)

    if lb and rb:
        return True
    return False

    


root = tree()
PrintTree(root)
print(balanced(root))

