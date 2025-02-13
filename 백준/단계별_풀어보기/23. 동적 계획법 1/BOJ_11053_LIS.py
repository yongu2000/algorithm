n = int(input())
seq = list(map(int, input().split()))
dp = [1]*n

for i in range(n):
    for j in range(i, n):
        if seq[j] > seq[i]:
            dp[j] = max(dp[i] + 1, dp[j])

print(max(dp))