import heapq

def kLargest(lst, k):
    heap = lst[:k]
    heapq.heapify(heap)
    n = len(lst)

    for i in range(k, n):
        if heap[0] < lst[i]:
            heapq.heapreplace(heap, lst[i])
    return heap    
    

# Main Code
n = int(input())
lst = list(int(i) for i in input().strip().split(' '))
k = int(input())
ans = kLargest(lst, k)
print(*ans, sep='\n')
