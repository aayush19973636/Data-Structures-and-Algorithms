def uniqueChar(s):
    newString = ''

    for i in range(len(s)):
        if s[i] not in newString:
            newString += s[i]
    return newString


# Main
s = input()
print(uniqueChar(s))
