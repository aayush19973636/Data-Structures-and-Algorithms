def mul(n,m):
    if n == 0 or m == 0:
        return 0
    return n*m

n, m = map(int, input().split())
print(mul(n,m))