import queue
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)


class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


'''
def isIdentical(tree1, tree2):
    if tree1 == None and tree2 == None:
        return True
    
    if tree1 == None or tree2 == None:
        return False
    
    q1 = queue.Queue()
    q2 = queue.Queue()
    
    q1.put(tree1)
    q2.put(tree2)
     
    l1 = []
    l2 = []
    
    while(not(q1.empty())):
        curr = q1.get()
        l1.append(curr)
        for child in curr.children:
            l1.append(child)
            q1.put(child)            
    
    while(not(q2.empty())):
        curr = q2.get()
        l2.append(curr)
        for child in curr.children:
            l2.append(child)
            q2.put(child)
            
    print(len(l1), l1)
    print(len(l2), l2)
    
    if len(l1) == len(l2):
        for i in range(len(l1)):
            print(l1[i].data, end = " ")
            print(l2[i].data)
            if l1[i].data != l2[i].data:
                return False
        return True
    else:
        return False
'''


def isIdentical(tree1, tree2):
    if tree1.data != tree2.data:
        return False
    if len(tree1.children) != len(tree2.children):
        return False
    for i in range(len(tree1.children)):
        if tree1.children[i].data != tree2.children[i].data:
            return False
    return True


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
arr1 = list(int(x) for x in stdin.readline().strip().split())
tree1 = createLevelWiseTree(arr1)
arr2 = list(int(x) for x in stdin.readline().strip().split())
tree2 = createLevelWiseTree(arr2)
if isIdentical(tree1, tree2):
    print('true')
else:
    print('false')
