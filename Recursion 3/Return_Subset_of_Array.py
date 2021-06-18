def subset(li):
    if len(li) == 0:
        output = []
        output.append("")
        return output
    smalloutput = subset(li[1:])

    output = []
    for i in smalloutput:
        output.append(str(i))

    for i in smalloutput:
        output.append(str(li[0])+" "+str(i))
    return output


n = int(input())
li = [int(x) for x in input().split()]
ans = subset(li)
for i in ans:
    print(i)
