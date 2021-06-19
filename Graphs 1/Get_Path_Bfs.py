# Write your code here## Read input as specified in the question.
## Print output as specified in the question.
## Read input as specified in the question.
## Print output as specified in the question.
import queue
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)


class graph:
    def __init__(self, nvertices):
        self.nvertices = nvertices
        self.adjmatrix = [[0 for i in range(nvertices)]
                          for j in range(nvertices)]

    def addedge(self, v1, v2):
        self.adjmatrix[v1][v2] = 1
        self.adjmatrix[v2][v1] = 1

    def __getpathbfs(self, sv, ev, visited):
        map = {}
        q = queue.Queue()
        if self.adjmatrix[sv][ev] == 1 and sv == ev:
            ans = []
            ans.append(sv)
            return ans
        q.put(sv)
        visited[sv] = True
        while q.empty() is False:
            front = q.get()
            for i in range(self.nvertices):
                if self.adjmatrix[front][i] == 1 and visited[i] is False:
                    map[i] = front
                    q.put(i)
                    visited[i] = True
                    if i == ev:
                        ans = []
                        ans.append(ev)
                        value = map[ev]
                        while value != sv:
                            ans.append(value)
                            value = map[value]
                        ans.append(value)
                        return ans
        return []

    def getpathbfs(self, sv, ev):
        if sv > self.nvertices-1 or ev > self.nvertices-1:
            return list()
        visited = [False for i in range(self.nvertices)]
        return self.__getpathbfs(sv, ev, visited)


li = input().strip().split()
v = int(li[0])
e = int(li[1])
g = graph(v)
for i in range(e):
    arr = input().strip().split()
    fv = int(arr[0])
    sv = int(arr[1])
    g.addedge(fv, sv)
li = input().strip().split()
sv = int(li[0])
ev = int(li[1])
li = g.getpathbfs(sv, ev)
if li != None:
    for element in li:
        print(element, end=" ")
