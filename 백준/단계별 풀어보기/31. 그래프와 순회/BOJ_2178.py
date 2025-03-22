import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    queue = deque()
    queue.append([0, 0, 1])

    while queue:
        x, y, length = queue.popleft()
        if x == n-1 and y == m-1:
            return length
        for i in range(4):
            nx, ny = dx[i]+x, dy[i]+y

            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny, length+1])
    return length

n, m = map(int, input().split())
data = [list(map(int, list(input().strip()))) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
print(bfs())