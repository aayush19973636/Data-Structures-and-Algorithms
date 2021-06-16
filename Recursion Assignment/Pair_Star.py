def pair(input, output,i = 0):

    output += input[i]
    if i == len(input)-1:
        print(output)
        return
    if input[i] == input[i+1]:
        output += '*'

    pair(input, output, i + 1)

input = str(input())
output = ''
pair(input,output)