class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)]
                          for j in range(nVertices)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def hasPathHelper(self, v1, v2, visited):

        if self.adjMatrix[v1][v2] == 1:
            return True

        visited[v1] = True

        for i in range(self.nVertices):
            if self.adjMatrix[v1][i] > 0 and visited[i] is False:
                if self.hasPathHelper(i, v2, visited):
                    return True

        return False

    def hasPath(self, v1, v2, n):
        if v1 >= self.nVertices or v2 >= self.nVertices:
            return False
        visited = [False] * n
        return self.hasPathHelper(v1, v2, visited)


v, e = [int(i) for i in input().split()[:2]]
g = Graph(v)
for i in range(e):
    a, b = [int(x) for x in input().split()[:2]]
    g.addEdge(a, b)

v1, v2 = [int(r) for r in input().split()[:2]]
if g.hasPath(v1, v2, v):
    print("true")
else:
    print("false")
