import sys

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

INF = sys.maxsize
ans = INF

for i in range(3):
    dp = [[INF] * 3 for _ in range(n)]
    dp[0][i] = data[0][i]

    for j in range(1, n):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + data[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + data[j][1]
        dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + data[j][2]

    for j in range(3):
        if i != j:
            ans = min(ans, dp[n-1][j])

print(ans)