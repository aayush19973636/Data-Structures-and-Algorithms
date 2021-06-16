from sys import stdin


def pairSum0(l, n):
    d = {}
    count = 0
    for w in l:
        d[w] = d.get(w, 0) + 1
    print(d)
    for key in d:
        if key == 0:
            zero = d[0]
            count += (zero*(zero - 1)//2)
        if key > 0 and -key in d:
            a = d[key]
            b = d[-key]
            count += a*b
    return count
        


def takeInput():
    #To take fast I/O
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split()))
    return arr, n


arr, n = takeInput()
print(pairSum0(arr, n))
