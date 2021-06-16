
from sys import stdin


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def appendLastNToFirst(head, n):
    if n == 0 or head is None:
        return head

    fast = head
    slow = head
    initialHead = head

    for i in range(n):
        fast = fast.next

    while fast.next is not None:
        slow = slow.next
        fast = fast.next

    temp = slow.next
    slow.next = None
    fast.next = initialHead
    head = temp

    return head


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


def printLinkedList(head):

    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0:

    head = takeInput()
    n = int(stdin.readline().rstrip())

    head = appendLastNToFirst(head, n)
    printLinkedList(head)

    t -= 1
