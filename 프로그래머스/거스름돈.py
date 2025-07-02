# https://school.programmers.co.kr/learn/courses/30/lessons/12907

def solution(n, money):
    dp = [1] + [0]*n
    for coin in money:
        for i in range(coin, n+1):
            dp[i] += dp[i - coin] 
    return dp[n] % 1_000_000_007

print(solution(5, [1,2,5])) # 4
