from sys import stdin


def arrayEquilibriumIndex(arr, n):
    # Your code goes here
    leftSum = []
    rightSum = []

    for i in range(n):
        if i:
            leftSum.append(arr[i] + leftSum[i-1])
            rightSum.append(rightSum[i-1] + arr[n-1-i])

        else:
            leftSum.append(arr[i])
            rightSum.append(arr[n-1])
    for i in range(n):
        if(leftSum[i] == rightSum[n - 1 - i]):
            return(i)

    return -1


# Taking input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


# main
t = int(stdin.readline().strip())

while t > 0:

    arr, n = takeInput()
    print(arrayEquilibriumIndex(arr, n))

    t -= 1
