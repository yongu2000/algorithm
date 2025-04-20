import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(start):
    queue = deque()
    x, y, count = start
    visited[x][y] = True
    queue.append([x, y, count])
    while queue:
        x, y, count = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and zido[nx][ny] != 0 and not visited[nx][ny]:
                result[nx][ny] = count+1
                queue.append([nx, ny, count+1])
                visited[nx][ny] = True

n, m = map(int, input().split())

zido = [list(map(int, input().split())) for _ in range(n)]
result = [[0] * (m) for _ in range(n)]
visited = [[False] * (m) for _ in range(n)]


start = []
for i in range(n):
    for j in range(m):
        if zido[i][j] == 2:
            start = [i, j, 0]

bfs(start)

for i in range(n):
    for j in range(m):
        if zido[i][j] == 1 and not visited[i][j]:
            result[i][j] = -1

for r in result:
    print(*r)