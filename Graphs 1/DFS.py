class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for j in range(nVertices)]
                          for i in range(nVertices)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def __dfsHelper(self, sv, visited):

        print(sv)
        visited[sv] = True
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i]>0 and visited[i] is False:
                self.__dfsHelper(i, visited)

    def dfs(self):
        visited = [False for i in range(self.nVertices)]
        self.__dfsHelper(0, visited)
    def __str__(self):
        return str(self.adjMatrix)


g = Graph(5)
g.addEdge(0, 1)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(2, 3)
g.addEdge(0, 2)
g.dfs()
print(g)
