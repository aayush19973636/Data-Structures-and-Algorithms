def geometric(n):
    
    if n == 0:
        return 1
    return 1/pow(2,n)+ geometric(n-1)

n = int(input())
val = geometric(n)
print('%.5f' % val)
