def binary(a,x, start, end):

    if start > end:
        return -1
    
    middle = (start+end)//2
    if a[middle] == x:
        return middle
    elif middle > x:
        return binary(a,x,start, middle -1)
    else:
        return binary(a,x,middle + 1, end)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary(a, 11, 0, 9))
