from sys import setrecursionlimit


def lastIndex(arr, x):
    n = len(arr)
    if n == 0:
        return -1
    
    smallerListOutput = lastIndex(arr[1:],x)

    if smallerListOutput != -1:
        return smallerListOutput + 1
    else:
        if arr[0] == x:
            return 0
        else:
            return -1


# Main
setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())
print(lastIndex(arr, x))
