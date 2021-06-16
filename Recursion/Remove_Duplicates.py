# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(string):
    n = len(string)

    if n == 0 or n == 1:
        return string
    if string[0] == string[1]:  # keep the continuity and remove 0th index element
        return removeConsecutiveDuplicates(string[1:])
    else:
        smallout = removeConsecutiveDuplicates(string[1:])
        return string[0] + smallout

# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
