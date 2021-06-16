import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def elementsInRangeK1K2(root, k1, k2):
    if root is None:
        return None
    
    elementsInRangeK1K2(root.left,k1,k2)
    
    if root.data >= k1 and root.data <= k2:
        print(root.data, end= ' ')

    elementsInRangeK1K2(root.right,k1,k2)
    
    

        #############################
        # PLEASE ADD YOUR CODE HERE #
        #############################


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
k1, k2 = (int(i) for i in input().strip().split())
elementsInRangeK1K2(root, k1, k2)
