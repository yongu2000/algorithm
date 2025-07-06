# https://school.programmers.co.kr/learn/courses/30/lessons/87946

answer = 0
n = 0
visited = []

def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for i in range(n):
        if k >= dungeons[i][0] and not visited[i]:
            visited[i] = True
            dfs(k - dungeons[i][1], cnt + 1, dungeons)
            visited[i] = False

def solution(k, dungeons):
    global n, visited
    n = len(dungeons)
    visited = [False] * n
    dfs(k, 0, dungeons)
    return answer

        

print(solution(80, [[80,20],[50,40],[30,10]]))

