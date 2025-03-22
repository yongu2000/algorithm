n = int(input())
nums = list(map(int, input().split()))
nums.insert(0, 0)

dp = [-1001] * (n+1)
for i in range(1, n+1):
    dp[i] = max(dp[i-1] + nums[i], nums[i])

print(max(dp)) 