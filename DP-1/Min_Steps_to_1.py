from sys import stdin
from sys import maxsize as MAX_VALUE
from sys import setrecursionlimit
setrecursionlimit(10**6)

def countMinStepsToOne(n, dp):
    if n == 1:
        return 0
    if dp[n-1] == -1:
        ans1 = countMinStepsToOne(n-1, dp)
        dp[n-1] == ans1
    else:
        ans1 = dp[n-1]

    ans2 = MAX_VALUE
    if n % 2 == 0:
        if dp[n//2] == -1:
            ans2 = countMinStepsToOne(n//2, dp)
            dp[n//2] = ans2
        else:
            ans2 = dp[n//2]

    ans3 = MAX_VALUE
    if n % 3 == 0:
        if dp[n//3] == -1:
            ans3 = countMinStepsToOne(n//3, dp)
            dp[n//3] = ans3
        else:
            ans3 = dp[n//3]
    
    myAns = 1 + min(ans1, ans2, ans3)
    return myAns


# main
n = int(stdin.readline().rstrip())
dp = [-1 for i in range(n+1)]
print(countMinStepsToOne(n, dp))
