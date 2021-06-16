import queue
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()


def takeTreeInputLevelWise():
    q = queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return None

    root = TreeNode(rootData)
    q.put(root)

    while (not(q.empty())):
        current_node = q.get()
        print("Enter number of childrens for ", current_node.data)
        numChildren = int(input())
        for i in range(numChildren):
            print("Enter next child for ", current_node.data)
            childData = int(input())
            child = TreeNode(childData)
            current_node.children.append(child)
            q.put(child)

    return root


def printTreeDetailed(root):
    if root == None:
        return

    print(root.data, ": ", end="")
    for child in root.children:
        print(child.data, ",", end="")

    print()

    for child in root.children:
        printTreeDetailed(child)


root = takeTreeInputLevelWise()
printTreeDetailed(root)
