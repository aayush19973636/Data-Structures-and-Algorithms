# Problem: Remove x from string
def removeX(string, a, b):
    n = len(string)

    if n == 0:
        return string

    smallout = removeX(string[1:], a, b)

    if string[0] == a:
        return b + smallout
    else:
        return string[0] + smallout


# Main
string = input()
print(removeX(string, "x", ""))
