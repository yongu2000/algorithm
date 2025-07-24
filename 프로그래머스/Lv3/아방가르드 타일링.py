# https://school.programmers.co.kr/learn/courses/30/lessons/181186

def solution(n):
    dp = [0, 1, 3, 10, 23, 62, 170] + [0] * n

    for i in range(7, n+1):    
        dp[i] = (dp[i-1] + 2*dp[i-2] + 6*dp[i-3] + dp[i-4] - dp[i-6]) % 1_000_000_007
    
    return dp[n]

print(solution(2))
print(solution(3))
print(solution(4))


