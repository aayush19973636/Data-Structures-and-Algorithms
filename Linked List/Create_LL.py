class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def Input():

    L = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for current in L:
        if current == -1:
            break

        newNode = Node(current)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode

    return head

def printLL(head):
    while head is not None:
        print(str(head.value) + ' ->', end = ' ')
        head = head.next
    print("None")
    return

head = Input()
printLL(head)