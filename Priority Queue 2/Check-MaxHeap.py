def checkMaxHeap(lst):
    n = len(lst)
    for i in range(((n-2)//2) + 1):
        parentIndex = i
        leftChildIndex = 2*parentIndex + 1 
        rightChildIndex = 2*parentIndex + 2 

        if lst[leftChildIndex] > lst[i]:
            return False
        if rightChildIndex < n and lst[rightChildIndex] > lst[i]:
            return False
    return True

# Main Code
n = int(input())
lst = list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')
