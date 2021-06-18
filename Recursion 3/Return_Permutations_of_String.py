from itertools import permutations

def totalpermutations(str):
    permList = permutations(str)
    for perm in list(permList):
        print(''.join(perm))


string = input()
ans = totalpermutations(string)

