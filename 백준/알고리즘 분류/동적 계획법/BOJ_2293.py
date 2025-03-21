import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0]*(k+1) for _ in range(n+1)]
coins = []
for _ in range(n):
    coins.append(int(input()))

print(dp)
for i in range(1, n+1):
    for j in range(1, k+1):
        if j % coins[i-1] == 0:
            dp[i][j] = 1

for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= coins[i-1]:
            dp[i][j] += dp[i-1][j-coins[i-1]] + 1

print(dp)
