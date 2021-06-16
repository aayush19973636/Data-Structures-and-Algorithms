from sys import stdin
import sys
import heapq as heap


class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        newNode = LinkedListNode(data)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
        return

    def dequeue(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def getSize(self):
        return self.size

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def peek(self):
        if self.head is None:
            return None
        return self.head.data


def buyTicket(arr, n, k):
    time = 0
    flag = 0
    d = {i: v for i, v in enumerate(arr)}
    for word in range(n):
        for i, v in d.copy().items():
            if v < max(d.values()):
                d.pop(i)
                d.update({i: v})

            elif flag == 1:
                break

            else:
                d.pop(i)
                time = time + 1
                
                if i == k:
                    flag = 1
    print(time)


def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return n, list(), int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    k = int(stdin.readline().strip())
    return n, arr, k


#main
sys.setrecursionlimit(10**6)
n, arr, k = takeInput()
buyTicket(arr, n, k)
