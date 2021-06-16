
from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

#Following is the Node class already written for the Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printReverse(head):
    prev = None
    current = head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev
    ''' 
     if head == None or head.next == None:
        return head
    rec = printReverse(head.next)
    head.next.next = head
    head.next = None
    return rec
    '''


def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        i += 1

    return head


#to print the linked list
def printLinkedList(head):

    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0:

    head = takeInput()
    newhead = printReverse(head)
    #Call PrintLinkedList function
    printLinkedList(newhead)
    print()

    t -= 1
