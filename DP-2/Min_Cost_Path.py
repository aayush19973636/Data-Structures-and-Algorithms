
from sys import stdin
MAX_VALUE = 2147483647


def minCostPath(input, i, j,mRows, nCols):

    if i == mRows-1 and j == nCols-1:
        return input[i][j]

    if i >= mRows or j >= nCols:
        return MAX_VALUE
    ans1 = minCostPath(input, i, j+1, mRows, nCols)
    ans2 = minCostPath(input, i+1, j, mRows, nCols)
    ans3 = minCostPath(input, i+1, j+1, mRows, nCols)

    ans = input[i][j] + min(ans1, ans2, ans3)
    return ans




def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    mRows = int(li[0])
    nCols = int(li[1])

    if mRows == 0:
        return list(), 0, 0

    mat = [list(map(int, input().strip().split(" "))) for row in range(mRows)]
    return mat, mRows, nCols


#main
mat, mRows, nCols = take2DInput()
print(minCostPath(mat, 0, 0, mRows, nCols))
