from sys import stdin


def longestConsecutiveSubsequence(arr, n):
    visitedElements = {}
    elementToIndexMapping = {}
    for i in range(n):
        elementToIndexMapping[arr[i]] = i
        if arr[i] not in visitedElements:
            visitedElements[arr[i]] = True

    longestSequence = []
    maxSequenceLength = 1
    minStartIndex = 0

    for i in range(n):
        num = arr[i]
        currentMinStartIndex = i
        count = 0
        tempNum = num

        while tempNum in visitedElements and visitedElements[tempNum] == True:
            visitedElements[tempNum] = False
            count += 1
            tempNum += 1

        tempNum = num - 1
        while tempNum in visitedElements and visitedElements[tempNum] == True:
            visitedElements[tempNum] = False
            count += 1
            currentMinStartIndex = elementToIndexMapping[tempNum]
            tempNum -= 1

        if (count > maxSequenceLength):
            maxSequenceLength = count
            minStartIndex = currentMinStartIndex
        elif (count == maxSequenceLength):
            if (currentMinStartIndex < minStartIndex):
                minStartIndex = currentMinStartIndex

    startNum = arr[minStartIndex]

    longestSequence.append(startNum)
    if (maxSequenceLength > 1):
        longestSequence.append(startNum + maxSequenceLength - 1)

    return longestSequence


def takeInput():
    #To take fast I/O
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split()))
    return arr, n


# Main
arr, n = takeInput()
ans = longestConsecutiveSubsequence(arr, n)
# This ans array contains two numbers, ie, start and end of longest sequence respectively
print(*ans)
