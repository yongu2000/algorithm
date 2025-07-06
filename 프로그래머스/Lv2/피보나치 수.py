# https://school.programmers.co.kr/learn/courses/30/lessons/12945
def solution(n):
    dp = [0] * (100_001)
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n] % 1234567

print(solution(3))
print(solution(5))



