# https://school.programmers.co.kr/learn/courses/30/lessons/12900

def solution(n):
    dp = [0] * (n+1)

    if n >= 2:
        dp[2] = 2
    if n >= 3:
        dp[3] = 3

    for i in range(4, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1_000_000_007

    return dp[n] 

print(solution(2)) # 5



