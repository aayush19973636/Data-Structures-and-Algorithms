class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()

def PrintTree(root):
    if root is None:
        return
    print(root.data)
    for child in root.children:
        PrintTree(child)

def printTreeDetailed(root):
    if root == None:
        return
    print(root.data, ":", end='')
    for child in root.children:
        print(child.data, ',', end='')
    print()
    for child in root.children:
        printTreeDetailed(child)

def treeInput():
    print('Enter')

    rootData = int(input())
    if rootData == -1:
        return None
    root = TreeNode(rootData)
    print('No. of Children', rootData)
    childrenCount = int(input())
    for i in range(childrenCount):
        child = treeInput()
        root.children.append(child)
    return root

def numNodes(root):
    if root is None:
        return
    count = 1
    for child in root.children:
        count += numNodes(child)
    return count
root = treeInput()
printTreeDetailed(root)
print(numNodes)