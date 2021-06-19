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

    def __dfsHelper(self, sv, visited, list):

        list.append(sv)
        visited[sv] = True
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] > 0 and visited[i] is False:
                self.__dfsHelper(i, visited, list)

        return list

    def dfs(self):
        visited = [False for i in range(self.nVertices)]
        final_list = []
        for i in range(self.nVertices):
            if not visited[i]:
                cc = self.__dfsHelper(i, visited, [])
                final_list.append(cc)

        return final_list


v, e = [int(i) for i in input().split()[:2]]
g = Graph(v)

for i in range(e):
    a, b = [int(x) for x in input().split()[:2]]
    g.addEdge(a, b)

list = g.dfs()

for i in list:
    i.sort()
    for j in i:

        print(j, end=" ")
    print()
