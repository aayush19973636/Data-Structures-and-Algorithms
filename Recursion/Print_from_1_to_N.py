def print1toN(n):
    if n == 0:
        return
    print1toN(n-1)
    print(n)
    return


n = int(input())
print1toN(n)

def printNto1(N):
    if N== 0:
        return
    print(N)
    printNto1(N-1)
    return

N=int(input())
printNto1(N)
    
