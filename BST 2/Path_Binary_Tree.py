def NodeToRoot(root,s):
    if root is None:
        return None
    
    if root.data == s:
        l = list()
        l.append(root.data)
        return l
    
    leftOut = NodeToRoot(root.left, s)
    if leftOut != None:
        leftOut.append(root.data)
        return leftOut
    
    rightOut = NodeToRoot(root.right, s)
    if rightOut != None:
        rightOut.append(root.data)
        return rightOut
    else:
        return None
