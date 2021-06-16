def check(s):

    if len(s) == 0:
        return 1
    if s[0] == 'b':
        return False
    if s[0] == 'a':
        if s[1:] == 'a' or s[1] == '' or s[1:3] == 'bb':
            return check(s[3:])
        else:
            return check(s[1:])
    else:
        return False


s = input()
if check(s):
    print('true')
else:
    print('false')
