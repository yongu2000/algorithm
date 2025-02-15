n, k = map(int, input().split())
obj = []
dp = [[0] * (k+1) for _ in range(n+1)]
for _ in range(n):
    obj.append(list(map(int, input().split())))

for i in range(1, n+1):
    weight, value = obj[i-1]
    for j in range(1, k+1):
        if j - weight >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - weight] + value)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])