def replaceC(s):

    n = len(s)

    if n == 0 or n == 1:
        return s
    
    if  s[0] == 'p' and s[1] == 'i':
        smallout = replaceC(s[2:])
        return '3.14' + smallout
    else:
        smallout = replaceC(s[1:])
        return s[0] + smallout

print(replaceC('pipi'))