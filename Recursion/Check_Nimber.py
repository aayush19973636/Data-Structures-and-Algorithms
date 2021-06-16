from sys import setrecursionlimit


def checkNumber(arr, x):
    n = len(arr)

    if n == 0:
        return
    if arr[0] == x:
        return True
    return checkNumber(arr[1:], x)


# Main
setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')
