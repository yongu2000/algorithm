# n, k = map(int, input().split())
# obj = []
# dp = [[0] * (k+1) for _ in range(n+1)]
# for _ in range(n):
#     obj.append(list(map(int, input().split())))

# for i in range(1, n+1):
#     weight, value = obj[i-1]
#     for j in range(1, k+1):
#         if j - weight >= 0:
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j - weight] + value)
#         else:
#             dp[i][j] = dp[i-1][j]

# print(dp[n][k])

n, k = map(int, input().split())
obj = []
dp1 = [0] * (k+1)
dp2 = [0] * (k+1)
for _ in range(n):
    obj.append(list(map(int, input().split())))

for o in obj:
    weight, value = o
    for i in range(weight, k+1):
        dp2[i] = max(dp1[i], dp1[i - weight] + value)
    for i in range(k+1):
        dp1[i] = dp2[i]

print(dp2[k])