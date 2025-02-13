n = int(input())
lines = []
dp = [1] * n
for _ in range(n):
    line = list(map(int, input().split()))
    lines.append(line)
lines.sort()

for i in range(n):
    for j in range(i, n):
        if lines[i][1] < lines[j][1]:
            dp[j] = max(dp[i] + 1, dp[j])

print(n - max(dp))