from sys import setrecursionlimit


def firstIndex(arr, x):
    n = len(arr)
    if n == 0:
        return -1
    if arr[0] == x:
        return 0
    smallerListOutput = firstIndex(arr[1:], x)


    if smallerListOutput == -1:
        return -1
    else:
        return smallerListOutput + 1

# Main
setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())
print(firstIndex(arr, x))
