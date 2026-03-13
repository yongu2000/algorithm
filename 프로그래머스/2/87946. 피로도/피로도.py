answer = -1

def dfs(dungeons, visited, k, cnt):
    global answer
    for i in range(len(dungeons)):
        if not visited[i]:
            if k >= dungeons[i][0]:
                visited[i] = True
                dfs(dungeons, visited, k-dungeons[i][1], cnt+1)
                visited[i] = False
    answer = max(answer, cnt)
    return

def solution(k, dungeons):
    visited = [False] * len(dungeons)
    dfs(dungeons, visited, k, 0)
    return answer