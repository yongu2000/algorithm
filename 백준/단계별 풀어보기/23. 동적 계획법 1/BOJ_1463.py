n = int(input())
dp = [10**6]*(n+1)
dp[-1] = 0
for i in range(n, 1, -1):
    if i % 3 == 0 and i//3 >= 1:
        dp[i//3] = min(dp[i]+1, dp[i//3])
    if i % 2 == 0 and i//2 >= 1:
        dp[i//2] = min(dp[i]+1, dp[i//2])
    dp[i-1] = min(dp[i]+1, dp[i-1])
print(dp[1])
