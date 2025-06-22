# https://school.programmers.co.kr/learn/courses/30/lessons/12971

def solution(sticker):
    answer = 0
    n = len(sticker)

    dp = [[0]*(n) for _ in range(2)]

    if n == 1:
        return sticker[0]
    
    if n >= 2:
        dp[0][0] = sticker[0]
        dp[0][1] = max(dp[0][0], sticker[1])

        dp[1][0] = 0
        dp[1][1] = sticker[1]

    for i in range(2, n-1):
        dp[0][i] = max(dp[0][i-2]+sticker[i], dp[0][i-1])

    for i in range(2, n):
        dp[1][i] = max(dp[1][i-2]+sticker[i], dp[1][i-1])
    
    for d in dp:
        answer = max(max(d), answer)

    return answer

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))


