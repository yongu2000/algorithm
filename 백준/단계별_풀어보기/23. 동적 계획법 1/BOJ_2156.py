n = int(input())
w = []
dp = [0] * n
for _ in range(n):
    w.append(int(input()))

if n <= 2:
    print(sum(w))
else:
    dp[0] = w[0]
    dp[1] = w[0] + w[1]
    dp[2] = max(w[0] + w[2], w[1] + w[2], dp[1])
    for i in range(3, n):
        dp[i] = max(dp[i-2] + w[i], dp[i-3] + w[i-1] + w[i], dp[i-1])
    print(dp[n-1])