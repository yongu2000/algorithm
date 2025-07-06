# https://school.programmers.co.kr/learn/courses/30/lessons/12904

def solution(s):
    answer = 1
    n = len(s)
    dp = [[False]*n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True
        if i < n - 1 and s[i] == s[i+1]:
            dp[i][i+1] = True
            answer = 2

    for i in range(3, n+1):
        for start in range(n - i + 1):
            end = start + i - 1
            if s[start] == s[end] and dp[start + 1][end - 1]:
                dp[start][end] = True
                answer = i

    return answer

print(solution("a")) #1
print(solution("abaabaaaaaaa")) #7
