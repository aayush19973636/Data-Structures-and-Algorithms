import queue


class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for j in range(nVertices)]
                          for i in range(nVertices)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def bfsHelper(self, visited, source):
        q = queue.Queue()
        q.put(source)
        visited[source] = True
        while q.empty() is False:
            u = q.get()
            print(u, end=' ')
            for i in range(self.nVertices):
                if self.adjMatrix[u][i] == 1 and visited[i] is False:
                    q.put(i)
                    visited[i] = True

    def bfs(self):
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if not visited[i]:
                self.bfsHelper(visited, i)

    def __str__(self):
        return str(self.adjMatrix)


v, e = [int(x) for x in input().split()[:2]]
g = Graph(v)
for i in range(e):
    a, b = [int(x) for x in input().split()[:2]]
    g.addEdge(a, b)
g.bfs()
