from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)


class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)


def maxDataNode(tree):
    if not tree:
        return None
    maxNode = tree  # Assume that the root node has max Data
    for child in tree.children:
        temp = maxDataNode(child)
        if temp.data > maxNode.data:
            maxNode = temp
    return maxNode


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
arr = list(int(x) for x in stdin.readline().strip().split())
tree = createLevelWiseTree(arr)
print(maxDataNode(tree).data)
