from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildTree(postorder, inorder, n):
    if len(postorder) == 0:
        return None

    rootData = postorder[len(postorder) - 1]
    root = BinaryTreeNode(rootData)
    rootIndex = -1

    for i in range(0, len(inorder)):
        if inorder[i] == rootData:
            rootIndex = i
            break
    if rootIndex == -1:
        return None

    leftInorder = inorder[:rootIndex]
    rightInorder = inorder[rootIndex + 1:]

    x = len(leftInorder)
    leftPostorder = postorder[:x]
    rightPostorder = postorder[x:len(postorder) - 1]

    root.left = buildTree(leftPostorder, leftInorder,
                          n)    # Where to call recursion?
    root.right = buildTree(rightPostorder, rightInorder, n)

    return root
#Your code goes here


'''-------------------------- Utility Functions --------------------------'''


def printLevelWise(root):
    if root is None:
        return

    pendingNodes = queue.Queue()
    pendingNodes.put(root)
    pendingNodes.put(None)

    while not pendingNodes.empty():
        frontNode = pendingNodes.get()

        if frontNode is None:
            print()

            if not pendingNodes.empty():
                pendingNodes.put(None)

        else:
            print(frontNode.data, end=" ")

            if frontNode.left is not None:
                pendingNodes.put(frontNode.left)

            if frontNode.right is not None:
                pendingNodes.put(frontNode.right)


#Taking level-order input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0:
        return list(), list(), 0

    postorder = list(map(int, stdin.readline().strip().split(" ")))
    inorder = list(map(int, stdin.readline().strip().split(" ")))

    return postorder, inorder, n


# Main
postorder, inorder, n = takeInput()
root = buildTree(postorder, inorder, n)
printLevelWise(root)
