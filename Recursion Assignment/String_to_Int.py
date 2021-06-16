def StringToInt(str):
    if len(str) == 1:
        return ord(str[0]) - ord('0')
    
    y = StringToInt(str[1:])
    x = ord(str[0]) - ord('0')

    x = x*(10**(len(str)-1)) + y
    return int(x)


str = input()
print(StringToInt(str))
