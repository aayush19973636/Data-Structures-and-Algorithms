import sys


#main
sys.setrecursionlimit(10**6)


class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)


def height(tree):
    max = 0
    for child in tree.children:
        h = height(child)
        if max < h:
            max = h

    return max + 1


def numNodes(root):
    if root is None:
        return 0
    count = 1
    for child in root.children:
        count = count + numNodes(child)

    return count


def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i < size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0, childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root


# Main
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
print(height(tree))
## Read input as specified in the question.
## Print output as specified in the question.
