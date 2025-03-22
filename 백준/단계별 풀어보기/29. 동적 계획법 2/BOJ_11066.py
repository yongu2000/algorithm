import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    nums = list(map(int, input().split()))
    dp = [[0] * (k+1) for _ in range(k+1)]
    sums = [0]
    for i in range(len(nums)):
        sums.append(nums[i] + sums[i])

    for count in range(1, k+1):
        for start in range(1, k-count+1):
            end = start + count

            min_val = sys.maxsize
            for mid in range(start, end):
                min_val = min(min_val, dp[start][mid] + dp[mid+1][end])
            dp[start][end] = min_val + sums[end] - sums[start-1]

    print(dp[1][k])
