def mirrorBinaryTree(root):
    if root is None:
        return
    mirrorBinaryTree(root.left)
    mirrorBinaryTree(root.right)
    root.left, root.right = root.right, root.left
