class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def printLL(head):
    while head is not None:
        print(str(head.value) + ' ->', end=' ')
        head = head.next
    print("None")
    return


def length(head):
    temp = head
    count = 0
    while temp:
        count += 1
        temp = temp.next
    return count


def insert(head, i, value):
    if i < 0 or i > length(head):
        return head

    count = 0
    prev = None
    current = head
    while count < i:
        prev = current
        current = current.next
        count += 1

    newNode = Node(value)
    if prev is not None:
        prev.next = newNode
    else:
        head = newNode
    newNode.next = current

    return head


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


head = Input()
printLL(head)
head = insert(head, 6, 10)
printLL(head)