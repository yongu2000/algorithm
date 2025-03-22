a = list(input())
b = list(input())

a_len = len(a) + 1
b_len = len(b) + 1

dp = [[0] * (b_len) for _ in range(a_len)]

for i in range(1, a_len):
    for j in range(1, b_len):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])