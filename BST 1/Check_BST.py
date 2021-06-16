def minTree(root):
    if root == None:
        return 100000
    leftMin = minTree(root.left)
    rightMin = minTree(root.right)
    return min(leftMin, rightMin, root.data)

def maxTree(root):
    if root == None:
        return -100000
    leftMax = maxTree(root.left)
    rightMax = maxTree(root.right)
    return max(leftMax, rightMax, root.data)

def isBST(root):
    if root is None:
        return True
    leftMax = maxTree(root.left)
    rightMin = minTree(root.right)
    if root.data > rightMin or root.left <= leftMax:
        return False
    isLeftBST = isBST(root.left)
    isRightBST = isBST(root.right)
    return isLeftBST and isRightBST