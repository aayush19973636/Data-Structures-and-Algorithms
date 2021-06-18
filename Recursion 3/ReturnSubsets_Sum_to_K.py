import sys
sys.setrecursionlimit(10 ** 8)


def subsetsSumK(arr, k):
    if len(arr) == 0:
        if k == 0:
            return [[]]
        else:
            return []

    output = []
    if arr[0] <= k:
        smallOutput = subsetsSumK(arr[1:], k-arr[0])
        if len(smallOutput) > 0:
            for i in range(len(smallOutput)):
                smallOutput[i].insert(0, arr[0])
                output.append(smallOutput[i])

    smallOutput = subsetsSumK(arr[1:], k)
    if len(smallOutput) > 0:
        for i in range(len(smallOutput)):
            output.append(smallOutput[i])
    return output


def takeInput():
    n = int(input().strip())

    if n == 0:
        return list(), 0

    arr = [int(element) for element in list(input().strip().split(" "))]
    return arr, n


#printing the list of lists
def printListOfList(liOfLi):
    for li in liOfLi:
        for elem in li:
            print(elem, end=" ")
        print()


#main
arr, n = takeInput()

if n != 0:
    k = int(input().strip())
    liOfLi = subsetsSumK(arr, k)

    printListOfList(liOfLi)
