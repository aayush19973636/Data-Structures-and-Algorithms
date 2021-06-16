import queue
from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printPathsUtil(curr_node, sum,
                   sum_so_far, path):
    # empty node
    if (not curr_node):
        return
    sum_so_far += curr_node.data

    # add current node to the path
    path.append(curr_node.data)

    if (curr_node.left != None):
        printPathsUtil(curr_node.left, sum,
                       sum_so_far, path)

        # if right child exists
    if (curr_node.right != None):
        printPathsUtil(curr_node.right, sum,
                       sum_so_far, path)

    # print the required path
    if (sum_so_far == sum):

        for i in range(len(path)):
            print(path[i], end=" ")

        print()

        # if left child exists
   

        # Remove the current element
    # from the path
    path.pop(-1)


def rootToLeafPathsSumToK(root, k, lst):
    # Return true if we run out of tree and s = 0
    path = []
    printPathsUtil(root, k, 0, path)


def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length <= 0 or levelorder[0] == -1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root


# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
k = int(input())
rootToLeafPathsSumToK(root, k, [])
