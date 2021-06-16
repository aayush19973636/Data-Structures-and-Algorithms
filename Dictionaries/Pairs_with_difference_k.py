def printPairDiffK(l, k):
    d = {}

    count = 0

    for i in l:
        if i+k in d:
            count += d[i+k]
        if i-k in d and k!=0:
            count += d[i-k]
        
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    return count
    
    
    # Main
n = int(input())
l = list(int(i) for i in input().strip().split(' '))
k = int(input())
print(printPairDiffK(l, k))



