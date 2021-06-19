from sys import setrecursionlimit
setrecursionlimit(10**6)


class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)]
                          for j in range(nVertices)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self, v1, v2):
        if self.containEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    def __str__(self):
        return str(self.adjMatrix)

    def __dfsHelper(self, sv, visited):

        visited[sv] = True
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] > 0 and visited[i] is False:
                self.__dfsHelper(i, visited)

        return visited

    def dfs(self, sv):
        visited = [False for i in range(self.nVertices)]
        return self.__dfsHelper(sv, visited)


v, e = [int(i) for i in input().split()[:2]]
g = Graph(v)
if v == 0 and e == 0:
    print("true")
else:
    for i in range(e):
        a, b = [int(x) for x in input().split()[:2]]
        g.addEdge(a, b)

    visited = g.dfs(0)
    flag = True
    for j in visited:
        if j is False:
            flag = False

    if flag:
        print("true")
    else:
        print("false")
