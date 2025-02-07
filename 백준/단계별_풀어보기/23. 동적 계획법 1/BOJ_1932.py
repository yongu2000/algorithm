n = int(input())
triangle = []
dp = []
for i in range(n):
    triangle.append(list(map(int, input().split())))
    dp.append([0]*(i+1))
dp[0] = triangle[0]


for i in range(1, n):
    for j in range(len(triangle[i])):
        if j == 0:
            dp[i][j] = dp[i-1][0] + triangle[i][0]
        elif j == len(triangle[i])-1:
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1] + triangle[i][j], dp[i-1][j] + triangle[i][j])

print(max(dp[n-1]))
