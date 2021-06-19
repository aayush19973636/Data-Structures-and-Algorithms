import sys


def Edge(v1, v2, w, adjmat):
    adjmat[v1][v2] = w
    adjmat[v2][v1] = w


def getminvertex(visited, weight):
    min_vertex = -1
    for i in range(n):
        if(visited[i] is False and (min_vertex == -1 or weight[min_vertex] > weight[i])):
            min_vertex = i
    return min_vertex


def prims():
    visited = [False for i in range(n)]
    parent = [-1 for i in range(n)]
    weight = [sys.maxsize for i in range(n)]
    #weight[0]=0
    for i in range(n-1):
        min_vertex = getminvertex(visited, weight)
        visited[min_vertex] = True
        for j in range(n):
            if adjmat[min_vertex][j] > 0 and visited[j] is False:
                if weight[j] > adjmat[min_vertex][j]:
                    weight[j] = adjmat[min_vertex][j]
                    parent[j] = min_vertex
    for i in range(1, n):
        if i < parent[i]:
            print(str(i)+" "+str(parent[i])+" "+str(weight[i]))
        else:
            print(str(parent[i])+" "+str(i)+" "+str(weight[i]))


li = [int(ele) for ele in input().split()]
n = li[0]
E = li[1]
adjmat = [[0 for j in range(n)] for i in range(n)]
for i in range(E):
    curr_input = [int(ele) for ele in input().split()]
    src = curr_input[0]
    dest = curr_input[1]
    wt = curr_input[2]
    Edge(src, dest, wt, adjmat)
prims()
