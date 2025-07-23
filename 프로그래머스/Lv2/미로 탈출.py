# https://school.programmers.co.kr/learn/courses/30/lessons/159993
from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def bfs(start, end):
        queue = deque()
        visited = [[False]*m for _ in range(n)]
        sx, sy = start
        queue.append([sx, sy, 0])
        visited[sx][sy] = True
        while queue:
            x, y, cnt = queue.popleft()

            if x == end[0] and y == end[1]:
                return cnt

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != "X":
                    visited[nx][ny] = True
                    queue.append([nx, ny, cnt+1])
        return -1

    s = []
    l = []
    e = []

    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                s = [i, j]
            elif maps[i][j] == "L":
                l = [i, j]
            elif maps[i][j] == "E":
                e = [i, j]
    lever = bfs(s, l)
    exit = bfs(l, e)

    if lever == -1:
        return -1
    if exit == -1:
        return -1
    return lever + exit

# print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"])) # 16
print(solution(["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"])) # -1













