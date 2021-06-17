def lis(arr, i, n, dp):
    if i == n:
        return 0, 0
    include_max = 1

    for j in range(i+1, n):
        if arr[j] > arr[i]:

            if dp[j] == -1:
                ans = lis(arr, j, n, dp)
                dp[j] = ans
                further_include_max = ans[0]
            else:
                further_include_max = dp[j][0]

            include_max = max(include_max, 1 + further_include_max)
    if dp[i+1] == -1:
        ans = lis(arr, i+1, n, dp)
        dp[i+1] = ans
        exclude_max = ans[1]
    else:
        exclude_max = dp[i+1][1]

    overall_max = max(include_max, exclude_max)
    return include_max, overall_max

n = int(input())
dp = [-1 for i in range(n+1)]
arr = [int(ele) for ele in input().split() ]
ans = lis(arr, 0, n, dp)[1]
print(ans)
