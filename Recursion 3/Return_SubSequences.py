def subsequences(string):
    n = len(string)

    if n == 0:
        output = []
        output.append("")
        return output
    
    smallerString = string[1:]
    smallerOutput = subsequences(smallerString)

    output = []
    for sub in smallerOutput:
        output.append(sub)
    for sub in smallerOutput:
        output.append(string[0] + sub)
    
    return output

string = input()
ans = subsequences(string)
for ele in ans:
    print(ele)
