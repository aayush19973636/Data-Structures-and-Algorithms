from sys import stdin
from sys import maxsize as MAX_VALUE
from sys import setrecursionlimit
setrecursionlimit(10**6)
import math

def minStepsTo1(n, dp):
    if n == 0:
        return 0

    ans = MAX_VALUE
    root = int(math.sqrt(n))
    
    for i in range(1, root+1):

        newCheck = n-(i**2)

        if dp[newCheck] == -1:
            small = minStepsTo1(newCheck, dp)
            dp[newCheck] = small
            current_Ans = 1 + small

        else:
            current_Ans = 1 + dp[newCheck]
        ans = min(ans, current_Ans)
    return ans



n = int(input())
dp = [-1 for i in range(n+1)]
ans = minStepsTo1(n, dp)
print(ans)
