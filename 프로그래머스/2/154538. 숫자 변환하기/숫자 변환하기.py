import sys

def solution(x, y, n):
    dp = [sys.maxsize] * (y+1)
    dp[x] = 0
    
    count = 1
    for i in range(x, y+1):
        if dp[i] == -1:
            continue
        if i+n <= y:
            dp[i+n] = min(dp[i]+1, dp[i+n])
        if i*2 <= y:
            dp[i*2] = min(dp[i]+1, dp[i*2])
        if i*3 <= y:
            dp[i*3] = min(dp[i]+1, dp[i*3])

    for i, d in enumerate(dp):
        if d == sys.maxsize:
            dp[i] = -1
        
    return dp[y]