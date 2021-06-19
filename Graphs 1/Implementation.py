class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for j in range(nVertices)]for i in range(nVertices)]
    
    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    
    def remvoeEdge(self, v1, v2):
        if self.containEdge[v1][v2] is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
    
    def containEdge(self, v1, v2):
        if self.adjMatrix[v1][v2] > 0:
            return True
        else:
            return False
    
    def __str__(self):
        return str(self.adjMatrix)

g = Graph(5)
g.addEdge(0,1)
g.addEdge(1,3)
g.addEdge(2,4)
print(g)        
