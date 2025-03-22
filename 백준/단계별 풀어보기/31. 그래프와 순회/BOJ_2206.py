import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    queue = deque()
    queue.append([0, 0, 1, True])
    visited[0][0] = 1
    while queue:
        x, y, depth, breakable = queue.popleft()
        if x == n-1 and y == m-1:
            return depth

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] <= 0:
                if breakable and data[nx][ny] == 1:
                    queue.append([nx, ny, depth+1, False])
                    visited[nx][ny] = -1
                elif breakable and data[nx][ny] == 0:
                    queue.append([nx, ny, depth+1, breakable])
                    visited[nx][ny] = 1
                elif not breakable and data[nx][ny] == 0 and visited[nx][ny] == 0:
                    queue.append([nx, ny, depth+1, breakable])
                    visited[nx][ny] = -1
    return -1

n, m = map(int, input().split())
data = [list(map(int, list(input().strip()))) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
print(bfs())