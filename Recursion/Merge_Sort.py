def merge(left, right, arr):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            k += 1
            i += 1
        else:
            arr[k] = right[j]
            k += 1
            j += 1
    
    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1




def mergeSort(arr):
    # Please add your code here
    n = len(arr)
 
    if n == 1 or n ==0:
        return 
    
    mid = n//2
    left = arr[0:mid]
    right = arr[mid:]
    mergeSort(left)
    mergeSort(right)
    merge(left,right,arr)
    


# Main
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
mergeSort(arr)
print(*arr)
