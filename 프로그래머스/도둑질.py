# https://school.programmers.co.kr/learn/courses/30/lessons/42897

def solution(money):
    answer = 0

    n = len(money)

    dp = [[0]*(n+1) for _ in range(3)]
    print(dp)
    # case 1: 첫집 O 마지막집 X
    for i in range(n-1):
        dp[0][i] = max(dp[0][i-2] + money[i], dp[0][i-1])
    # case 2: 첫집 X 마지막집 O
    for i in range(1, n):
        dp[1][i] = max(dp[1][i-2] + money[i], dp[1][i-1])
    # case 3: 첫집 X 마지막집 X
    for i in range(1, n-1):
        dp[2][i] = max(dp[2][i-2] + money[i], dp[2][i-1])

    for r in dp:
        answer = max(max(r), answer)
    return answer

print(solution([1, 2, 3, 1]))
