from sys import stdin

def lcs(s, t, i, j, dp):
    if i == len(s) or j == len(t):
        return 0

    if s[i] == t[j]:
        if dp[i+1][j+1] == -1:
            smallAns = lcs(s, t, i+1, j+1, dp)
            dp[i+1][j+1] = smallAns
            ans = 1 + smallAns
        else:
            ans = 1 + dp[i+1][j+1]

    else:
        if dp[i+1][j] == -1:
            ans1 = lcs(s, t, i+1, j, dp)
            dp[i+1][j] = ans1
        else:
            ans1 = dp[i+1][j]

        if dp[i][j+1] == -1: 
            ans2 = lcs(s, t, i, j+1, dp)
            dp[i][j+1] = ans2
        else:
            ans2 = dp[i][j+1]
        ans = max(ans1, ans2)
    return ans

    # Your code goes here

    # main
s = str(stdin.readline().rstrip())
t = str(stdin.readline().rstrip())
n = len(s)
m = len(t)
dp = [[-1 for j in range(m+1)] for i in range(n+1)]
ans = lcs(s, t, 0, 0, dp)
print(ans)
