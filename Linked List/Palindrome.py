''' 1. Find the middle of the LL
    2. Reverse the second half
    3. Check if first half is identical to second half
    4. Construct the original linked list by reversing the second half again and attaching it back to the first half
'''
from sys import stdin, setrecursionlimit
setrecursionlimit(10**5)

#Following is the Node class already written for the Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse(head):

    prev = None
    current = head
    next = None

    while current != None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev

def isPalindrome(head):
    if head is not None and head.next is not None:
        return True
    
    fast = head
    slow = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    
    secondHalf = slow.next
    slow.next = None
    secondHalf = reverse(secondHalf)

    firstSublist = secondHalf
    secondSublist = head

    while firstSublist is not None:
        if firstSublist.data != secondSublist.data:
            return False
        firstSublist = firstSublist.next
        secondSublist = secondSublist.next
    
    firstSublist  = head
    secondSublist  = reverse(secondHalf)

    while firstSublist.next is not None:
        firstSublist = firstSublist.next
    
    firstSublist.next = secondSublist

    return True




#Taking Input Using Fast I/O


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

    if isPalindrome(head):
        print('true')
    else:
        print('false')

    t -= 1
